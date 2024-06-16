def ONSquareTime(n):
  iteration = 0
  for i in range(0,n):
    for j in range(0,n):
      print("*", end="")
      interation += 1
    print("")
    print("\n")
  print("N = ", n, "and total interation= ", interation)
  ONSquareTime(4)
  ONSquareTime(2)
  ONSquareTime(3)
print("\n for every 'n' the time taken equals 'n^2' ")
print("0(n^2)")