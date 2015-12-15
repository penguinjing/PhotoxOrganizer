# -*- encoding: utf-8 -*-
# heading statement
'''
文件说明：根据图片拍摄日期建立(-年/-月/-日)三级目录(备份资料库)，将文件相应
拷贝至相应日期目录中，并将图片文件名改为拍摄日期(20151210)+原图片名
作者信息：penguinjing
版本自述: 0.0.1
...
'''
# 全局引用
import sys
# 全局变量
PATH = "/path/2/work dir"
# 函式撰写区
def foo():
    pass
    return None

# 自检区
if __name__ == '__main__':
    if 1 != len(sys.argv):
        print '''Usage:
$ python main..py
        '''
    else:
        foo()
    