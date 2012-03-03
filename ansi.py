#!/usr/bin/python3
 
#License：GPL v3 or higher.
#Copyright (C) 2011 Biergaizi
 
times=0
plain=input("Please input your plain text:")
value=input("Please input your key(included negatives):")
secret_list=list(plain)
secret_list_len=len(secret_list)
 
# 'a' = 97, 'z'=122
# 'A' = 65, 'Z'=90
while times < secret_list_len:
	times=times+1
	ansi_raw=ord(secret_list[0+times-1])
	ansi=ansi_raw+int(value)
	word=(secret_list[0+times-1])
 
	if (ansi_raw <65 or ansi_raw > 90) and word.isupper() == True:
		print(word,end='')
	elif (ansi_raw <97 or ansi_raw >122) and word.isupper() == False:
		print(word,end='')
	else:
		while word.isupper() == True and ansi > 90:
			ansi = ansi - 90 + 65 -1
		while word.isupper() == True and ansi < 65:
			ansi = 90-(65-ansi)+1
		while word.isupper() == False and ansi > 122:
			ansi = ansi - 122 + 97 -1
		while word.isupper() == False and ansi < 97:
			ansi = 122-(97-ansi)+1
		print(chr(ansi),end='')

print("")
