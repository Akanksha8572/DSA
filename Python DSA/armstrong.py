##check if the number is armmstrong
def is_armstrong(n):
    num =n
    total = 0
    nod = len(str(n))
    while num > 0:
        ld = num%10
        total = total + (ld ** nod)
        num = num//10
    return total == n
print(is_armstrong(153))
print(is_armstrong(121))


