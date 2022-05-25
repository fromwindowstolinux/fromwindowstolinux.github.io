from pyodide.http import open_url
import csv
import random

reader = csv.reader(open_url("https://raw.githubusercontent.com/fromwindowstolinux/Python-Projects/main/Flask%20Project/manga.csv"))
manga = random.choice(list(reader))        
print ("Your manga recommendation is : ", manga[0])