class Mandelbrot:
    def __init__(self, c, max_iter = 100):
        self.c = c
        self.max_iter = max_iter
    
    def isMandel(self, coord):
        real_number, image_number = coord
        for _ in range(self.max_iter):
            real_number, image_number = (
                real_number ** 2 - image_number ** 2 + self.c,
                2 * real_number * image_number
            )
            if self.isDivergence(real_number, image_number):
                return 0
        return 1
    
    def isDivergence(self, x, y):
        return (x ** 2 + y ** 2 > 4)

if __name__ == "__main__":
    c = 2
    mab = Mandelbrot(-2)
    for i in range(10 + 1):
        for j in range(10 + 1):
            coord = -1 + 2 * i / 10, -1 + 2 * j / 10
            if mab.isMandel(coord):
                print("{} + {}i".format(coord[0], coord[1])) if coord[1] != 0 else print("{}".format(coord[0]))