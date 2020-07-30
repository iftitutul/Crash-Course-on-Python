# This function converts miles to kilometers (km).

# Complete the function to return the result of the conversion
# Call the function to convert the trip distance from miles to kilometers
# Fill in the blank to print the result of the conversion
# Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
   km = miles * 1.6  # approximately 1.6 km in 1 mile
   return km
   
my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
round_trip = my_trip_km*2
print("The round-trip in kilometers is " + str(round_trip))

#Remember to use the str() function to convert numbers into strings when printing them with text, and to call the function with just one parameter, then accept the return value into a new variable.
