l = [10, 20, 30, 40]
print("Before modification", l)
print("Address of l before modification", id(l))
l[2] = 777
print("After modification", l)
print("Address of l after modification", id(l))
print("Hence list is mutable")


#immutablity
t = (10, 20, 30, 40)
#t[2] = 777 #it gives an error
print(t)

s = "abcdef"
#s[0] = 'x'
print(s)
#in case of string and tuple there is no adding element is available so both the string and tuple are immutable