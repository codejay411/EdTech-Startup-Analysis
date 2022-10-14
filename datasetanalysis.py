# importing packages
import pandas as pd
import pandas_profiling as pp
import os

# forming dataframe and printing
data = pd.read_csv("Startup Company.csv")
# print(data)
  
# forming ProfileReport and save
# as output.html file

profile = pp.ProfileReport(data)
profile.to_file("templates/datasetanalysis.html")