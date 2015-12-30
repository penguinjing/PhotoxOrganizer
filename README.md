# PhotoxOrganizer 
### 个人照片备份整理程序

本程序帮助你自动根据拍摄的年月日将照片文件(.jpg)拷贝至一个指定目录下的-年/-月/-日三级目录中备份归档, 让你有个全面完整的个人图片备份仓库。  
原图片文件并不会删除。

###### 三级目录结构示意

```
temp_photos/
├── IMG224924.jpg
├── IMG134015.jpg
├── IMG134031.jpg
├── IMG211327.jpg
├── Subfolders
│   ├── Photo110.jpg
│   ├── Photo119.jpg
│   └── Photo120.jpg
└── IMG211429.jpg
```

```
-/...
-/Year2010/...
-/Year2011/...
-/Year2012/...
-/Year2013/01-Jan/...
-/Year2013/02-Feb/...
-/Year2013/03-Mar/...
-/Year2014/05-May/20100501/...
-/Year2014/05-May/20100502/...
-/Year2014/05-May/20100510/20100510_img110.jpg
                           20100510_img119.jpg
                           20100510_img120.jpg
                           20100510_img3456.jpg
                           20100510_img345337.jpg
                           ...
```

### 用法

`$python main.py <original dir> <target dir>`

> 参数目录说明  
> `<orginal dir>` - 待整理图片源目录(包括其所在的子目录) e.g. ../temp_photos
> `<target dir>`  - 整理好的图片放置的目标目录 e.g. ../photobase


### 安装
1. 安装 [Python 2.7.11](https://www.python.org/downloads/release/python-2711/) 运行环境 - 选择对应你机器操作系统的版本下载安装
2. 下载 [本仓库](https://github.com/penguinjing/PhotoxOrganizer) 中main.py程序 - 在文件上点击右键另存到本地
3. 安装下面Python包依赖关系

### Python包依赖关系

本程序须依赖Python中exif-py包。请参考下面安装exif-py包  
`$pip install exifread`