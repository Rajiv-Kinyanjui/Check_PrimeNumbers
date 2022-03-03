print("Please enter a number")
try:
    num = int(input())
    
    #Prime numbers are divisible by 1 and itself
    #Primes numbers are values greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(False)
                print(i,"times",num//i,"is",num)
                break
        else:
            print(True)
               
except ValueError:
    print("Invalid Input Please enter a number")
