def power2(num):
  if (num == 0):
    return 0
  if (num&(~(num - 1)) == num):
    return 1
  return 0
num = int(input("enter a number"))
if (power2(num)):
  print("\nthe number is power of 2")
else:
  print("\nthe number is not power of 2")