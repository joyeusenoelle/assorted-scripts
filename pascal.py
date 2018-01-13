import sys

def pascal(n):
  if n < 0:
    print("Row number must be positive.")
    return
  elif n == 0:
    print("1")
    return
  elif n == 1:
    print("1 1")
    return
  m, sum = n, 1
  print(sum, end=" ")
  for k in range(1, n+1):
    sum *= (m/k)
    print(round(sum), end=" ")
    m -= 1
  print()

def main(n = None, s = None):
  if n != None:
    if s == True:
      pascal(n)
    else:
      if n < 0:
        print("Row number must be positive.")
        return
      print("1")
      if n == 0:
        return
      print("1 1")
      if n == 1:
        return
      for i in range(2,n+1):
        pascal(i)

if __name__ == "__main__":
  if len(sys.argv) == 1:
    print("Prints Pascal's Triangle up to the indicated line number.\n\nSyntax:\n  python3 pascal.py target_number [--solo/-s]\n\n  target_number: a positive integer\n  --solo, -s: only print target_number's line of the triangle\n")
    sys.exit(0)
  solo = False
  if len(sys.argv) == 3:
    if sys.argv[2] in ["-s", "--solo"]:
      solo = True
  main(int(sys.argv[1]), solo)
