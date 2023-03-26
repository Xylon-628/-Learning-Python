a=[11,23.3,'adnf']
b=list['python',12.1,a]
print('a',a,type(a))
print('b',b,type(b))

#
#列表查询元素位置  -----------------------【列表名m】 . index(【元素】，start，stop)
m=['hello',12.3,True,45,12.3,'tr','pythhon']
print(m.index(12.3)) #如果列表中有相同元素，index只查第一个
print(m.index(12.3,1,3))  #从start 到 stop 中查询
##列表查询位置元素，列表元素有顺序，并有各自索引-------【列表名m】[位号]
print(m[1])  # 从前往后从0开始
print(m[-2]) #从后往前，从-1开始
#获取多个元素
#【列表名】[start:stop:step]--------成为一个新列表
n=[1,2,3,4,5,6,7,8,9,10]
print(n[0:5:2])
print(n[-5:-2])
print(n[::3])#--stop 默认元素数+1
print(n[8:5:-1])#---逆序输出



