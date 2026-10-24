def getSum(n):
    total = 0
    for j in range (1, n+1):
        total += j
    return total

n = int(input("Heya! Please enter your age: "))

while n <= 0:
    print("Invalid input.")
    print("Please enter a positive whole number greater than 0.")
    n = int(input("Enter age: "))

s = n * (n + 1) // 2
print("Expected sum is", s)

output = getSum(n)

print("After calling the function getSum, the sum of all numbers from 1 to", n, "is: ", output)

if output == s:
    print("Output verified.")

else:
    print("Output not verified.")

