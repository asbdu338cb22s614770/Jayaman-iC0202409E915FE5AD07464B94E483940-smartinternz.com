def fact(n):
  return 1 if (n==1 or n==0) else n* fact(n-1);
num=int(input("Enter a no:"))
print("factorial of",num,"is",fact(num))