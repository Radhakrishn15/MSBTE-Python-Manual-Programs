def prime(num):
    if (num==1):
        print(num,"is a not prime number")
    elif (num==2):
          print(num,"is a prime number")
    else:
        for x in range(2, num):
            if(num % x==0):
                print(num,"is a not prime number")
        print(num,"is a prime number")      
num=int(input("Enter number:"  ))   
print(prime(num))

"""Output
Enter number:5
5 is a prime number

[Program finished]