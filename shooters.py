import sys
from random import random

MAGAZINE_CAP = 12
A = 8
B = 6
C = 4

VERBOSE = False

TOTAL = 10000

def log(s):
    if VERBOSE:
        print(s)


class Player:
    def __init__(self, name, bullets, alive=True):
        self.name = name
        self.bullets = bullets
        self.alive = alive
        self.score = 0
        
    def lethal_rate(self):
        return self.bullets / MAGAZINE_CAP
        
    def triggered(self):
        r = random()
        return r <= self.lethal_rate()
        
    def __repr__(self):
        return f"{self.name}({self.bullets})"
        
    def __str__(self):
        return self.__repr__()


class Game:
    def __init__(self):
        self.players = []
        self.players_alive = []
        self.winner = None
        
    def add(self, p):
        self.players.append(p)
        self.players_alive.append(p)
        
    def shoot(self, a, b):
        if a.triggered():
            log(f"{a} shoots and kills {b}")
            a.bullets -= 1
            b.alive = False
            self.players_alive.remove(b)
        else:
            log(f"{a} shoots {b} but not triggered")            
            
    def pick(self, shooter, players):
        target = None
        for player in players:
            if player == shooter:
                continue
            if not target or target.lethal_rate() < player.lethal_rate():
                target = player
        return target
            
    def run(self):
        while len(self.players_alive) > 1:
            players = self.players_alive
            for player in players:
                target = self.pick(player, players)
                if target:
                    self.shoot(player, target)
                else:
                    log(f"No target for {player}, game over.")
                    break

        self.winner = self.players_alive[0]
        log(f"The winner is {self.winner}")
        for player in self.players:
            if self.winner == player:
                player.score += 1
                break


if __name__ == "__main__":
    running_count = TOTAL
    if len(sys.argv) > 1:
        running_count = int(sys.argv[1])

    a = Player('Jun', A)
    b = Player('Rory', B)
    c = Player('Max', C)

    def reload():
        a.bullets = A
        b.bullets = B
        c.bullets = C

    n = 1
    while n <= running_count:
        g = Game()
        reload()
        g.add(a)
        g.add(b)
        g.add(c)
        log(f"Simulation #{n}: {[f'{x}' for x in g.players]}")
        g.run()
        n += 1
        
    reload()
    print(f"Winning Board: {a} - {a.score}, {b} - {b.score}, {c} - {c.score}")