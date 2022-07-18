# function which return reverse of a string

# def isPalindrome(s):
# 	return s == s[::-1]

# s = "madam"
# s = isPalindrome(s)
# if s:
# 	print("Yes")
# else:
# 	print("No")




# s = "madam"
# s1 = s[::-1]
# print (s1)
#     if s==s1:
#         print ("yes")
#     else:
#         print("no")



num = int (input("enter the value"))
temp = num
rev = 0
while (num>0):
    dig = num%10
    rev = rev * 10+dig
    num = num//10
    if (temp == rev):
        print("the value is palindrome")
    else: 
            print ("the value is not palindrome")