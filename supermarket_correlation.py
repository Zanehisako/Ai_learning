import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("/home/yassine/Downloads/archive(1)/Sample - Superstore.csv",encoding='Windows-1252')
#df = df.drop(columns=['Row','Order ID','Order Date','Ship Date'])
#df = df.loc[:'Ship Mode','Segment','Country','City','State','Region','Category','Sales','Quantity','Discount','Profit']
df = df.loc[:,['Sales','Quantity','Discount','Profit']]
correlation_matrix =  df.corr()
print("finished the Correlation matrix")
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
print("finished the drawing the heatmap")
plt.title("Correlation Matrix Heatmap")
plt.show()



