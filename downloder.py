# %%
import requests
from zipfile import ZipFile
import datetime as dt
import os

# %%
'''
holidaylist = ['25-12-2023','27-11-2023','14-11-2023',
               '24-10-2023','02-10-2023','19-09-2023',
               '15-08-2023','28-06-2023','22-04-2023',
               '01-05-2023','14-04-2023','07-04-2023',
               '04-04-2023','30-03-2023','07-03-2023','26-01-2023',]
'''

# %%
#print(len(holidaylist))

# %%
ct = dt.datetime.today()
day= ct.strftime("%d") 
day=str(int(day)-2) #today is sunday
month= ct.strftime("%b").upper()
year= ct.strftime("%Y")
day,month,year
file_name = f"C:\\Users\\Ryzen\\python\\StockTracker\\bhavcopy\\downloads\\cm{day}{month}{year}bhav.csv.zip"

# %%
'''
year = 2023 # YYYY format
month= 'MAY' # MMM format
day= 19 # DD format
'''

# %%
url= f'https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{day}{month}{year}bhav.csv.zip'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)


# %%
def downloadfile():
    file_name = f'C:\\Users\\Ryzen\\python\\StockTracker\\bhavcopy\\downloads\\cm{day}{month}{year}bhav.csv.zip'
    r = requests.get(url,headers=headers,stream=True)
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

# %%
def unzipfile():
    file=f'C:\\Users\\Ryzen\python\\StockTracker\\bhavcopy\\downloads\\cm{day}{month}{year}bhav.csv.zip'
    handle=ZipFile(file)
    handle.extractall('C:\\Users\\Ryzen\\python\\StockTracker\\bhavcopy\\downloads')
    handle.close()


# %%
def deletezipfile():
    file = f"cm{day}{month}{year}bhav.csv.zip"  
    location = "C:/Users/Ryzen/python/StockTracker/bhavcopy/downloads"
    path = os.path.join(location, file)  
    print(path)
    os.remove(path)

# %%
if __name__ == "__main__":
    downloadfile()
    unzipfile()
    deletezipfile()


# %%



