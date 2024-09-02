def palindrome_check(text):
    text = text.lower() #convert to lowercase
    text = text.replace(" ", "")#remove spaces
    return text == text[::-1] #check if it the same backward

# Example phrases to check for palindromes:
# "Racecar" -  True
# "A man a plan a canal Panama" -  True
# "Madam In Eden I'm Adam" - True
# "Was it a car or a cat I saw" - True
# "No lemon, no melon" -  True
# "Hello" -  False
# "12321" -  True
# "Able was I ere I saw Elba" -  True
# "Step on no pets" - True
# "Palindrome" -  False

# input string for check
input_palindrome = input("Please enter a string to check if it is a palindrome:")

result_p = palindrome_check(input_palindrome)

#Print results
if result_p:
    print(f"The string '{input_palindrome}' is a palindrome!")
else:
    print(f"The string '{input_palindrome}' is not a palindrome.")

