#prime number
num=int(input("Enter number:"))

if num <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime == True:
        print(f"The number {num} is prime")
    else:
        print(f"The number {num} is not prime")



    
