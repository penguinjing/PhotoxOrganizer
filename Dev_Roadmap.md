## 开发路线图

#### version 0.0 
- [x] 建立Python程序通用空框架

#### version 0.1~0.3 by penguin
- [x] 实现读取单一文件中exif中拍摄日期并将日期字符串切片成'年''月''日'三段。
    - [x] 采用Pillow 读取exif中拍摄日期字段 => 发现太复杂，转采用exif.py 项目
    - [x] 采用exif.py 中的exifread模块，读取exif中拍摄日期字段EXIF DateTimeOriginal
- [x] 实现按3个字符串'年''月''日'来建立目录
- [x] 拷贝文件至指定字符串'年''月''日'组合成的字符串路径中, 改文件名为拍摄日期前缀'20100510_'+ 原图片名

#### version 0.4 by penguin
- [x] 循环检索指定的目录下所有图片文件(.jpg)制造个路径文件名列表

#### 测试

- [x] 测试两个命令行的参数传递进来的必须是路径
- [x] 测试传递绝对路径参数是否ok
- [x] 测试转递相对路径参数是否ok
- [x] 测试.jpg无拍摄日期字段的情况
- [x] 测试拍摄日期目录已建立的情况
- [x] 测试如果在目标位置已有同名文件，弹出提示，由客户修改新文件名进行备份

## Reference:

#### 照片exif中读取拍摄日期
采用模块读取字段 EXIF.Photo.DateTimeOriginal

tags.get('EXIF DateTimeOriginal').values

```
import exifread

filename = open(path_name, 'rb')
tags =exifread.process_file(filename, details=False)  #  Return Exif tags as a dictionary
```

类似字段 EXIF.Photo.DateTimeDigitized

[Standard Exif Tags from Metadata reference tables](http://www.exiv2.org/tags.html) at www.exiv2.org


#### 有用的函数
import os
os.path.join()
os.getcwd()
os.chdir()
os.makedirs()
os.path.abspath(path)
os.path.isabs(path)
os.pathrelpath(path, start)
os.path.dirname(path)
os.path.basename(path)
os.path.sep() => / (POSIX) or \\ (Windows)
os.name() => posix (Mac/Linux) or nt (windows)

os.path.exists(path)
os.mkdir()

from PIL.ExifTags import TAGS