print('ATM\n输入密码')
for x in range(3):
    a=input('输入')
    if a=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:                   #-------------循环结束后执行
    print('此卡已经被冻结')



