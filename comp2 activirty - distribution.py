import numpy as np
import matplotlib.pyplot as plt

# Define a function to create a discrete probability distribution
def create_distribution(dist_type):
    if dist_type == 'uniform':
        # Uniform distribution
        x = np.arange(1, 7)
        probabilities = np.full(6, 1/6)
    elif dist_type == 'binomial':
        # Binomial distribution
        x = np.arange(0, 11)
        probabilities = np.array([1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]) / 1024
    elif dist_type == 'poisson':
        # Poisson distribution
        x = np.arange(0, 11)
        probabilities = np.array([0.3679, 0.3679, 0.1839, 0.0613, 0.0153, 0.0031, 0.0005, 0.0001, 0.00002, 0.000003, 0]) 
    else:
        raise ValueError("Invalid distribution type. Choose 'uniform', 'binomial', or 'poisson'.")
    # Plot the distribution
    plt.bar(x, probabilities)
    plt.title(f"{dist_type.capitalize()} Distribution")
    plt.xlabel("X")
    plt.ylabel("P(X)")
    plt.show()

# Ask the user what type of distribution they want
dist_type = input("What type of distribution do you want? (uniform, binomial, or poisson) ")

# Call the function to create the distribution
create_distribution(dist_type)
