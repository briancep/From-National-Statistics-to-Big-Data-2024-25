#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:43:42 2023

@author: briancepparulo
"""
#import relevant libraries
import pandas as pd
import numpy as np
import os
import eurostat

print(os.getcwd())
os.chdir('/Users/briancepparulo/Library/CloudStorage/OneDrive-GoldsmithsCollege/GOLDSMITH/From National Statistics to Big data/2023-2024/Python/py')

toc_df=eurostat.get_toc_df() #create a df with info on all eurostata dataset
print(toc_df.head()) #print first five rows of df

f=eurostat.subset_toc_df(toc_df, 'gdp') #create a subset of the previously created df with datasets including 'gdp' in their name

code='namq_10_gdp' #assign to the object code a string with dataset code
pars=eurostat.get_pars(code) #get a list of datset parameters
pars
par_item=eurostat.get_par_values(code, 'na_item') #get values from parameter 'na_item'
par_item
par_geo = eurostat.get_par_values(code, 'geo')
par_geo
par_unit=eurostat.get_par_values(code,'unit')
par_unit

### set filters for dowload
my_filter_pars={'s_adj':['SCA'], 'unit':['CLV10_MNAC'], \
                  'na_item':['B1GQ','P31_S14_S15','P3_S13', 'P51G', 'P52_P53', 'P6', 'P7']} 
    
df_gdp=eurostat.get_data_df(code, filter_pars=my_filter_pars) #dowload gdp and components database



  