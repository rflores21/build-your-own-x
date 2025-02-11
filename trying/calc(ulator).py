import numpy as np
import matplotlib.pyplot as plt

# Function to plot a graph
def graphing_calculator():
    # Input: Ask the user for a mathematical function
    function_input = input("Enter a function of x (e.g., x**2, np.sin(x), etc.): ")
    
    # Define the function using lambda
    try:
        function = lambda x: eval(function_input)
    except:
        print("Invalid function. Please try again.")
        return
    
    # Input: Ask for the range of x values
    try:
        x_min = float(input("Enter the minimum x value: "))
        x_max = float(input("Enter the maximum x value: "))
    except:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Generate x values
    x_values = np.linspace(x_min, x_max, 1000)
    
    # Calculate y values
    y_values = function(x_values)
    
    # Plot the graph
    plt.plot(x_values, y_values, label=f"y = {function_input}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graphing Calculator")
    plt.axhline(0, color="black", linewidth=0.5)  # x-axis
    plt.axvline(0, color="black", linewidth=0.5)  # y-axis
    plt.grid(True)
    plt.legend()
    plt.show()

# Run the graphing calculator
graphing_calculator()