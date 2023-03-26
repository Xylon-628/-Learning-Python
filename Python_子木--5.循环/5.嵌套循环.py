print('三行四列')
for o in range(3):
    for p in range(4):
        print('*',end='\t')     #取消换行
    print()       #换行

print('乘法表')
for a in range(1,10):
    for b in  range(1,10):  #    for b in  range(1,a+1):
        if b>a :            #
            break           #
        else:
            print(a, end="*")
            print(b, end="=")
            print(a*b,end='\t')
    print()


print('乘法表')
for a in range(1,10):
    for b in  range(1,a+1):  #    for b in  range(1,a+1):
            print(a, end="*")
            print(b, end="=")
            print(a*b,end='\t')
    print()

