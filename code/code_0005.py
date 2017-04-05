"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

from PIL import Image
import glob


def zoom_pic(file):
    image = Image.open(file)
    size_y = 640
    size_x = 1136
    pic_type = file.split(".")[-1]
    if pic_type == 'jpg':
        pic_type = 'jpeg'
    out = image.resize((size_x, size_y), Image.ANTIALIAS)
    file_out = '../resize/' + file.split(".")[-2].split('/')[-1] + 'resize.' + file.split(".")[-1]
    print(file_out)
    out.save(file_out, pic_type)


if __name__ == '__main__':
    for file in glob.glob('../imgs/*'):
        zoom_pic(file)
