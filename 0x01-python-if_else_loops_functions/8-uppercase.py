#!/usr/bin/python3

def uppercase(str):
    
    for each_char in str:
        each_char_num = ord(each_char)
        
        if each_char_num > 96 and each_char_num < 123:
            each_char_num -=32

        str_char = chr(each_char_num)
        print('{}'.format(str_char), end='')
    
    print('')
