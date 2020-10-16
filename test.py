# This python file has all the necessary functions used
import pandas as pd
import numpy as np
import os
# from zipfile import ZipFile
import json
import seaborn as sns
# importing required libraries
import config as c
import my_functions as my_func
import logging
from datetime import datetime


# from zipfile import ZipFile


class DataProcess:
    """
    This class has all the data cleaning functions
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.columns = df.columns
        self.select_dtypes = df.select_dtypes(include=['object'])

    def check_null(self):
        """
        This funtion takes a Data Frame as input and checks if the variables have any null values.
        It returns a Data Frame with column names and corresponding True/False if it has any nulls.
        """
        colname = self.columns
        na_array = []
        i: str
        for i in colname:
            # appends column name to temporary array
            na_array.append(str(i))
            # appends True/False after checking if it has any nulls
            na_array.append(self[i].isnull().values.any())
        res = pd.DataFrame(np.reshape(na_array, (-1, 2)), columns=['Column Names', 'Has Nulls'])
        return res

    def capital(self):
        """
        This function takes data frame and captializes every word of object columns and returns a data frame.
        """
        for i in self.select_dtypes:
            self[i] = self[i].str.title()
        return self

    # def drop_dup(df):
    #     """
    #     This function takes data frame and drop duplicate records and returns a data frame.
    #     """
    #     df = df.drop_duplicates()
    #     return df

    def remove_nl_tab(self):
        """
        This function takes data frame and removes new lines and tabs and returns a data frame.
        """
        self = self.replace(regex=['\n', '\t'], value='')
        return self

    def trim(self):
        """
        Trims whitespace from beginning and end of each value across all non-numeric columns in a dataframe
        :rtype: pd.DataFrame
        """
        df_obj = self.select_dtypes

        def function(x):
            return x.str.strip()

        self[df_obj.columns] = df_obj.apply(function)
        return self


# This class has the necessary functions to generate summary statistics
class SummaryStats:
    """
    This class gives basic summary statistics
    """

    def __init__(self, df):
        self = df
        self.columns = df.columns
        self.select_dtypes = df.select_dtypes(include=['object'])

    def freq(self):
        """
        This function gives frequency table of the dataframes and prints the frequency table.
        """
        for i in self.columns:
            print(pd.crosstab(index=self[i], columns='count').sort_values(by='count', ascending=False), '\n')

    def summarize(self, path):
        """
        This function give final summary table of the dataframe and outputs to a specified path.
        """
        final_summary = pd.crosstab(index=[self['Stratum'], self['Habitat'],
                                           self['Family'], self['Genus'],
                                           self['Species']],
                                    columns=[self['Flight Call'], self['Locality']], margins=True)
        final_summary.to_csv(path + '\\summary.csv')

    def count_plot(self, path):
        """
        This function give final summary table of the dataframe and outputs to a specified path.
        """
        sns.set(rc={'figure.figsize': (12, 9)})
        cols = ['Genus', 'Species', 'Locality', 'Family', 'Habitat', 'Stratum']
        for i in cols:
            sns_plot = sns.countplot(x=i, data=self,
                                     order=pd.value_counts(self[i]).iloc[:10].index)
            sns_plot.figure.savefig(str(path + '\\' + i + "_bar_plot.png"))

        #      pl1 = self[['Flight Call', 'Date']].groupby(['Flight Call']).count()
        #      pl1 = pl1.reset_index()
        #      pl1 = pl1.rename(columns={'Date': 'Count'})
        sns_plot = sns.countplot(x='Flight Call', data=self,
                                 order=pd.value_counts(self['Flight Call']).iloc[:10].index)
        sns_plot.figure.savefig(str(path + '\\' + "flight_call_bar_plot.png"))


def clean(collision_df, flight_call_df, light_level_df):
    """
    This function cleans data frame and returns data frames.
    :type collision_df: DataFrame
    :type flight_call_df: DataFrame
    :type light_level_df: DataFrame
    """
    collision_df: pd.DataFrame = collision_df
    flight_call_df: pd.DataFrame = flight_call_df
    light_level_df: pd.DataFrame = light_level_df

    # Maps to the correct column names
    flight_call_col_map = {'Species': 'Genus', 'Family': 'Species', 'Collisions': 'Family', 'Flight': 'Collisions',
                           'Call': 'Flight Call', 'Habitat': 'Habitat', 'Stratum': 'Stratum'}
    flight_call_df.columns = [flight_call_col_map.get(x, "No_key") for x in flight_call_df.columns]

    # Removes whitespaces from column names
    collision_df.columns = collision_df.columns.str.strip()
    light_level_df.columns = light_level_df.columns.str.strip()

    # Trimming the leading and trailing whitespaces
    collision_df = DataProcess.trim(collision_df)
    flight_call_df = DataProcess.trim(flight_call_df)
    light_level_df = DataProcess.trim(light_level_df)

    # standardizing the date column
    collision_df['Date'] = pd.to_datetime(collision_df['Date'], format='%m/%d/%Y %H:%M')

    # sorting collision by Date for better understanding
    collision_df = collision_df.sort_values(by='Date', ascending=True, ignore_index=True)

    # dropping rows with missing date in light levels data
    mis_ind = light_level_df[light_level_df['Date'] == ''].index
    light_level_df = light_level_df.drop(index=mis_ind)

    # standardizing the date column
    light_level_df['Date'] = pd.to_datetime(light_level_df['Date'], format='%Y-%m-%d')

    # sorting light level by Date for better understanding
    light_level_df = light_level_df.sort_values(by='Date', ascending=True, ignore_index=True)

    # Checking null values
    # DataProcess.check_null(light_level)
    # DataProcess.check_null(collision)
    # DataProcess.check_null(flight_call)

    # Converting the categorical and non-numeric data to a Standard form for better data handling
    flight_call_df = DataProcess.capital
    collision_df = DataProcess.capital
    light_level_df = DataProcess.capital
    collision_df['Locality'] = collision_df['Locality'].str.upper()
    # interpolating the missing values of light data with linear interpolationg
    light_level_df = light_level_df.interpolate(method='linear', axis=0)

    # The below function drops duplicate rows since they result in erroneous reports
    flight_call_df = flight_call_df.drop_duplicates()
    light_level_df = light_level_df.drop_duplicates(subset='Date', keep='first')

    # The since the column can only have 'Yes/No', we can map 'Rare' to 'Yes'
    flight_call_df['Flight Call'] = np.where(flight_call_df['Flight Call'] == 'Rare', 'Yes', flight_call_df[
        "Flight Call"])

    return collision_df, flight_call_df, light_level_df


def input_path(path):
    """
    This function takes input path and checks if file exist.
    """
    a: bool = True
    while a:
        path = input(path)
        if os.path.isdir(path):
            # a = False
            return path
        else:
            print('Please enter a valid input path')


def output_path(path):
    """
    This function takes input path and checks if file exist.
    """
    a: bool = True
    while a:
        path = input(path)
        if os.path.isdir(path):
            # a = False
            return path
        else:
            print('Please enter a valid input path')


def file_merge(collision_df, flight_call_df, light_level_df):
    """
    This function takes in 3 data frames and merges them and returns a final Data Frame.
    """
    collision_df = collision_df
    flight_call_df = flight_call_df
    light_level_df = light_level_df

    # merging collision and flight_call into a final dataframe
    final_df = pd.merge(collision_df, flight_call_df, on=['Genus', 'Species'], how='right')

    # dropping collision as it was already summarized
    final_df = final_df.drop('Collisions', axis=1)

    # merging collision and final into a light dataframe
    final2 = pd.merge(final_df, light_level_df, on='Date', how='left')

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
        data = myfile.read()
    # parse file
    df = pd.DataFrame(json.loads(data))
    # os.remove(path)
    return df


# initiating logging
now: datetime = datetime.now()
now: str = now.strftime('%m%d%y_%H%M%S')
logpath = c.config.get('log_path')
logging.basicConfig(filename=str(logpath + '\\' + now + '.log'), level=logging.DEBUG)
logging.info('Importing the required libraries')

logging.info('Libraries imported')

# Setting input and output path variables
logging.info('Setting input and output file paths')

input_pathname = my_func.input_path('Enter input path_name:')
output_pathname = my_func.output_path('Enter output path folder:')
logging.info('Input Path = ' + input_pathname)
logging.info('Output Path = ' + output_pathname)

# unzip file
# logging.info('Unzipping file')
# my_func.extract_data(input_pathname)

# Read Data Files
logging.info('Read Data Files')
collision = my_func.json_df(input_pathname + "\\" + c.config.get('collision'))
flight_call = my_func.json_df(input_pathname + "\\" + c.config.get('flight_call'))
light_level = my_func.json_df(input_pathname + "\\" + c.config.get('light_level'))

# Cleaning Data Files
logging.info('Cleaning Data Files')
(collision, flight_call, light_level) = my_func.clean(collision, flight_call, light_level)

# Merging the data files
logging.info('Merging the data files')
final = my_func.file_merge(collision, flight_call, light_level)

# Generating summary file
logging.info('Generating summary file')
my_func.summary_stats.summarize(final, output_pathname)

# Generating summary plots
logging.info('Generating summary plots')
my_func.summary_stats.count_plot(final, output_pathname)

# End of program
logging.info('End of program')
logging.shutdown()
