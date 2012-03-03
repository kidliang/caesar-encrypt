#!/usr/bin/python3
 
#License：GPL v3 or higher.
#Copyright (C) 2011 Biergaizi
 
# '#' 是具体细节的讲解；
# '##'是大算法的讲解。
 
##实际上，这个程序是这样的：
##首先，初始化一个字母表。然后让用户输入一段明文，并将该字符串转换成每个字母为一个对象的列表。
##然后，让用户输入一个密钥，即字母移位的量。接着，通过种种方法来化简这个移位量，比如移动26位实际上是没有移位。
##再然后，将用户的这段明文列表的每一个字母，进行处理，用循环实现。
##这里是循环：得到用户明文列表字母里第n个字母在字母表里的顺序，然后进行移位。即直接加上处理过的移位量。并最后输出。
##这里就基本讲解完了。不过还要处理另一种情况，即列表出界问题，解决的方法是将列表首尾相连，如果向前出界，就跳到最后；
##亦而反之。这也是在while中实现的。另外，如果字符不是一个字母，就会引发异常，那就用try...except...来直接输出原始内容，
##比如一个逗号。还有，大写字母也不再范围中，但需要加密，故还有一大写字母列表尝试。
 
##比尔盖子
##2012/03/01
 
#-----------------------------------------------
times=0
 
#初始化一个字母表
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 
plain=input("Please input your plain text:")
value=input("Please input your key(included negatives):")
 
value=int(value)
 
#将用户输入的内容转换为列表，每个字母都是列表中的一个对象。
secret_list=list(plain)
secret_list_len=len(secret_list)
 
##循环一次就处理一个字母
while times < secret_list_len:
	times=times+1
 
#如果用户输入的移位量大于等于二十六，实际上就是26减去它。
#比如：移位量27，实际上就是1；移位量是26，实际上就是不移位（0）。
	if value>=26:
		value=value-26
	else:
		pass
 
#num实际上就是最终字母的移位量。
	##这分为几步：
	##第一步：取出plain这个列表的第某个对象，times为循环次数。第一次循环就处理第一个字母哦！但由于列表从0开始，因此-1。
	##第二步：alphabet.index用来将用户输入在plain列表的字母，查到alphabet列表对应的位置。
	##第三步：在这个位置上加上value这个用户设置的移位量。最终的变量将是一个已经移动位置的alphabet列表对象顺序。
 
	#这个try...except实际上就是，如果这是一个符号，或者其它非英文小写字母，则直接输出，不加密。
 
	try:
		if plain[times-1].isupper() == True:
			num=int(alphabet_upper.index(plain[times-1])+int(value))
		else:
			num=int(alphabet.index(plain[times-1])+int(value))
		while num>25:
			num=int(num-26)
		while num<-25:
			num=int(num+26)
		if plain[times-1].isupper() == True:
			print(alphabet_upper[num],end='')
		else:
			print(alphabet[num],end='')
	except:
		print(plain[times-1],end='')
 
	#如果列表超出范围（list index out of range），则回到开头。
 
	##最终，将num这个顺序对应的字母输出。
	#由于是循环N次，因此输出会换行。end=''用于不换行。
 
#由于不换行，最后一行看着很难受，故换一行。
print("")
