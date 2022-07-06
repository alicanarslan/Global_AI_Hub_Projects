import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

netflix = pd.read_csv(r'C:\Users\dtblackk\Desktop\project\netflix.csv', encoding='ISO-8859-1')
netflix_df =  pd.DataFrame(netflix)
x = netflix_df.sort_values(by ="IMDB Score", ascending=False)
x.head(10)[["Title", "IMDB Score"]].to_excel(r"C:\Users\dtblackk\Desktop\excels\top10imbd.xlsx", index=False, encoding='ISO-8859-1')
