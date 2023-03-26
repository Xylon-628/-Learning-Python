'''
range(b,a,c)
#从b开始，相差c,一直到 a-1
默认b=0,c=1
'''

#只有一个值
a=10
r=range(a)
print(r)  #range(0, 10)----迭代器对象
print(list(r))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]----查看range对象的整数序列,,list__序列
# 默认从0开始，默认相差1,一直到 a-1
#两个值
b=1
r=range(b,a)
print(r)
print(list(r)) #从b开始，默认相差1,一直到 a-1
#三个数
c=2
r=range(b,a,c)
print(r)
print(list(r))#从b开始，相差c,一直到 a-1






