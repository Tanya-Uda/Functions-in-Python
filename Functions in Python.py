def greaterThan(x, y):
    # Check if x is greater than y
    if x > y:
        return True
    else:
        return False

# Main part of the program
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Call the greaterThan function and store the result
result = greaterThan(a, b)

# Print the result in the required format
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

