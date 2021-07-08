import numpy as np

print("Hello Copilot!")

class Test:
    def __init__(self, name):
        self.name = name


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[3, 2, 1], [7, 8, 9]])
c = np.array([[4, 4, 4], [11, 13, 15]])
d = np.array([[7, 6, 5], [18, 21, 24]])

def vector_add(a, b):
    return a + b

def test_vector_add():
    print("Testing vector_add()...", end="")
    assert(vector_add(a, b) == c)
    assert(vector_add(b, c) == d)
    print("Passed!")

print(vector_add(a, b))
test_vector_add()