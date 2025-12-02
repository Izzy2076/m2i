a = 2
b = 1

# a = a + 1
# b = b - 1

tmp = a
a = b
b = tmp

# version avec un tuple
a,b = b,a

print(a)
print(b)