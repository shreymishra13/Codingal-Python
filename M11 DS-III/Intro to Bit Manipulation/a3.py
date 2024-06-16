def numberOfBits(n):
  count=0
  while(n):
    count=count+1
    n>>=1
  return count
number=int(input("Enter a number : "))
print("Total no:of bits in ",number,"is ",numberOfBits(number))

print(10 | 15)
print(~ 15)
print(10 & 15)
print(10 << 15)
print(10 >> 15)
print(10 ^ 15)