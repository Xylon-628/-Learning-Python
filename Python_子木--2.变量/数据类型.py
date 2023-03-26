#整数类型-int -- 98
#浮点数类型-float -- 3.1415926
#布尔类型-bool--  True、False
#字符串类型-str--人生苦短，我用Python
#1.整数类型—二进制--0b，八进制--0o，十六进制--0x
print(2048)
print(0b1001101)
print(0o47322)
print(0x6F8C)
print(type(0o3224))
#2.浮点数类型__浮点数存储不精确
a=1.1
b=2.2
print(type (a))
print(a+b)
#   解决——导入模块
from decimal import Decimal
print (Decimal('1.1')+Decimal('2.2'))
#3.布尔类型__表示真假，布尔值可转化为整数，True-1，False-0
f1=True
f2=False
print(type(f1))
print(f1)
print(f1+f2)
#4.字符串类型  字符串又称不可变的字符序列,可使用单，双，三引号定义，三引号可在多行显示
str1='人生苦短，我用Python'
str2="人生苦短，我用Python"
str3='''人生苦短，
我用Python'''
str4='人生苦短，' \
     '我用Python'
str5=''''人生苦短，我用Python'''''
print(type(str1))
print(str4)

