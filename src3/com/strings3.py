s = input("Enter a string: ")

print("Duplicate characters in the string is: ")
for i in range(0, len(s)):
    count = 1
    for j in range(i+1, len(s)):

        if (s[i] == s[j] and s[i] != s[j]):
            count = count + 1
            s = s[:j] + '0' + s[j+1:]
if (count > 1 and s[i] !