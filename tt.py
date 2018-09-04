
import math
dayfactor=0.01
dayup=math.pow((1.0+dayfactor),365)
daydown=math.pow((1.0-dayfactor),365)
print("向上：{:.2f},向下：{:.2f}.".format(dayup,daydown)) #输出小数点后两位
 
#导包
import math  #函数名需要加上模块名字
math.ceil(10.2)
from math import floor  #函数名可直接使用
floor(10.2)
from math import *    #导入全部的函数
 
TempStr="103C"
print(eval(TempStr[0:-1]))
input( )