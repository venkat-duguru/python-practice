#1. String reversal  by slice operator
s = input("Enter some string:")
s1 = s[::-1]
print(s1)

#2.
a = "ABCDEF"
a1 = a[None:None:-1]
print(a1)

#3. by using join method
s = input("Enter a string: ")
S1 = reversed(s)
S2 = ''.join(S1)
print(S2)

#4
string = input("Enter some string in the input: ")
str1 = reversed(string)
str2 = ''.join(str1)
print("The string entered in the input is: ", string)
print("The output of the entered string is: ", str2)

#5string reversal using for loop
def reverse_for_loop(s):
    s1 = ''
    for x in s:
        s1 = x + s1
    return s1


input_string = 'can you return me in this program or not'
print("the reversed of s is :", reverse_for_loop(input_string))

