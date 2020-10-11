# Sep, 29th, 2020 @ OMGlost

import os
import re

#待检测目录
path_input = "C:/Users/wqstu/Desktop/test/new6/"
#输出目录
path_output = "C:/Users/wqstu/Desktop/test_output/"
# 匹配字段  #send为可调匹配字段
matchfield = re.compile(r'send|ien')

A_list = os.listdir(path_input)

for A_str in A_list:
    file_path = path_input + A_str
    file = open(file_path)
    # # 匹配字段  #send为可调匹配字段
    # matchfield = re.compile(r'send|ien')
    file_content = file.read()
    file.close()
    try:
        matched_field = matchfield.search(file_content).group()
        # print(matched_field)
    except AttributeError:
        path_origin = path_input + A_str
        #‘.txt’可以调节为其他的后缀
        path_new = path_output + A_str + '.txt'
        os.rename(path_origin, path_new)
