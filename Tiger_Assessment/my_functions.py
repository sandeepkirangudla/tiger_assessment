# This python file has all the necessary functions used
import pandas as pd
import numpy as np
import os
# from zipfile import ZipFile
import json
import seaborn as sns
# import matplotlib.pyplot as plt

# This class has all the necessary function used for clean the dataset
class data_process:
    """
    This class has all the data cleaning functions
    """
    
    def __init__(self,df):
        self.df = df
        
    def check_null(df):
        """
        This funtions takes a Data Frame as input and checks if the variables have any null values.
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
        This function takes data frame and captializes every word of object columns and returns a data frame.
        """
        df_obj = df.select_dtypes(include=['object'])
        for i in df_obj.columns:
            df[i] = df[i].str.title()
        return df
    
    def drop_dup(df):
        """
        This function takes data frame and drop duplicate records and returns a data frame.
        """
        df = df.drop_duplicates()
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

# This class has the necessary functions to generate summary statistics
class summary_stats:
    """
    This class gives basic summary statistics
    """
    def freq(df):
        """
        This function gives frequency table of the dataframea and prints the frequency table.
        """
        df = df.select_dtypes(include=['object'])
        col = df.columns
        for i in col:
            print(pd.crosstab(index=df[i], columns='count').sort_values(by='count', ascending=False),'\n')
    
    def summarize(df, path): 
        """
        This function give final summary table of the dataframe and outputs to a specified path.
        """
        final_summary = pd.crosstab(index=[df['Stratum'], df['Habitat'], 
                                           df['Family'], df['Genus'], 
                                           df['Species']] , 
    columns=[df['Flight Call'], df['Locality']], margins=True)
        final_summary.to_csv(path+'\summary.csv')
        
    def count_plot(df, path):
        """
        This function give final summary table of the dataframe and outputs to a specified path.
        """
        sns.set(rc={'figure.figsize':(12, 9)})
        cols = ['Genus', 'Species', 'Locality', 'Family', 'Habitat', 'Stratum']       
        for i in cols:
            sns_plot = sns.countplot(x=i, data=df, 
                             order=pd.value_counts(df[i]).iloc[:10].index)
            sns_plot.figure.savefig(str(path + '\\' + i +"_bar_plot.png"))
        
        pl1 = df[['Flight Call', 'Date']].groupby(['Flight Call']).count()
        pl1 = pl1.reset_index()
        pl1 = pl1.rename(columns = {'Date':'Count'})
        sns_plot = sns.countplot(x='Flight Call', data=df, 
                             order=pd.value_counts(df['Flight Call']).iloc[:10].index)
        sns_plot.figure.savefig(str(path + '\\' + "flight_call_bar_plot.png"))
    

def clean(collision, flight_call, light_level):
    """
    This function cleans data frame and returns data frames.
    """
    collision = collision
    flight_call = flight_call
    light_level = light_level
    
    # Maps to the correct column names
    flight_call_col_map = {'Species': 'Genus', 'Family': 'Species', 'Collisions': 'Family', 'Flight': 'Collisions', 
                       'Call':'Flight Call', 'Habitat': 'Habitat', 'Stratum':'Stratum'}
    flight_call.columns = [flight_call_col_map.get(x,"No_key") for x in flight_call.columns]
    
    # Removes whitespaces from column names
    collision.columns = collision.columns.str.strip()
    light_level.columns = light_level.columns.str.strip()
    
    # Trimming the leading and trailing whitespaces
    collision = data_process.trim(collision)
    flight_call = data_process.trim(flight_call)
    light_level = data_process.trim(light_level)
    
    # standardizing the date column
    collision['Date'] = pd.to_datetime(collision['Date'], format='%m/%d/%Y %H:%M')
    
    # sorting collision by Date for better understanding
    collision = collision.sort_values(by='Date', ascending=True, ignore_index=True)

    # dropping rows with missing date in light levels data
    mis_ind = light_level[light_level['Date'] == ''].index
    light_level = light_level.drop(index=mis_ind)
    
    # standardizing the date column
    light_level['Date'] = pd.to_datetime(light_level['Date'], format='%Y-%m-%d')
    
    # sorting light level by Date for better understanding
    light_level = light_level.sort_values(by='Date', ascending=True, ignore_index=True)
    
    # Checking null values
    #data_process.check_null(light_level)
    #data_process.check_null(collision)
    #data_process.check_null(flight_call)
    
    # Converting the categorical and non-numeric data to a Standard form for better data handling
    flight_call = data_process.capital(flight_call)
    collision = data_process.capital(collision)
    light_level = data_process.capital(light_level)
    collision['Locality'] = collision['Locality'].str.upper()
    # The below function drops duplicate rows since they result in erroneous reports
    flight_call = data_process.drop_dup(flight_call)
    light_level = data_process.drop_dup(light_level)
    
    # interpolating the missing values of light data with linear interpolationg
    light_level = light_level.interpolate(method='linear', axis=0)

    # The since the column can only have 'Yes/No', we can map 'Rare' to 'Yes'
    flight_call['Flight Call'] = np.where(flight_call['Flight Call']=='Rare','Yes',flight_call['Flight Call'])
    
    return (collision, flight_call, light_level)

def input_path(path):
    """
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

def output_path(path):
    """
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

def file_merge(collision, flight_call, light_level):
    """
    This function takes in 3 data frames and merges them and returns a final Data Frame.
    """
    collision = collision
    flight_call = flight_call
    light_level = light_level
    
    # merging collision and flight_call into a final dataframe
    final = pd.merge(collision, flight_call, on=['Genus', 'Species'], how='right')
    
    # dropping collision as it was already summarized
    final = final.drop('Collisions', axis=1)

    # merging collision and final into a light dataframe
    final2 = pd.merge(final, light_level, on='Date', how='left')
    
    return final2


# def extract_data(path):
#     """
#     This function extract zip files into input folder and deletes the zip file.
#     """
#     zf = ZipFile(path, 'r')
#     zf.extractall(path)
#     zf.close()
#     #os.remove(path)

def json_df(path):
    """
    This function converts the json file to data frame and returns data frames.
    """
    # Read file and return Data Frame
    with open(path, 'r') as myfile:
        data=myfile.read()
    # parse file
    df = pd.DataFrame(json.loads(data))
    #os.remove(path)
    return df

