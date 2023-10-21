import pandas as pd
from sklearn import datasets
df = datasets.load_breast_cancer()
print(df.info())