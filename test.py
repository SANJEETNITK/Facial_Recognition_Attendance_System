import pandas as pd
from pandas import DataFrame
from datetime import date

# df = pd.read_csv('attendance.csv')
# today = ""+str(date.today())

raw_data = {'date':['abc','def'],'val':[1,2]}
print(raw_data)

df = pd.DataFrame(raw_data)
df.to_csv('test.csv',index=False)


# date = pd.DataFrame(raw_data,columns = ["abc"])
# date.to_csv('test.csv')

# df = pd.concat([df,date],axis=1)

# df.to_csv('attendance.csv',index=False)

