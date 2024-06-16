def is_nth_bit_set(num, n):
  if num & (1 << (n - 1)):
      print("\nSET")
  else:
      print("\nNOT SET")
num = int(input("Enter a number: "))
n = int(input("Enter the bit position: "))
is_nth_bit_set(num, n)

"""
num = 56
n = 5

56 = 00111000
5  = 00000101
if 56 & (1 << 4):
56 & (1 << (5 - 1))
56 & (1 << 4)
56 & 8
56 = 00111000
8  = 00001000
56 & 8 = 00001000 = 8
if 56 & 8:
set
else:
not set
""" 