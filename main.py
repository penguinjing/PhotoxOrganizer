# -*- encoding: utf-8 -*-
# heading statement
'''
文件说明：根据图片拍摄日期建立(-年/-月/-日)三级目录(备份资料库)，将文件相应
拷贝至相应日期目录中，并将图片文件名改为拍摄日期(20151210)+原图片名
作者信息：penguinjing & lixiguangzhou
版本自述: 0.3.1
...
'''
# 全局引用
import os
import exifread
import shutil

# 全局变量
#PATH = "/path/2/work dir"

# 函式撰写区
def get_exif_date(FileName='./test_o.jpg'):
    tags = {}
    with open(FileName, 'rb') as f:
        tags =exifread.process_file(f, details=False)  #  Return Exif tags as a dictionary
    shotDateTime = tags.get('EXIF DateTimeOriginal').values
    shotDate = shotDateTime[:10].split(':')
    return shotDate

def create_target_dir(TargetDir, ShotDate):
    year, month, day = ShotDate
    targetDirJoin = os.path.join(TargetDir, year, month, day)
    os.makedirs(targetDirJoin)

def copy_image_file(FileName, TargetDir, ShotDate):
    year, month, day = ShotDate
    newFileName = year + month + day + '_' + os.path.basename(FileName)
    targetFileName = os.path.join(TargetDir, year, month, day, newFileName)
    shutil.copy2(FileName, targetFileName)


# 自检区
if __name__ == '__main__':
    image_date = get_exif_date()
    create_target_dir(TargetDir = '.', ShotDate = image_date)
    copy_image_file(FileName='./test_o.jpg', TargetDir = '.', ShotDate = image_date)