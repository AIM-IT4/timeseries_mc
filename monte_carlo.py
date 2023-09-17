
import numpy as np
from .utils import preprocess_data

def simulate(data, n_simulations=1000):
    """
    Simulate future paths of a time series using Monte Carlo.
    
    Parameters:
    - data: Time series data as a list or numpy array.
    - n_simulations: Number of simulations to run.
    
    Returns:
    - Simulated paths as a 2D numpy array.
    """
    processed_data = preprocess_data(data)
    mean = np.mean(processed_data)
    std_dev = np.std(processed_data)
    
    simulations = []
    for _ in range(n_simulations):
        simulation = [processed_data[-1]]
        for i in range(len(data) - 1):
            next_val = simulation[-1] + np.random.normal(mean, std_dev)
            simulation.append(next_val)
        simulations.append(simulation)
    
    return np.array(simulations)
