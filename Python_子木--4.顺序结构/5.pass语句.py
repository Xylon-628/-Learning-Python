#pass--不执行任何程序，充当一个占位符

money=1000
print('ATM','\n余额：',money)
s=float(input("取款金额"))
if money< s :
    pass  # --------占位
else:
    money = money - s
    print('取款成功，你的余额：', money)
print('结束')





