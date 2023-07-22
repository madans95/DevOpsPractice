import re

# Function to check the user entered password is meeting the Password criteria.
def check_password_strength(password):
    if(len(password) >= 8):
        if re.search('[A-Z]+', password) and re.search('[a-z]+', password) and re.search('[0-9]+', password) and re.search('[\!\@\#\$\%\^\&\*]+', password):
            #print("Password Criteria is met.")
            return True
        else:
            #print("Password Criteria does not met. Please enter password as mentioned in the Criteria.")
            return False
        
    else:
        #print("Password should contain minimum 8 characters!!!")
        return False


result = False
while not result:
    password = input("Enter Password: ")
    result = check_password_strength(password)
    if(result == False):
        print("Password Criteria does not met. Please Re-enter the Password")

if result == True:
    print("Password Set Successful!")