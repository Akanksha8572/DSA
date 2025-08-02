from math import * 

def count_digit(num):
    return int(log10(num)+1)

a = count_digit(234567)
print(a , "digit present in you input")
##N = 12345 :: number of digit
N = 12345678
num = N
count = 0
while num>0:
    count += 1
    num = num//10
print(count)

    