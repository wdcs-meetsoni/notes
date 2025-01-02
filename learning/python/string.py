var = "Meet Soni"
print(var)
print(var[5])
print(var[4])
print(var[1:2])
print(var[:2])
print(var[::-1])
print(var[2:])
print(var[1::2])

s1 = "m" + var[1:]
print(s1)

a = var.replace("Soni", "Meet")
print(a)

var = var[::-1]
print(var)

print(len(var))
print(var.upper())
