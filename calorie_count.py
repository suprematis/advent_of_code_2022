import numpy as np
import pandas as pd

df = pd.read_csv ('elf_count.csv', skip_blank_lines=False)
empties = np.where(pd.isnull(df))
np.where(df.applymap(lambda x: x == ''))
print(empties)

pd.set_option('expand_frame_repr', True)
# calling head() method  
# storing in new variable 
data_top = df.head() 
print(df.iloc[2221,0])

# display 
#print(data_top)

#print(df.to_string())

