import math


class vector:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.y = y
        self.z = z
        self.x = x

    def add(self, vector1):
        self.x += vector1.x
        self.y += vector1.y
        self.z += vector1.z

    def sub(self, vector1):
        self.x -= vector1.x
        self.y -= vector1.y
        self.z -= vector1.z

    def mul(self, k):
        self.x *= k
        self.z *= k
        self.y *= k

    def div(self, k):
        self.x /= k
        self.z /= k
        self.y /= k

    def get_length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def p(self):
        a = [str(self.x), str(self.y), str(self.z)]
        print(" ".join(a))


if __name__ == '__main__':

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    v1 = vector(a[0], a[1], a[2])
    v2 = vector(b[0], b[1], b[2])
    #print("%.2f" % (float(v1.x) / 2.0) + " " + "%.2f" % (float(v1.y) / 2.0) + " " + "%.2f" % (float(v1.z) / 2.0))
    command = input()
    if command == "add":
        v1.add(v2)
        v1.p()
    elif command == "sub":
        v1.sub(v2)
        v1.p()
    elif command == "mul":
        v1.mul(int(input()))
        v1.p()
    elif command == "div ":
        k = float(input())
        print("%.2f" % (v1.x / k) + " " + "%.2f" % (v1.y/ k) + " " + "%.2f" % (v1.z / k))
    elif command == 'get_length':
        print("%.2f" % v1.get_length())
