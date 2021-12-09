# reverse_number.py

user_input=int(input("Enter the number to reverse: "))
_rev=0
while(user_input>0):
  dig=user_input%10
  _rev=_rev*10+dig
  user_input=user_input//10
print("The reversed number is :",_rev)



# ----------------------------------------------------------------------------------------------------
#### The script above seeks to reverse the value of a number. In this case, the solution entails:

# 1. Take the integer’s value and store it in a variable.
# 2. Get each digit of the number and store the reversed number in another variable using a while loop.
# 3. Write the number backward.
# 4. Get out of there.
