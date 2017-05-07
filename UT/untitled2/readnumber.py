# encoding:UTF-8

import csv

#读取本地csv文件

date = csv.reader(open('info.csv','r'))

# 循环输出每一行信息
for user in date:
    print(user)
    print (user[1])


