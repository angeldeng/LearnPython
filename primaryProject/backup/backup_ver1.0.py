#导入 os time包
import os
import time
# 1. 需要备份的文件和目录由一个列表指定
source=['D:\\Chinasofti']
# 2. 备份必须存在一个主备份目录中
target_dir='D:\\pythonCodeBackup'  #这里可以改变主目录
# 3. 文件会被备份为一个 zip 文件。

# 4. 这个 zip 文件以当前的日期和时间命名。
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 5. 我们使用 zip 命令将文件归档成一个 zip.
zip_command = "D:\\GnuWin32\\bin\\zip.exe -qr {0} {1}".format(target, ' '.join(source))

#1.将WinRAR软件安装路径加入环境变量的系统
#此时在cmd命令行下面可以正常运行，但是在pycharm中运行报错。因为os可能与系统包含路径有出入。
#2.将python程序中的zip或winrar命令改为安装路径
#*注意此处路径不要加引号
#zip_command="D:\winRAR\WinRAR.exe A {0} {1}".format(target, ''.join(source))
#Done!!'''

# 执行备份
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')