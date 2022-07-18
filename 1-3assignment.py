# write a python program to calculate the length of string.
# name ='simran'
# a= len(name)
# print(a)


# frequency of char.
str1 = input("enter the string")
d1 = dict()
for c in str1:
    if c in d1:
        d1[c] = d1[c]+1
    else:
        d1[c]=1
        print (d1)



# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String





