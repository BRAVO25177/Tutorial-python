from images import Image
from functools import reduce

image = Image('myth.gif')

def blur(image):
   
    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)
    new = image.clone()

    for y in range(1, image.getHeight() - 1):
        for x in range(1, image.getWidth() - 1):
            
            oldP = image.getPixel(x, y)
            left = image.getPixel(x - 1, y) 
            right = image.getPixel(x + 1, y) 
            top = image.getPixel(x, y - 1) 
            bottom = image.getPixel(x, y + 1) 
            sums = reduce(tripleSum, [oldP, left, right, top, bottom])
            averages = tuple(map(lambda x: x // 5, sums))
            new.setPixel(x, y, averages)
    new.draw()
newy=image.getHeight()//2
newx=image.getWidth()//2
small=Image(newx,newy)


def shrink():
    for x in range(newx):
        for y in range(newy):
            color=image.getPixel(2*x,2*y)
            small.setPixel(x,y,(color))
    small.draw()

shrink()