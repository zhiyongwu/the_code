"""
使用 Python 生成类似于下图中的字母验证码图片
https://camo.githubusercontent.com/f80e7aa0d43b3685657b4d329f2809a28c82e12a/687474703a2f2f692e696d6775722e636f6d2f615668626567562e6a7067
"""
from PIL import Image
from PIL import ImageColor, ImageDraw, ImageFont, ImageFilter
import random, string


def get_rand_letter():
    return random.choice(string.ascii_letters)


def get_rand_fill():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def get_font_rand_fill():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def get_random_pic():
    width = 50 * 4
    height = 50
    img = Image.new('RGB', (width, height))

    font = ImageFont.truetype('../font/calibri.ttf', 50)
    draw = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=get_rand_fill())
    for i in range(4):
        draw.text((50 * i + 20, 10), get_rand_letter(), font=font, fill=get_font_rand_fill())
    for i in range(3):
        draw.line([(random.randint(0, width), random.randint(0, height)),
                   (random.randint(0, width), random.randint(0, height))
                   ], fill=get_font_rand_fill())
    # img = img.filter(ImageFilter.EDGE_ENHANCE).filter(ImageFilter.GaussianBlur)
    img.show()


if __name__ == '__main__':
    get_random_pic()
