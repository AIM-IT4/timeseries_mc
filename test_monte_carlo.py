
import numpy as np
from timeseries_mc import simulate

def test_simulate():
    # Sample time series data
    data = [1, 2, 3, 4, 5]
    n_simulations = 10
    
    # Call the simulate function
    simulated_paths = simulate(data, n_simulations)
    
    # Check if the output has the correct shape
    assert simulated_paths.shape == (n_simulations, len(data)), f"Expected shape {(n_simulations, len(data))}, but got {simulated_paths.shape}"
