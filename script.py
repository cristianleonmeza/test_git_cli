print("Hello from Python")

import numpy as np
import pandas as pd

# Create a NumPy array
arr = np.array([1, 2, 3, 4])

# Create a DataFrame
df = pd.DataFrame({
    "numbers": arr,
    "squared": arr**2
})

print(df)