print('中国珠宝')
qq=float(input('总计：'))
zh=int(input('账号：'))
if zh == 123  :
    print('会员')
    if qq >=200:
        print('给你6折，付款：',qq*0.6)
        print('抽奖：')
        a=int(input('猜数字：'))
        if a == 123:
            print('牛B，送你只袜子')
        else:
            print('谢谢惠顾')
    elif qq>=100:
        print('8折，支付：',qq*0.8)
    else:
        print('9折，支付：',qq*0.9)
else:
    if qq >=200:
        print('9折，支付：',qq*0.9)
    else:
        print('qb,支付：',qq)









