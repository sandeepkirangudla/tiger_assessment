#importing required libraries
import HCSC.config as config
import HCSC.my_functions as my_func
import pandas as pd

# Setting input and output path variables
# input_pathnames
covid = config.get('covid_df')
pop = config.get('pop_df')
output_pathname = my_func.output_path('Enter output path folder:')

# Read Data Files
covid_df = pd.read_csv(covid)
pop_df = pd.read_csv(pop, encoding='latin-1',
                     usecols = ['POPESTIMATE2019', 'STATE', 'COUNTY'])

# Cleaning Data Files
(covid_df, pop_df) = my_func.clean(covid_df, pop_df)


# Merging the data files
final = my_func.final_merge(covid_df, pop_df)

# Generating summary file
my_func.SummaryStats.summarize(final, output_pathname)