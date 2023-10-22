import requests
import pandas as pd
import json

# Base url for Chicago Open Data Portal crime API; plus addin of date and location filters
baseurl = "https://data.cityofchicago.org/resource/w98m-zvie.json"

datebetw = "?$where=date between '2019-01-01T12:00:00' and '2019-07-16T14:00:00'"

# syntax for below filter is  'within_box(location_col, NW_lat, NW_long, SE_lat, SE_long)' I have updated my location and Chinatown
boxurl = 'within_box(location, 41.840340, -87.613701, 40.714458, -73.999588)'

# Create the overall URL to interogate API with our data and location filters
ourl = baseurl + datebetw + ' AND ' + boxurl

text =  requests.get(ourl).json()  
 
# create pandas dataframe dictionary container object 
df = pd.DataFrame(
    text, columns=['date', 'block', 'primary_type', 'description'])

print(df.head())
print(df.head(n=100))
print(df) # full set

print(df['date'])
print(df.columns[0][:])

print(df.describe()) # possible stats

