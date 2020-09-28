#importing required libraries
import Tiger_Assessment.config as config
import Tiger_Assessment.my_functions as my_func

from datetime import datetime


# Setting input and output path variables
input_pathname = my_func.input_path('Enter input path_name:')
output_pathname = my_func.output_path('Enter output path folder:')

# unzip file
# logging.info('Unzipping file')
# my_func.extract_data(input_pathname)

# Read Data Files
collision = my_func.json_df(input_pathname + "\\" + config.get('collision'))
flight_call = my_func.json_df(input_pathname + "\\" + config.get('flight_call'))
light_level = my_func.json_df(input_pathname + "\\" + config.get('light_level'))


# Cleaning Data Files
(collision, flight_call, light_level) = my_func.clean(collision, flight_call, light_level)

# Merging the data files
final = my_func.file_merge(collision, flight_call, light_level)

# Generating summary file
my_func.summary_stats.summarize(final, output_pathname)

# Generating summary plots
my_func.summary_stats.count_plot(final, output_pathname)

# End of program