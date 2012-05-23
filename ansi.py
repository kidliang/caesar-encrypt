#License：GPL v3 or higher.
#Copyright (C) 2012 Biergaizi

import sys
times = 0
plain = input("Please input your plain text: ")
value = input("Please input your key(included negatives): ")
secret_list = list(plain)
secret_list_len = len(secret_list)

try:
    value = int(value)
except ValueError:
    print("Please input an integer.")
    sys.exit()

#a的ANSI码是97, z的ANSI码是122。
#A的ANSI码是65, Z的ANSI码是90。

print("")
print("secret: ", end='')

while times < secret_list_len:
    times = times + 1
    #ansi_raw即没有经过任何处理的原始ANSI。
    ansi_raw = ord(secret_list[0 + times - 1])

    #ansi是经过移位加密的ANSI。
    ansi = ansi_raw + int(value)

    #word是用户输入的原始字符。
    word = (secret_list[0 + times - 1])

    #如果ansi_raw小于65或大于90，而且还不是小写字母，那么则说明它根本就不是字母。不加密，直接输出原始内容。
    if (ansi_raw < 65 or ansi_raw > 90) and word.islower() == False:
        print(word, end='')

    #如果ansi_raw小于97或大于122，而且还不是大写字母，那么则说明它根本不是字母。不加密，直接输出原始内容。
    elif (ansi_raw < 97 or ansi_raw > 122) and word.isupper() == False:
        print(word, end='')

    #否则，它就是字母。
    else:
        #如果它是大写字母，而且ANSI码大于90，则说明向后出界。那么通过这个公式回到开头，直到不出界为止。
        while word.isupper() == True and ansi > 90:
            ansi = -26 + ansi

        #如果它是大写字母，而且ANSI码小于65，则说明向前出界。那么通过这个公式回到结尾，直到不出界为止。
        while word.isupper() == True and ansi < 65:
            ansi = 26 + ansi

        #如果它是小写字母，而且ANSI码大于122，则说明向后出界。那么通过这个公式回到开头，直到不出界为止。
        while word.isupper() == False and ansi > 122:
            ansi = -26 + ansi

        #如果它是小写字母，而且ANSI码小于97，则说明向前出界。那么通过这个公式回到结尾，直到不出界为止。
        while word.isupper() == False and ansi < 97:
            ansi = 26 + ansi

        #将处理过的ANSI转换为字符，来输出密文。
        print(chr(ansi), end='')

print("")