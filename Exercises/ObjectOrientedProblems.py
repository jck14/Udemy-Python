from math import sqrt

class Line:

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

        self.coord1x = coord1[0]
        self.coord1y = coord1[1]
        self.coord2x = coord2[0]
        self.coord2y = coord2[1]

        self.xlen = abs(self.coord1x - self.coord2x)
        self.ylen = abs(self.coord1y - self.coord2y)

    def distance(self):
        return sqrt(self.xlen**2 + self.ylen**2)

    def slope(self):
        return self.ylen/self.xlen



if __name__ == '__main__':

    line1 = Line((0,0),(4,3))
    print(line1.distance())
    print(line1.slope())