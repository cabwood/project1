# Exceptions

num1 = 5
num2 = 0

# try:
#     print(num1 / num2)
# except:
#     print("Damn, that didn't work")


# str1 = '123'

# try:
#     num3 = int(str1)
# except ValueError:
#     print("That's not an integer!")
# except TypeError:
#     print("I need a string!")
# else:
#     print(num3 + 10)
# finally:
#     print("I'll always do this")


f = open("LICENS", "r")
try:
    print(f2.readline())
finally:
    print("Always aways always close the file")
    f.close()
