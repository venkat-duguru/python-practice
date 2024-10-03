#1. Type conversion from string to float
a = '100'
d = float(a)
print(type(a))
print(d)
print(type(d))


#2. Type conversion from int to float
b = 90
c = oct(b)
print(type(b))
print(c)
print(type(c))


#3. Type conversion from unicode to int
x = 'A'
y = ord(x)
print(y)
print(type(y))


#4. Type conversion from int to str it gives unicode
y = 100
z = chr(y)
print(type(y))
print(z)
print(type(z))


#5. Type conversion from str to int by using an expression
p = "100 + 20 + 3 - 18"
q = eval(p)
print(q)
print(type(q))
print(type(p))


#6. Type conversion from int to str
r = 150
s = str(r)
print(type(r))
print(s)
print(type(s))


#7. Type conversion from int to str by using represent datatype
t = 120
u = repr(t)
print(u)
print(type(u))
