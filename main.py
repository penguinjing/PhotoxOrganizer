# -*- encoding: utf-8 -*-
# heading statement
'''
文件说明：根据图片拍摄日期建立(-年/-月/-日)三级目录(备份资料库)，将文件相应
拷贝至相应日期目录中，并将图片文件名改为拍摄日期(20151210)+原图片名
作者信息：penguinjing & lixiguangzhou
版本自述: 0.1.0
...
'''
# 全局引用
import exifread

# 全局变量
#PATH = "/path/2/work dir"

# 函式撰写区
def get_exif_date(filename='test_o.jpg'):
    tags = {}
    f = open(filename, 'rb')
    tags =exifread.process_file(f)  #  Return Exif tags as a dictionary
    ShotDateTime = tags.get('EXIF DateTimeOriginal').values
    ShotDate = ShotDateTime[:10].split(':')
    return ShotDate

# 自检区
if __name__ == '__main__':
    print get_exif_date()