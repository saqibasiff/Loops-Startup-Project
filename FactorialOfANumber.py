# 5! = 1 X 2 X 3 X 4 X 5

n = int(input("Please Enter Your Number For Factorial : "))
product = 1
for i in range (1, n+1):
    product = product * i
    print(f"The Factorial of {n} Is {product}")

