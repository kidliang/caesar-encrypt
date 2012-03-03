#!/usr/bin/python3
 
#License：GPL v3 or higher.
#Copyright (C) 2012 Biergaizi
 
#实际上，这个程序是这样的：
#首先，初始化一个字母表。然后让用户输入一段明文，并将该字符串转换成每个字符为一个对象的列表。
#然后，让用户输入一个密钥，即字母移位的量。接着，通过种种方法来化简这个移位量，比如移动26位实际上是没有移位。

#再然后，按照顺序处理每一个字母，这使用循环即可轻易实现。
#首先得到用户明文列表字母里第n个字母在字母表里的顺序，然后进行移位。即直接加上处理过的移位量。并最后输出。
#不过，需要判断用户的明文到底是大写字母，还是小写字母，并使用不同的列表alphabet和alphabet_upper来处理输出。
#不过有两种异常需要处理：
#1.如果根本不是字母，则直接输出，不加密。2.列表出界问题，解决的方法是将列表首尾相连，如果向前出界，就跳到最后；亦而反之。
#判断输入的过程都是用多组try...except...实现的。

#最后输出这一个字母的密文，由于是循环，因此将处理并输出完所有的字母，程序才会停止。

#比尔盖子
#2012/03/01

#-----------------------------------------------
times=0
 
#初始化一个字母表
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 
plain=input("Please input your plain text: ")
value=input("Please input your key(included negatives): ")
 
value=int(value)

#将用户输入的内容转换为列表，每个字母都是列表中的一个对象。
secret_list=list(plain)
secret_list_len=len(secret_list)
 
print("")
print("secret: ",end='')

#循环一次就处理一个字母
while times < secret_list_len:
	times=times+1
 
#num实际上就是最终字母的移位量。
    #这分为几步：
    #第一步：取出plain这个列表的第某个对象，times为循环次数。第一次循环就处理第一个字母哦！但由于列表从0开始，因此-1。
    #第二步：alphabet.index用来将用户输入在plain列表的字母，查到alphabet列表对应的位置。
    #第三步：在这个位置上加上value这个用户设置的移位量。最终的变量将是一个已经移动位置的alphabet列表对象顺序。
 
    #这个try...except实际上就是：
	try:
	#如果这个try完全正常，则说明这是一个小写字母(能在alphabet中找到该字母)，同时不存在列表超出范围(list index out of range)的问题。那么，将密文保存到output。
		num=int(alphabet.index(plain[times-1])+int(value))
		output=alphabet[num]
	except ValueError:
	#如果发生了ValueError，则说明这不是一个小写字母(不能在alphabet中找到该字母)。
		try:
		#如果这个try完全正常，则说明这是一个大写字母(能在alphabet_upper中找到该字母)，同时不存在列表超出范围的问题。那么，将密文保存到output。
			num=int(alphabet_upper.index(plain[times-1])+int(value))
			output=alphabet_upper[num]
		except IndexError:
		#如果发生了IndexError，则说明这是一个大写字母，但是列表超出范围。那么，如果列表是向前超出范围的，将回到后面；亦而反之。这是通过修改num实现的。修正之后，将密文保存到output。
			if num>25:
				num=int(num%26)
			if num<-25:
				num=int(-(-num%26))
			output=alphabet_upper[num]
		except ValueError:
		#如果发生了ValueError，则说明这不是一个英文字母(无论是alphabet或alphabet_upper都不存在该字母)。那么，这个字符将不会被加密，直接保存到output。
			output=plain[times-1]
	except IndexError:
	#如果发生了IndexError，则说明这是一个小写字母，但是列表超出范围。那么，如果列表是向前超出范围的，将回到后面；亦而反之。这是通过修改num实现的。修正之后，将密文保存到output。
		if num>25:
			num=int(num%26)
		if num<-25:
			num=int(-(-num%26))
		output=alphabet[num]
 
    #最终，将保存在output中的密文输出。
	print(output,end='')
    #由于是循环输出，每次都会换行，将导致输出的密文难以阅读。因此用end=''选项不换行。
 
#由于不换行，最后一行看着很难受，故换一行。
print("")
