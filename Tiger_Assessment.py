# importing required libraries
import config as c
import my_functions as my_func
import logging
from datetime import datetime

# initiating logging
now = datetime.now()
now = now.strftime('%m%d%y_%H%M%S')
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
