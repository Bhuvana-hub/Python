import pandas as pd
import datetime as dt

#Getting assigning the current year
current_year=int(dt.datetime.now().year)

## reading file from CSV sheet and mapping it to Dataframe
samp=pd.read_csv('c:\\Users\\b.nedumaran\\PycharmProjects\\data.csv')
samp_df=pd.DataFrame(samp)

## concatenating the 2 columns in the excel sheet to one column
samp_df['NAME']=samp_df['SURNAME']+' ' + samp['FIRST_NAME']

##addding new column to get current year
samp_df['CURRENTYEAR']=current_year

##now trying to get current age using year of birth and current year value
samp_df['AGE']=samp_df['CURRENTYEAR']-samp_df['YEAR_OF_BIRTH']

## Getting only selected column
##samp_df=samp_df[['NAME','YEAR_OF_BIRTH','EMAIL','RELIGION','CURRENTYEAR','AGE']]

## Converting the few column values to title case
samp_df["NAME"]=samp_df["NAME"].str.title()
samp_df["NATIONALITY"]=samp_df["NATIONALITY"].str.title()
samp_df["RELIGION"]=samp_df["RELIGION"].str.title()

## Getting only final specified columns
samp_df=samp_df[['NAME','AGE','EMAIL','NATIONALITY','RELIGION']]

print("THE FINAL OUTPUT DATA \n ", samp_df)

## Sending the output to excel sheet
samp_df.to_csv("c:\\Users\\b.nedumaran\\PycharmProjects\\output.csv")

print("the output file has been generated")
