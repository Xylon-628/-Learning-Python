#转义字符:反斜杠+想要转义功能的首字母  通过转义字符可实现文字的整理
# \n (newline）， \r (return)， \b (backspace)， \t (tab)
print('1hello''new','new')
print('2hello\nworld') #换行
print('3hello\tworld')
print('4hello\rworld') #覆盖前面所有字符
print('5hello\b\b\bworld') #删除n(\b)个字符
print(12345678,'\t123456')
# print(A\tB)--让B在4n或4n+1个位置上
print(1234567890)
print('1\tworld')
print('12\tworld')
print('123\tworld')
print('1234\tworld')
print('12345\tworld')
#\+符号
print('http\\\\www.baidu.com')  #\\=\
print('12345\\t123')
print('The teacher said, \'Good morning.\'')  #\'--使英语单引号成为字符
# 原字符  在前面加r或R 注：依然不能在最后加\
print(r'hello\nworld')
print('hello\\nworld')
print('a\b')

print('\n' + '\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]) + '\n')
print(
    '\n' + '\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]) + '\n')