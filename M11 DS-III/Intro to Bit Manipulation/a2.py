
num = int(input("Enter a number: "))

def isEvenOdd(n):
    if n^1 == n+1:
        return True
    else:
        if isEvenOdd(num):
            pass

if isEvenOdd(num):
    print(num, "is even")
else:
    print(num, "is odd")
    