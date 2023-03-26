#、str( )——将其他类型转成str类型，print(str(a1))
a1=12.5
a2=False
a3='python'
print(type(a1),type(a2),type(a3))
print(str(a1),str(a2),str(a3))
a1=str(a1)
print(type(a1))

# int( )——将其他类型转成int类型，print(int(b2))
b1=12.6  #float类型转int类型，只截取整数部分
b2=True  #str类型转int类型，只能是整数
b3='1233'
print(type(b1),type(b2),type(b3))
print(int(b1),int(b2),int(b3))
b2=int(b2)
print(b2,type(b2))

# float( )函数   字符串不能转，整数转成整数+.0
#......

