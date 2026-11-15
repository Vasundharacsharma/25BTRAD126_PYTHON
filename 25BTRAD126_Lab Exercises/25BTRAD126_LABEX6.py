# Prime number 

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is Not Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is Not Prime Number")
            break
        else:
            print(f"{num} is Prime Number")


# Factorial program 

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i
    
print(f"Factorial of {num} is {factorial}")