#标准算术
print(1+1)
print(1-1)
print(2*4)
print(11/2)
#整除
print(11//2)
#取余
print(11%2)
#幂运算  2**2--2的2次方  2**3--2的3次方
print(2**2)
print(2**3)

#正负数整除、取余   A*B<0
#A//b=-|A|//|B|-1
#A%b=A-B*A//B---被除数-除数*整除商
a=-11
b=3
print('a=',a,'b=',b)
c=a//b
d=a%b
print('a/b=',a/b,'\na//b=',c,'\na%b=',d)
print('验证：','a%b=a-b*a//b=',a-b*c)
print('a-b=',a-b,'a//b',c,b*c)
a=11
b=-3
print('\na=',a,'b=',b)
c=a//b
d=a%b
print('a/b=',a/b,'\na//b=',c,'\na%b=',d)
print('验证：','a%b=a-b*a//b=a-((b*a)//b)',a,'-','((',b,'*',a,')','//',b,')')
print('a-b=',a-b,'a//b',c,b*c)



