import numpy as np

def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

# Riemann Sum Calculation
def riemann_sum(n):
    dx = 1 / n  # Step size
    total_sum = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = i * dx
                y = j * dx
                z = k * dx
                total_sum += f(x, y, z) * dx**3

    return total_sum

# Monte Carlo Method
def monte_carlo_integration(num_samples):
    samples_x = np.random.uniform(0, 1, num_samples)
    samples_y = np.random.uniform(0, 1, num_samples)
    samples_z = np.random.uniform(0, 1, num_samples)
    
    values = f(samples_x, samples_y, samples_z)
    integral = np.mean(values) * 1**3  
    return integral

def main():
    n_riemann = 100  
    num_samples_monte_carlo = 100000  
    
    riemann_result = riemann_sum(n_riemann)
    print(f"Riemann Sum Result with n={n_riemann}: {riemann_result}")
    
    monte_carlo_result = monte_carlo_integration(num_samples_monte_carlo)
    print(f"Monte Carlo Method Result with {num_samples_monte_carlo} samples: {monte_carlo_result}")

# Run the script
if __name__ == "__main__":
    main()
