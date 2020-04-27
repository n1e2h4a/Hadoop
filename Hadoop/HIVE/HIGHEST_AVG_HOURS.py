from pyhive import hive
import pandas as pd
import sys
#Establish the connection between hive server and Database
conn = hive.Connection(host="localhost", port=10000, database="newdb", auth="NOSASL")
#load database into hive
query= pd.read_sql('select * from log_data', conn)
#convert the data into the format of datetime
query['log_data.working_hours'] = pd.to_datetime(query['log_data.working_hours'])
#calculate the mean of total working_hours
averagehours = query[query['log_data.working_hours'] > query['log_data.working_hours'].mean()]
print(averagehours)
#print the user_name with highest average hours
highest_avg_hours =averagehours['log_data.user_name']
print(highest_avg_hours)