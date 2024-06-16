A=int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
def check_ifequal(A,B):
  if A^B!=0:
    print("The numbers are not equal")
  else:
    print("The numbers are equal")

check_ifequal(A,B)