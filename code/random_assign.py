import pandas as pd
import numpy as np

# you have to download this, it returns 403 if you don't
c = pd.read_html("/home/leo/Desktop/Anexo_Comunas de Chile - Wikipedia, la enciclopedia libre.html")

# it returns a list of dataframes, so
c = pd.DataFrame(c[0])

np.random.seed(42)
c = c.sample(frac=1).reset_index(drop=True)
c['Group'] = (c.index % 10) + 1

for group in range(1, 11):
    nombres = c[c['Group'] == group]['Nombre'].tolist()
    print(f"\nGroup {group}: {nombres}")
