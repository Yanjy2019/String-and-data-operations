#2019-12-04

#反斜杠的使用规则：表示续行的作用
print('''社会主义是就是好\
社会核心价值观\
好好学习天天向上\  
我是好人''',end="\n")

#转义字符的使用规则
print("社会就是好\n")                #换行操作
print("我是燕江依\\n")               #两个\\操作会识别后面的操作，不是转义字符
print("abcdefghjijk"[1:5:2])         #字符串的切片操作
print("社会主义现代化核心价值观"[::-2])  #其中第三个参数控制的是截取字符串的步长和方向

#字符串常见的方法操作
a="+++Python is a excellent language+++"
b="社会主义现代化强国！，我会好好努力的，一定会的"
print(a.lower())   #输出字符串的小写方法操作
print(b.lower())
print(a.upper())        #输出字符串的大写方法操作
print(b.upper())
print(a.split("e"))     #将字符串以e字符进行分割，不包含分割字符e，然后以列表的形式输出分割后的各个字符串
print(b.split("会"))
print(a.count("e"))     #输出字符串里面字符e的个数统计
print(b.count("会"))
print(a.replace("e","a"))  #交换方法：replace（old，new）：j将旧的内代替为新的内容
print(b.replace("会","一定"))
print(a.center(50,"#"))   #居中方法，其中居中以外的地方将补为#,两边填充相同的位数
print(b.center(50))       #如果忘了第二个需要写的参数，即需要填充的符号，则默认填充为空格
print(a.strip("+"))       #去掉原来字符串里面左侧和右侧的符号“+”字符串
print(b.strip("社"))
print(a.join("bcd"))     #将原来iter中个每个变量值间增加一个a字符串，当括号里面iter=bcd时，即输出结果为为：b(a)c(a)d，主体含义是将a加入到iter中去

#字符串的格式化操作：主要是format函数的规定和操作
print("孔子说:{},我的岁数现在为{}".format("逝者如斯夫，不舍昼夜！",30))
s="python语言"
print("{0:*<25}python语言".format("考试安排"))  #居中对齐/左对齐和右对齐方式,25表示的是总共的位数规定
print("{:,}".format(1234567890))      #输出三位划分好的数据表示方法
print("{:.2f}".format(1234.45656))  #输出浮点型数据两位小数时的数据表示
print("{:.5}".format("python是最火的人工智能编程语言"))  #输出字符串的前几位数
print("{0:b},{0:d},{0:o},{0:x},{0:c}".format(435))               #输出整数型数据的二进制、十进制、十六进制以及c形式ASCII码的字符输出(所有的字符输出都是将其字符规定为数字，然后转化为二进制数据来进行识别)
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))                    #输出标准形式下面的各个浮点型数据的形式：标准形式输出为6位小数
print("{0:.3e},{0:.2E},{0:.2f},{0:.2%}".format(3.14))             #规定浮点型数据输出的小数位数

#字符串之间的相关操作符
print(a+b)  #字符串之间的合并和拼接
print(3*a)  #复制n次a字符串的内容
print("exca" in a)    #判断子字符串是否包含在原来的字符串里面
#字符串的各个常见的处理函数
c=1+2j
print(len(a))
print(len(b))
print(str(c))         #将变量c以字符串的形式输出，即将数据的类型转换为字符串类型
print(type(str(c)))
print(chr(97))        #打印出Unicode码s数字值所对对应的单字符串内容
print(ord("a"))       #输出Unicode字符串码a所对应的数字值
print(type(hex(97)))  #返回整数x对应的十六进制的小写形式字符串
print(oct(97))        #返回整数x对应的八进制的小写形式字符串
print(bin(2000))      #返回整数x所对应的二进制的小写形式的字符串

#数字类型的转换
print(int(1.24346575))
print(type(int(3.1415926)))
print(float(3))
print(type(float(3.1414567867)))
print(type(str(3.1415926)))
x="3.1415926"
print(float(x))
print(type(float(x)))






















