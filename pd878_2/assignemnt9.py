import pandas as pd
import sys
import matplotlib.pyplot as plt
from functions import *
from load_data import *

# reload(sys)
# sys.setdefaultencoding("unicode") 

clean_df = data().clean_df()


if __name__ == "__main__":

	boros = list(clean_df['BORO'].unique())  
	for boro in boros:
	    df_boro = clean_df[clean_df.BORO == boro]
	    CAMIS_list=list(df_boro['CAMIS'].unique())
	    result = get_improvement(CAMIS_list, clean_df)
	    print "The overall improvement score of the restaurants in %s is %s. " %(boro, result)
	    filename = 'grade_improvement_%s.pdf' %boro.lower()
	    draw_graph(df_boro, filename)

	filename = 'grade_improvement_nyc.pdf' 
	draw_graph(clean_df, filename)

