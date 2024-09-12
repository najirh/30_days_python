# Mini project 1
# count word from user's input

"""
-- Input a sentence from the user.  
-- Count the number of words in the sentence  
-- Make sure it doesn't count space
"""



story = input("Please enter story ")

# Deleting all extra leading and trailing space
clean_story = story.strip()

# "   I my name is john i like to writing python code    "

# converted the string into list
store_list = clean_story.split(' ')

# counting the number of word
result = len(store_list)

# displaying the outcome
print(f"The number of count in the store is {result}")



# testing 
#    This day 3 of my 30 days python series. thank you so much for watching the video if you like the content do subscribe to my youtube channel 

