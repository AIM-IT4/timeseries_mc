
import numpy as np

def preprocess_data(data):
    """
    Preprocess time series data for Monte Carlo simulation.
    
    Parameters:
    - data: Time series data as a list or numpy array.
    
    Returns:
    - Preprocessed data as a numpy array.
    """
    return np.diff(data)
