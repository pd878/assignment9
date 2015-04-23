import pandas as pd
import sys


class data():

	def __init__(self):
		pass

	def clean_df(self):
		self.df = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', dtype='unicode')
		self.df = self.df[['CAMIS','GRADE','GRADE DATE','BORO']] #drop irrelavent columns
		self.df = self.df.dropna(subset = ['GRADE','GRADE DATE','BORO'])# removes NAN grade rows
		self.df = self.df[self.df['GRADE'].isin(["A", "B", "C"])] #removes invalid grade input
		self.df = self.df[self.df.BORO != 'Missing'] #remove the records with missing borough info

		self.df['GRADE DATE'] = pd.to_datetime(self.df['GRADE DATE'] ) # change the type of column 'GRADE DATE' to datatime
		self.df = self.df.drop_duplicates(['CAMIS','GRADE','GRADE DATE'])
		self.df.loc[:,'GRADE'] = self.df['GRADE'].astype(str) # convert data type
		return self.df

