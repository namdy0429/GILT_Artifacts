import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

df['D'] = np.nan

df['D'] = df.sum()

print(df)
