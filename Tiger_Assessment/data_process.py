# This python file has all the necessary functions used
import pandas as pd
import numpy as np


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