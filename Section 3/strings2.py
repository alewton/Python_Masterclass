#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)


print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print(parrot[0:9])  #Norwegian
print(parrot[:9])  #Norwegian
print(parrot[0:9:3])  #Nwi

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
