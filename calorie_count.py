import numpy as np
import pandas as pd

df = pd.read_csv ('elf_count.csv', skip_blank_lines=False)
empties = np.where(pd.isnull(df))
np.where(df.applymap(lambda x: x == ''))
#print(empties)

pd.set_option('expand_frame_repr', True)
# calling head() method  
# storing in new variable 
data_top = df.head() 
print(df.iloc[14,0])
nulls = df[df['calorie_count'].isnull()].index.tolist()
#for i in nulls:
#   print(df.iloc[i-1,0])


sum = df.iloc[0:14].sum()
print(sum)


#print(nulls)
# display 
#print(data_top)

#print(df.to_string())

