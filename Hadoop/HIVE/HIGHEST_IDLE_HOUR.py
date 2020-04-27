from pyhive import hive
import pandas as pd
import sys
#Establish the connection between hive server and Database
conn = hive.Connection(host="localhost", port=10000, database="newdb", auth="NOSASL")
#load database into hive
query = pd.read_sql('select * from log_data', conn)
#convert the data into the format of datetime
query['log_data.idle_time'] = pd.to_datetime(query['log_data.idle_time'])
#calculate total idle_hours mean
idledata =query[query['log_data.idle_time'] > query['log_data.idle_time'].mean()]
print(idledata)
#print user_name with HIGHEST_IDLE_HOURS
HIGHEST_IDLE_HOURS=idledata['log_data.user_name']
print(HIGHEST_IDLE_HOURS)