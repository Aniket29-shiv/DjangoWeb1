def factorial(number):
    if number==1 or number==0:
        return 1
    else:
        return number * factorial(number - 1)
# def factorialTrailingZero(number):
#     count = 0
#     i = 5
#     while(number//i != 0):
#         count += int(number/i)
#         i = i*5
#     return count

if __name__ == "__main__":
    num = int(input("Enter the number=\n"))
    fac = factorial(num)
    print(f"The factorial is {fac}")
    # print(factorialTrailingZero(num))

