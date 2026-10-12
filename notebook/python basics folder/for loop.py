# 1. Defining a reusable function
def check_number(num):
    # Uses control flow and the modulus operator (%) to check for remainders
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 2. Setting up preset variables
numbers_list = [12, 7, 22, 15, 3]
total_sum = 0

# 3. Using a loop to process the data automatically
print("--- Starting Data Analysis ---")

for number in numbers_list:
    # Call the function for each number
    result = check_number(number)
    print(f"Number {number} is {result}")
    
    # Keep track of the total sum
    total_sum = total_sum + number

# 4. Displaying the final output
print("------------------------------")
print("Total Sum of all numbers:", total_sum)
