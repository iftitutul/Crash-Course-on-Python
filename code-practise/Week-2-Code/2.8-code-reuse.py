# Ready to try it yourself? See if you can reduce the code duplication in this script.

# In this code, identify the repeated pattern and replace it with a function called month_days, that receives the name of the month and the number of days in that month as parameters. Adapt the rest of the code so that the result is the same. Confirm your results by making a function call with the correct parameters for both months listed.

'''
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")
'''

def month_days(month, day):
   print(month + " has " + str(day) + " days.")

month_days("June", 30)
month_days("July", 31)
