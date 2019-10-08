import pandas as pd
from pandas import DataFrame
from datetime import date

df = pd.read_csv('attendance.csv')
today = ""+str(date.today())
date = {'date':['24/07/2016','25/07/2016']}
date = pd.DataFrame(date)

df = pd.concat([df,date],axis=1)

df.to_csv('attendance.csv',index=False)

