#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
from PIL import Image
from pylab import *

'''
    NumPy 中的数组对象是多维的，可以用来表示向量、矩阵和图像
    数组中的元素可以使用下标访问(value = im[i,j,k])
        im[i,:] = im[j,:] # 将第 j 行的数值赋值给第 i 行
        im[:,i] = 100 # 将第 i 列的所有数值设为 100
        im[:100,:50].sum() # 计算前 100 行、前 50 列所有数值的和
        im[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）
        im[i].mean() # 第 i 行所有数值的平均值
        im[:,-1] # 
'''

im = array(Image.open("./img/test.jpg"))

print im.shape, im.dtype

# im = array(Image.open("./img/test.jpg").convert("L"), "f")
#
# print im.shape, im.dtype

for i in range(3):
    for j in range(300):
        for k in range(534):
            value = im[j, k, i]
            print value,
        print ""
    print "----"