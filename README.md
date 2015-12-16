# PhotoxOrganizer

## 照片exif中读取拍摄日期
采用模块读取字段 EXIF.Photo.DateTimeOriginal

tags.get('EXIF DateTimeOriginal').values

```
import exifread

filename = open(path_name, 'rb')
tags =exifread.process_file(filename)  #  Return Exif tags as a dictionary
```

类似字段 EXIF.Photo.DateTimeDigitized

Reference: [Standard Exif Tags from Metadata reference tables](http://www.exiv2.org/tags.html) at www.exiv2.org


## 有用的函数
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

os.path.exists(path)
os.mkdir()

from PIL.ExifTags import TAGS
