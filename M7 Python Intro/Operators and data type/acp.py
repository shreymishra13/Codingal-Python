x=5
y=9
z=1

def swap(x,y):
    temp=x
    x=y
    y=temp
    


if(x>y):
    temp=x
    x=y
    y=temp
if(x>z):
    temp=x
    x=z
    z=temp
if(y>z):
    temp=y
    y=z
    z=temp
    
print(x)
print(y)
print(z)
    
    
