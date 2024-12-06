# Importing the exp (exponential) function from the math module
from math import exp

# The main function where the program execution starts
def main():
    # Initialize the starting value of x to 0
    x = 0
    
    # Take input for the step size 'h' and convert it to a float
    h = float(input("Input the Value of h: "))
    
    # Initialize the starting value of y to 1
    y = 1
    
    # Initialize variables for approximate value (ap) and lists to store results
    ap = 0
    exact = []  # List to store exact values
    approx = []  # List to store approximate values
    exact_approx = []  # List to store differences (errors) between exact and approximate
    
    # Loop through x values from 0 to just before 1
    while 0 <= x < 1:
        x = round(x, 2)  # Round x to two decimal places for precision
        
        # Compute the function value f(x, y) using the provided f(xn, yn) function
        function = round(f(x, y), 7)  # Round to 7 decimal places
        
        # Compute the new approximate value of y using Euler's method
        y = y + h * function
        
        # Append the approximate value to the list
        approx.append(y)
        
        # Print the current approximate value
        print(y)
        
        # If x is greater than or equal to 0.1, compute the exact value using e(xn)
        if x >= 0.1:
            ap = round(e(x), 7)  # Compute exact value and round to 7 decimal places
            exact.append(ap)  # Append the exact value to the list
        
        # Increment x by the step size h
        x += h
    
    # Print a table header for displaying results
    print(f"     Xn     |      Yn(approx)       |      Yn(exact)      |      Error(e)      ")
    print(f"----------------------------------------------------------------------------------------------------------")
    
    # Loop through the length of both lists to print results in a tabular format
    for i in range(len(approx) and len(exact)):
        # Compute the error (exact - approx) for each step and print the values
        print(f"     x{i + 1}      |      {approx[i]}      |       {exact[i]}       |      {exact[i] - approx[i]} ")
        print(f"----------------------------------------------------------------------------------------------------------")

# Function to calculate the differential equation: dy/dx = 3 * x^2 * y
def f(xn, yn):
    return 3 * (xn ** 2) * yn

# Function to calculate the exact value using the given analytical solution
def e(xn):
    c = xn ** 3  # Compute x^3
    return exp(c)  # Return e^(x^3)

# Call the main function to execute the program
main()
