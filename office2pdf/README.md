# office2pdf
convert(print) office file(doc, ppt) to pdf file

转换（打印）同文件夹和子文件夹下的 office 文件到pdf文件，兼容设备以便浏览。

需要安装 comtypes 库。pip install comtypes

只写了转换doc(x)，ppt(x)的部分，其他格式文件的写法可以在 https://docs.microsoft.com/zh-cn/office/vba/api/powerpoint.presentation.saveas 这样的微软官方说明文档页面找到，大同小异。

如果由于文件损坏出错，在自动打开的文件夹中找到损坏的文件，用office修复后按提示继续即可。
