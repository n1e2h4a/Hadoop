import os
import sys

importcommandsqoop="sqoop import --connect jdbc:mysql://localhost:3306/db1 --username hduser --password hdpwd --table acad --m 1 --target-dir /user/hadoop/data"

os.system(importcommandsqoop)