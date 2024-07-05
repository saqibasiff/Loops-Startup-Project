n = int(input("Please Enter Your Number To Check : "))

for i in range(2, n):
    if n%i == 0:
        print("Number Is Not Prime")
        break
else:
    print("Your Number Is Prime.")
