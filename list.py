#!/usr/bin/python3

#凯撒加密算法实现。
#License：GPL v3 or higher.
#Copyright (C) 2012 Biergaizi

#初始化小、大字母表
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', \
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', \
        'x', 'y', 'z')
alphabet_upper = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',\
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', \
        'Y', 'Z')

#要求用户输入明文和密钥。
plain = input("Please input your plain text: ")
value = input("Please input your key(included negatives): ")

#防止用户输入非数字。
try:
    value = int(value)
except ValueError:
    print("Please input an integer.")
    exit()

#使用for循环来遍历plain，一次处理一个明文字符letter。
for letter in plain:
    #如果当前字符为大写字母……
    if letter.isupper() == True:
        #查出letter在大写字母表中的位置，加上用户的密钥，并取除以26的余数，得出实际的移位。
        output = alphabet_upper[(alphabet_upper.index(letter) + value) % 26]
    #如果当前字符为小写字母……
    elif letter.islower() == True:
        #查出letter在小写字母表中的位置，加上用户的密钥，并取除以26的余数，得出实际的移位。
        output = alphabet[(alphabet.index(letter) + value) % 26]
    #否则当前字符不是英文字母，直接返回原字符。
    else:
        output = letter
    #输出结果，由于是循环输出，每次都会换行，将导致输出的密文难以阅读。因此用end=''选项不换行。
    print(output, end='')
#由于不换行，最后一行看着很难受，故换一行。
print("")