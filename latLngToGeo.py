import pandas as pd
import xlrd
from pathlib import Path
import pandas as pd
import os, sys, glob, fnmatch
import numpy as np
from googletrans import Translator
import pygeohash as gh
import os
from openpyxl.writer.excel import ExcelWriter

df = pd.read_excel('POI_locations.xlsx')
# print(df.head())
df['geohash']=df.apply(lambda x: gh.encode(x.lat, x.lng, precision=8), axis=1)
# print(df.head(5))
df.to_csv('POI_locations.csv',index=False)
