##流水灯显示

import os
import time

contain = '  永远支持五月天  '
while True:
    os.system('cls')
    print(contain)
    time.sleep(0.001)
    contain = contain[1:] + contain[0]



"""设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成"""

import random

char = '0123456789zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP'
char_len = int(input("please enter the length of the varifi_number :"))
code = ''
for x in range(0,char_len):
    code += (char[random.randint(0,len(char) - 1)])
print(code)