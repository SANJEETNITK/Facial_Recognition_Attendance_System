import csv
import pandas as pd
import sqlite3

def addData():
	conn = sqlite3.connect('FaceBase.db')
	cmd = cmd = "SELECT * FROM People"
	cursor = conn.execute(cmd)

	name = []
	id = []

	for row in cursor:
		profile = row
		id.append(profile[0])
		name.append(profile[1])

	raw_data = {'Id':id,'Name':name}
	conn.close()
	return raw_data


raw_data = addData()
print(raw_data)
df = pd.DataFrame(raw_data,columns = ['Id','Name'])
df.to_csv('attendance.csv',index=False)

