def powerOf4(n):
  count = 0
  if (n & (~(n-1)) == n):
    while n>1:
      n >>= 1
      count +=1

    if count%2 == 0:
      return 1
    else:
      return 0

number=int(input("Enter a number : "))

if(powerOf4(number)):
  print("The number is Power of 4")
else:
  print("The number is not Power of 4")
