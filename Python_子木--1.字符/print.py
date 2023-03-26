#--输出函数--print( ) （#--注释）
#	内容  数字，'字符串'，含有运算符的表达式
#	输出目的地	显示器(控制台)，文件
#	输出形式  换行，不换行
##数字
print(52.01314)
#字符串  加引号(' '或 " ")--告诉计算机内容不需要理解
print("helloword")
#含有运算符的表达式
print(3+4)
print(3*4-4)
#输出到文件（桌面位置C:\Users\86186\Desktop）  注意：路径要存在，要使用 file=变量
fp=open('E:/text.txt','a+') #fp--变量，a+--以读写方式打开，没有就新建
print('helloworld',file=fp)
fp.close()

#取消换行
print('hello','world','Python')
print('hello''world''Python')
