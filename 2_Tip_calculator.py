print("\nWelcome to the Tip Calculator.\n")

bill = float(input("What is the bill?\n$"))

tip_input = input("\nWhat percent would you like to tip?\n")

people = int(input("\nHow many people are splitting the bill?\n"))

#implement function to protect against input of % sign
tip_formatted = ""
for character in tip_input:
    if character.isalnum():
        tip_formatted += character
tip_float = float(tip_formatted)


tipped_amount = bill * (tip_float / 100)
total = bill + tipped_amount
totalpp = total / people

total_str = "{:.2f}".format(total)
totalpp_str = "{:.2f}".format(totalpp)

print(f"\nThe total is ${total_str}.\nEach person should pay ${totalpp_str}.")

#type(variable), print(70 + float("100.5")), round(8/3, 2) [2 decimal places] or round(8/3)
#print(8//3) - floor division, result /= 2, print(f'Your score is {score}'), "{:.2f}" - 
# format to 2 decimal digits even if it is even (ie 25.0 to 25.00)