def print_diamond(n):
  for i in range(n - 1, -1, -1):
   
    for j in range(i):
      print(" ", end="")

    for j in range(2 * n - 2 * i - 1):
      print("*", end="")
    print()

  for i in range(n):
   
    for j in range(i):
      print(" ", end="")
 
    for j in range(2 * n - 2 * i - 1):
      print("*", end="")
    print()

n = 5
print_diamond(n)
