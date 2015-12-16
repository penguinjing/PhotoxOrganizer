# -*- encoding: utf-8 -*-
# heading statement
'''
文件说明：根据图片拍摄日期建立(-年/-月/-日)三级目录(备份资料库)，将文件相应
拷贝至相应日期目录中，并将图片文件名改为拍摄日期(20151210)+原图片名
作者信息：penguinjing & lixiguangzhou
版本自述: 0.2.0
...
'''
# 全局引用
import exifread
import os

# 全局变量
#PATH = "/path/2/work dir"

# 函式撰写区
def get_exif_date(filename='test_o.jpg'):
    tags = {}
    with open(filename, 'rb') as f:
        tags =exifread.process_file(f, details=False)  #  Return Exif tags as a dictionary
    ShotDateTime = tags.get('EXIF DateTimeOriginal').values
    ShotDate = ShotDateTime[:10].split(':')
    return ShotDate

def create_target_dir(TargetDir, ShotDate):
    year, month, day = ShotDate
    TargetDirJoin = os.path.join(TargetDir, year, month, day)
    os.makedirs(TargetDirJoin)

# 自检区
if __name__ == '__main__':
    print get_exif_date()
    create_target_dir('.', get_exif_date())