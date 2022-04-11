#! /usr/bin/python

first = input('enter the first number ')
second = input('enter the second number ')
third = input('enter the third number ')
fourth = input('enter the fourth number ')
fifth = input('enter the fifth number ')

try:
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)
    fifth = int(fifth)
    r_equal = 'duplicates'
    r_unique = 'all unique'
    
    if first == second or first ==  third or first == fourth or first ==  fifth:
        print(r_equal)
    elif second == third or second == fourth or second == fifth :
        print(r_equal)
    elif third == fourth or third == fifth :
        print(r_equal)
    elif fourth == fifth:
        print(r_equal)
    else:
        print(r_unique)
except:
    print('please input only integer values')