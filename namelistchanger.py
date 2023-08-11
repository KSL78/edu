import os
import shutil
file_path = '.././trans'

file_names = os.listdir(file_path)
i = 1
shutil.copytree(file_path,'.././trans/co')
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
###이름 변경 코어 모듈###
