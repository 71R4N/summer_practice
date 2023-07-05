import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(df)
print(df.describe().T)