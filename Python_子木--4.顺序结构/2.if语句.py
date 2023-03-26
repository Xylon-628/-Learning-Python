'''
if+条件表达式1+:
    True的执行代码
elif+条件表达式2+:
    条件2的执行代码
............
[else:
    ......]
'''
#双分支
money=1000
print('ATM','\n余额：',money)
s=float(input("取款金额"))
if money>= s :
    money=money-s
    print('取款成功，你的余额：',money)
else:
    print('余额不足')
#多分枝
print('\n成绩等级查询')
cj=float(input('输入你的成绩：'))
#1
'''if 0>=cj or cj>100 :
    print("去你码的")
elif cj>80:
    print('A级')
elif cj>60:
    print('B级')
elif cj>40:
    print('C级')
else:
    print('你考你m呢')'''
#2
if  80<=cj<=100:
    print('A级')
elif 60<=cj<80:
    print('B级')
elif 40<=cj<60:
    print('C级')
elif 0<=cj<40:
    print('你考你m呢')
else:
    print("去你码的")










