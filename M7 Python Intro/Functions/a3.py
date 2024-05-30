def addition(num1,num2):
  return num1+num2
def subtraction(num1,num2):
  return num1-num2
def product(d,e):
  return d*e
def div(g,h):
  return g//h

x=int(input("enter the first number  "))
y=int(input("enter the second number  "))

print("Sum is", addition(x,y)) 
print("Subtraction is",subtraction(x,y))  
print("Product is ", product(x,y))
print("Quotient is ", div(x,y)) 
