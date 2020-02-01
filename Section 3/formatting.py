for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

##      {index:field width, <>^left, right, center}

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))         # six digits after decimal
print("Pi is approximately {0:12.50f}".format(22 / 7))      # 50 digits of precision
print("Pi is approximately {0:52.50f}".format(22 / 7))      # different field widths
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
