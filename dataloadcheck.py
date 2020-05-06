import pandas as pd
import datetime as dt

def conname(samp_df):
    samp_df['NAME'] = samp_df['SURNAME'] + ' ' + samp_df['FIRST_NAME']
    return samp_df

def agecal(samp_df):
    current_year = int(dt.datetime.now().year)
    samp_df['CURRENTYEAR'] = current_year
    samp_df['AGE'] = samp_df['CURRENTYEAR'] - samp_df['YEAR_OF_BIRTH']
    return samp_df

def  titcase(samp_df):
    samp_df["NAME"] = samp_df["NAME"].str.title()
    samp_df["NATIONALITY"] = samp_df["NATIONALITY"].str.title()
    samp_df["RELIGION"] = samp_df["RELIGION"].str.title()
    return samp_df

def outfile(samp_df):
    samp_df = samp_df[['NAME', 'AGE', 'EMAIL', 'NATIONALITY', 'RELIGION']]
    print("THE FINAL OUTPUT DATA \n ", samp_df)
    samp_df.to_csv("c:\\Users\\PycharmProjects\\output.csv")
    print("the output file has been generated")


def main():
    samp = pd.read_csv('c:\\Users\\PycharmProjects\\data.csv')
    samp_df = pd.DataFrame(samp)
    conname(samp_df)
    agecal(samp_df)
    titcase(samp_df)
    outfile(samp_df)

if __name__ == '__main__':
    main()

