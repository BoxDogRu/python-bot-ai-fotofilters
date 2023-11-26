from PIL import Image
from random import randint

class red_Filter():
    def __init__(self, image):
        self.image = image

    def get_filter(self):
        img = Image.open(self.image)
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                r = min(255, int(r * 1))
                g = min(255, int(g * 0))
                b = min(255, int(b * 0))
                img.putpixel((x, y), (r, g, b))
        img.show()

    def img_save(self, name):
        img = Image.open(self.image)
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                r = min(255, int(r * 1))
                g = min(255, int(g * 0))
                b = min(255, int(b * 0))
                img.putpixel((x, y), (r, g, b))
        img.save(name)

class green_Filter():
    def __init__(self, image):
        self.image = image

    def get_filter(self):
        img = Image.open(self.image)
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                r = min(255, int(r * 0))
                g = min(255, int(g * 1))
                b = min(255, int(b * 0))
                img.putpixel((x, y), (r, g, b))
        img.show()

    def img_save(self, name):
        img = Image.open(self.image)
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                r = min(255, int(r * 0))
                g = min(255, int(g * 1))
                b = min(255, int(b * 0))
                img.putpixel((x, y), (r, g, b))
        img.save(name)

class blue_Filter():
    def __init__(self, image):
        self.image = image

    def get_filter(self):
        img = Image.open(self.image)
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                r = min(255, int(r * 0))
                g = min(255, int(g * 0))
                b = min(255, int(b * 1))
                img.putpixel((x, y), (r, g, b))
        img.show()

    def img_save(self, name):
        img = Image.open(self.image)
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                r = min(255, int(r * 0))
                g = min(255, int(g * 0))
                b = min(255, int(b * 1))
                img.putpixel((x, y), (r, g, b))
        img.save(name)

class bw_Filter():
    def __init__(self, image):
        self.image = image

    def get_filter(self):
        img = Image.open(self.image).convert('L')
        img.show()

    def img_save(self, direction):
        img = Image.open(self.image).convert("L")
        img.save(direction)

class bw_reverse_Filter():
    def __init__(self, image):
        self.image = image

    def get_filter(self):
        img = Image.open(self.image).convert("L")
        pixel_values = list(img.getdata())
        transformed_pixel_values = [255 - value for value in pixel_values]
        img.putdata(transformed_pixel_values)
        img.show()

    def img_save(self, name):
        img = Image.open(self.image).convert("L")
        pixel_values = list(img.getdata())
        transformed_pixel_values = [255 - value for value in pixel_values]
        img.putdata(transformed_pixel_values)
        img.save(name)

class bitie_pixeli_Filter():
    def __init__(self, image):
        self.image = image

    def get_filter(self):
        img = Image.open(self.image)
        for x in range(img.width, randint(0, 100)):
            for y in range(img.height, randint(0, 100)):
                pixel = img.getpixel(x, y)
                print(pixel)
        img.show()

    def img_save(self, name):
        img = Image.open(self.image)
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                r = min(255, int(r * 0))
                g = min(255, int(g * 0))
                b = min(255, int(b * 1))
                img.putpixel((x, y), (r, g, b))
        img.save(name)