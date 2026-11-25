import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data = np.array(data, dtype=np.float64)
    if operation == "flatten":
        return data.ravel()
    if operation == "transpose":
        return data.T
    if operation == "add_batch":
        return np.expand_dims(data, axis=0)
        

