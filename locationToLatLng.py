import googlemaps
import pandas as pd

def geocode_address(loc):
    gmaps = googlemaps.Client(key='AIzaSyC_YezsLXxNWVt8QgNcMJnNMRcWmPQmHDA')
    geocode_result = gmaps.geocode(loc)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    return lon
    #test - print results
#     print (lat,lon)
# geocode_address('Gp corporate office, Dhaka')

df = pd.read_excel("POI_locations.xlsx")
# print(df['Name'])
name = list(df['Name'])
address = list(df['Address'])
parameter = map(lambda x, y: x + y, name, address)
# print(name)

latList = map(geocode_address, parameter)
df = pd.DataFrame({'col':latList})
pd.set_option("display.max_rows", None, "display.max_columns", None)
print (df.to_string(index=False))