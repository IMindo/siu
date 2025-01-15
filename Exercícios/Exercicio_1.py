import pandas as pd

# Load the iris dataset from the raw URL
url = 'https://raw.githubusercontent.com/IMindo/siu/refs/heads/main/datasets/iris/iris.csv'
iris = pd.read_csv(url)

# Select the penultimate independent variable
penultimate_variable = iris.iloc[:, -2]

# Find the dimension of the resulting array
dimension = penultimate_variable.shape
dimension