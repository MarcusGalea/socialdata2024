#preamble
import os
import pandas as pd
import datetime as dt

#get current working directory
cwd = os.getcwd()
#get parent directory
parent = os.path.dirname(cwd)
#get files directory
files = os.path.join(parent, 'files')
#get police department data as pandas dataframe
police = pd.read_csv(os.path.join(files, 'Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240130.csv'))

#take the data from 2010 to 2017
police['Date'] = pd.to_datetime(police['Date'])
police = police[(police['Date'].dt.year >= 2010) & (police['Date'].dt.year <= 2017)]
police['Hour'] = police['Time'].str.split(':').str[0]