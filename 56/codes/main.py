import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Function to simulate PMF
def pmf_simulation(data):
    simlen = len(data)
    pmf_values = []

    for i in range(0, 30):  # Adjust the range based on your data
        x = i
        pmf_value = np.count_nonzero(np.array(data) == x) / simlen
        pmf_values.append(pmf_value)

    return pmf_values

# Function to plot and save PMF
def plot_and_save_pmf(values, simulated_pmf, theoretical_pmf, label):
    plt.plot(values, simulated_pmf, marker='o', label='Simulated PMF')
    plt.plot(values, theoretical_pmf, marker='x', label='Theoretical PMF')
    plt.xlabel('Poisson Random Variable ')
    plt.ylabel('PMF')
    plt.title(f'Simulated vs. Theoretical PMF for Lambda={label}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"../figs/fig{label}.png")
    plt.show()

# Lambda values
lambda_values = [1, 2]

for lambd in lambda_values:
    # Simulated data
    simulated_data = np.random.poisson(lam=lambd, size=10000)

    # Theoretical PMF
    values = np.arange(30)
    theoretical_pmf = poisson.pmf(values, mu=lambd)

    # Simulated PMF
    simulated_pmf = pmf_simulation(simulated_data)

    # Plot and save PMF
    plot_and_save_pmf(values, simulated_pmf, theoretical_pmf, lambd)
   
 
