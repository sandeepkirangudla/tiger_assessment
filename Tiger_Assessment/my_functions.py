# This python file has all the necessary functions used
import pandas as pd
import numpy as np
import os

class DataProcess:
    """
    This class has all the data cleaning functions required to
    """
    def __init__(self,df):
        return

    def check_null(df):
        """
        This functions takes a Data Frame as input and checks if the variables have any null values.
        It returns a Data Frame with column names and corresponding True/False if it has any nulls.
        """
        colname=df.columns
        na_array = []
        for i in colname:
            # appends column name to temporary array
            na_array.append(str(i))
            # appends True/False after checking if it has any nulls
            na_array.append(df[i].isnull().values.any())
        res = pd.DataFrame(np.reshape(na_array, (-1,2)), columns = ['Column Names', 'Has Nulls'])
        return res


    def capital(df):
        """
        This function takes data frame and capitalises every word of object columns and returns a data frame.
        """
        df_obj = df.select_dtypes(include=['object'])
        for i in df_obj.columns:
            df[i] = df[i].str.title()
        return df


    def remove_nl_tab(df):
        """
        This function takes data frame and removes new lines and tabs and returns a data frame.
        """
        df = df.replace(regex=['\n', '\t'], value='')
        return df


    def trim(df):
        """
        Trims whitespace from begining and end of each value across all non-numeric columns in a dataframe
        """
        df_obj = df.select_dtypes(['object'])
        df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
        return df


def clean(covid_df, pop_df):
    """
    This function cleans data frame and returns data frames.
    """
    covid_df = covid_df
    pop_df = pop_df

    # Maps to the correct column names
    pop_df_col_map = {'STATE': 'State_ID', 'COUNTY': 'County_ID', 'POPESTIMATE2019': 'Population'}
    pop_df.columns = [pop_df_col_map.get(x, "No_key") for x in pop_df.columns]

    covid_df_col_map = {'date': 'Date', 'county': 'County', 'state': 'State', 'CTYNAME': 'County',
                        'fips': 'FIPS', 'cases': 'Cases', 'deaths': 'Deaths'}
    covid_df.columns = [covid_df_col_map.get(x, "No_key") for x in covid_df.columns]

    # Combining State FIPS ID and County FIPS ID to 1 column and adding leading zeros
    pop_df['State_ID'] = pop_df['State_ID'].map('{:0>2}'.format)
    pop_df['County_ID'] = pop_df['County_ID'].map('{:0>3}'.format)
    pop_df['FIPS'] = pop_df['State_ID'] + pop_df['County_ID']
    pop_df = pop_df.drop(['State_ID', 'County_ID'], axis=1)
    covid_df['FIPS'] = covid_df['FIPS'].fillna(0).astype(int)
    covid_df['FIPS'] = covid_df['FIPS'].map('{:0>5}'.format)

    # standardizing the date column
    covid_df['Date'] = pd.to_datetime(covid_df['Date'], format='%Y-%m-%d')

    # sorting covid_df by Date for better understanding
    covid_df = covid_df.sort_values(by='Date', ascending=True, ignore_index=True)

    return (covid_df, pop_df)


# This class has the necessary functions to generate summary statistics
class SummaryStats:
    """
    This class gives basic summary statistics
    """

    def freq(df):
        """
        This function gives frequency table of the dataframe and prints the frequency table.
        """
        df = df.select_dtypes(include=['object'])
        col = df.columns
        for i in col:
            print(pd.crosstab(index=df[i], columns='count').sort_values(by='count', ascending=False), '\n')

    def summarize(df, path):
        """
        This function give final cumulative summary table of the dataframe and outputs to a specified path.
        """
        df['Cumulative Cases'] = df.groupby(by=['FIPS'])['Daily Cases'].transform(lambda x: x.cumsum())
        df['Cumulative Deaths'] = df.groupby(by=['FIPS'])['Daily Deaths'].transform(lambda x: x.cumsum())
        df = df[['Date', 'County', 'State', 'FIPS', 'Population', 'Daily Cases', 'Daily Deaths',
                 'Cumulative Cases', 'Cumulative Deaths']]
        df.to_csv(path + '\summary.csv', index=False)


def output_path(path):
    """`
    This function takes input path and checks if file exist.
    """
    a = True
    while a == True:
        path = input(path)
        if os.path.isdir(path):
            a = False
            return path
        else:
            print('Please enter a valid input path')

def final_merge(covid_df, pop_df):
    covid_df = covid_df
    pop_df = pop_df
    final = pd.merge(covid_df, pop_df, on=['FIPS'], how='left')
    final['Population'] = final['Population'].fillna(0).astype(int)
    final.columns = ['Date', 'County', 'State', 'FIPS', 'Daily Cases', 'Daily Deaths', 'Population']
    final = final.sort_values(by=['Date', 'State', 'County'], ascending=[True, True, True])
    return final