a=0
b=False
print(a>=b)
print(a is b)
print(a != b)  #!=为不等号

'''
布尔运算
and (并且)  True and True---True    other---False  
or（或者）  False and False---False    other---True
not（非）  结果取反
'''
a=3
b=4
c=6
print(b>a and c>b)
print(b>c and c>b)
print(b>a or c>b)
print(b>c or a>b)
print(not b>c)
#in 与 not in___是否在里面
s='hello'
print('e' in s)
print('k'not in s)