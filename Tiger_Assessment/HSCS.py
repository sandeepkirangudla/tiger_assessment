#importing required libraries
import HCSC.config as config
import HCSC.data_clean as data_clean
import HCSC.IO_path as IO_path
import HCSC.merge as merge
import HCSC.summary_stats as summary_stats
import pandas as pd

# Setting input and output path variables
# input_pathnames
covid = config.config.get('covid_df')
pop = config.config.get('pop_df')
output_pathname = IO_path.output_path('Enter output path folder:')

# Read Data Files
covid_df = pd.read_csv(covid)
pop_df = pd.read_csv(pop, encoding='latin-1',
                     usecols = ['POPESTIMATE2019', 'STATE', 'COUNTY'])

# Cleaning Data Files
(covid_df, pop_df) = data_clean.clean(covid_df, pop_df)


# Merging the data files
final = merge.final_merge(covid_df, pop_df)

# Generating summary file
summary_stats.SummaryStats.summarize(final, output_pathname)