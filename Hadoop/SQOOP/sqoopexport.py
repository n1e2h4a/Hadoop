import os
import sys
exportcommandsqoop="sqoop export --connect jdbc:mysql://localhost:3306/db1 --username hduser --password hdpwd --table acad --export-dir /user/sqopro/sqop.csv"

os.system(exportcommandsqoop)