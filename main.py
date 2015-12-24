# -*- encoding: utf-8 -*-
# heading statement
'''
文件说明：根据图片拍摄日期建立(-年/-月/-日)三级目录(备份资料库)，将文件相应
拷贝至相应日期目录中，并将图片文件名改为拍摄日期(20151210)+原图片名
作者信息：penguinjing & lixiguangzhou
版本自述: 0.4.1
'''
# 全局引用
import os
import exifread
import shutil
from sys import argv

# 全局变量
#PATH = "/path/2/work dir"

# 函式撰写区
def print_prompt():
    print "  ____   _             _                                     "
    print " |  _ \ | |__    ___  | |_  ___                              "
    print " | |_) || '_ \  / _ \ | __|/ _ \                             "
    print " |  __/ | | | || (_) || |_| (_) |                            "
    print " |_|    |_|_|_| \___/  \__|\___/           _                 "
    print "  __  __  / _ \  _ __  __ _   __ _  _ __  (_) ____ ___  _ __ "
    print "  \ \/ / | | | || '__|/ _` | / _` || '_ \ | ||_  // _ \| '__|"
    print "   >  <  | |_| || |  | (_| || (_| || | | || | / /|  __/| |   "
    print "  /_/\_\  \___/ |_|   \__, | \__,_||_| |_||_|/___|\___||_|   "
    print "                      |___/                                  "
    print '\nAutomatic sort photos by shotting date and backup it.\n'
    print "usage: python main.py <original dir> <target dir>"

def get_all_jpg(path):
    alljpgfilelist = []
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename[-4:] == '.jpg':
                alljpgfilelist.append(filename)
    return alljpgfilelist

def get_exif_date(FileName):
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

def copy_image_file(FullFileName, TargetDir, ShotDate):
    year, month, day = ShotDate
    newFileName = year + month + day + '_' + os.path.basename(FullFileName)
    targetFullFileName = os.path.join(TargetDir, year, month, day, newFileName)
    shutil.copy(FullFileName, targetFullFileName)

# 自检区
if __name__ == '__main__':
    if len(argv) in [1, 2]:
        print_prompt()

    if len(argv) == 3 and os.path.exists(sourcedir)\
    and os.path.exists(targetdir):
        selfname, sourcedir, targetdir = argv
        for jpgfile in get_all_jpg(sourcedir):
            image_date = get_exif_date(jpgfile)
            create_target_dir(targetdir, ShotDate = image_date)
            copy_image_file(jpgfile, targetdir, ShotDate = image_date)