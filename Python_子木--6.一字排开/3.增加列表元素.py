lst=[1,2,3,4,5,6,7,8]
a=[90,80,70,60,50]
#append---------------------在末尾添加元素【列表名】.append(添加元素)
print(lst,id(lst))
lst.append(10)    #仍是原来列表，ID不变
print(lst,id(lst))
#lst.append(lst)
#print(lst,id(lst))
#extend-----------------------在末尾添加至少一个元素
lst.extend(a)
print(lst)
#insert----------------------在某一位置后面添加一个元素  【】.insert(位号，添加元素）
lst.insert(3,'nm')
print(lst)
#替换------------------------把一个列表的某一元素后面换成另一列表元素
lst=[1,2,3,4,5,6,7,8]
a=[90,80,70,60,50]
lst[2:]=a[1:4]
print(lst)


