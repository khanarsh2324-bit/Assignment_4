print("A4.14")
n = int(input("enter a number: "))
reverse = 0 # starting with reverse as 0 because we will be adding digits to it to form the reversed number
while n > 0:
    digit = n % 10 # gives the last digit of the number
    reverse = reverse * 10 + digit # rearranging the digits to form the reversed number
    n = n // 10 # floor division to remove the last digit from the number
print("reversed number:", reverse)
