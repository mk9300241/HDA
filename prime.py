#Write a Program which has function to find out a number is prime or not
def prime(num):
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


num = int(input("Enter number to check prime:"))
prime(num)
