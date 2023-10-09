#1. Перемножить все не чётные значения в диапазоне от 9173 до 9435;
# result = 1
# for i in range(9173, 9435):
#     if i % 2 != 0:
#         result *= i
#
# print(result)

#2*. Print the following pattern
#    5 4 3 2 1
#    4 3 2 1
#    3 2 1
#    2 1
#    1

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

#3. Display numbers from -10 to -1 using for loop
# for i in range(-10, 0):
#     print(i, end=" ")
# print()

# 4. Calculate the cube of all numbers from 1 to a given number from user
# number = int(input("Please input some number: "))
# for i in range(1, number+1):
#     print(f"Cube for {i} equal to {i**3}")


#5. Find the factorial of a given number
number = int(input("Please input some number: "))
factorial = 1
for i in range(1, number+1):
    factorial *= i

print(F"Factorial of {number} is: {factorial}")

