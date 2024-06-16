def OddOccurring(arr):
    res = 0
    for element in arr:
        res = res ^ element

    return res  

arr = [5,6,7,5,6,8,6]                    

print("\n\nOdd occuring number is : ",OddOccurring(arr))