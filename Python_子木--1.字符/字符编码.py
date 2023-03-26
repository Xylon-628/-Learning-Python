#ASCLL表，Unicode汉字编码表 在计算机上把字符与编码一一对应
#chr（）  函数   ---输入编码转换汉字
#ord( )  函数   ---输入汉字转换编码，输出为十进制
print(chr(0b100111001011000))  #0b--告诉计算机数字为二进制
print(chr(20056))
print(ord('乘'))
print(chr(ord('乘')))  #套娃
print(chr(0b01000001))

