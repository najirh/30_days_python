#### Project 2: Email id Generate

"""
Take the user's first and last name as input.  
Generate a gmail_id for the user by concatenating the first three letters of the   first name and the last three letters of the last name with domain @gmail.com 
Ensure the username is lowercase and has no spaces.  
"""

# taking first name
f_name = input("Please enter first name :").lower().strip()

# Michael
short_f_name = f_name[:2+1]

# taking last name
l_name = input("Please enter last_name :").lower().strip()

# Michael
short_l_name = l_name[-3:]


domain = "@gmail.com"

# generating email
email = short_f_name + short_l_name + domain

# showing the email
print(f"Thank you sharing the info. Your email is \n{email}")
