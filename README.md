
  
# Covid - 19 Daily Cumulative Statistics
##### The below project is a part of HCSC Machine Learning Engineer position. 

As part of HCSC's COVID19 response, the Data Science team needs to prepare daily/weekly updates of nationwide infection counts, organized by county. We use numeric FIPS code https://en.wikipedia.org/wiki/FIPS_county_code rather than    
state and county name to serve our results.    
    
For every FIPS code and date, the program generates: population, daily cases, daily deaths, cumulative cases to date, and cumulative death counts to date.    
    
## Citations The data is supplied by [New York Times](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html).    
    
For details on the data extraction please refer https://github.com/nytimes/covid-19-data    
    
# Program Execution 

The goal of the project is to generate a daily/weekly updates of nationwide infection counts, organized by county. Below is the step by step process of executing this program.    
The user imports *Tiger_Assessment* library from pip by running the following command.     
(<b>pip install Tiger-Assessment </b>). This opens up a GUI in which the user have to provide    
    
 **Output Folder Path**    
 ## Data Files    
 As a part of this project, there are two csv files provided by [New York Times](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv) and [US Censes Data](https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv). The path of the output file directory is given by the user.    
    
## Libraries Below are the libraries used as a part of this project.    
    
 - pandas    
 - numpy    
 - os    
 - datetime    
    
## Project Files & Folders    
    
 <ul>    
   <li><b>Tiger_Assessment</b></li>    
   <p>This folder just has the init.py file required to initiate the package and program</p>    
   <li><b>config.py</b></li>    
   <p>This file initial configuration setting like paths etc.</p>    
   <li><b>LICENSE</b></li>    
   <p>This is an MIT license</p>    
   <li><b>setup.py</b></li>    
   <p>This is a setup file required by python to package and distribute the code. This file has all the indetail description and specifications.</p>    
   <li><b>data_process.py</b></li>    
   <p>This file has all the classes and functions required for the to pre-process the data.</p>    
   <li><b>data_clean.py</b></li>    
   <p>This file has all the classes and functions required for the to clean the data.</p>    
   <li><b>IO_path.py</b></li>    
   <p>This file has all the functions required to set the output and input paths.</p>    
   <li><b>merge.py</b></li>    
   <p>This file has all the functions required to merge the data into a final output on which we can summarize.</p>    
   <li><b>summary_stats.py</b></li>    
   <p>This file has all the classes and functions required to generate the summary output to desired location.</p>    
   <li><b>Tiger_Assessment.py</b></li>    
   <p>This is the main file of the project. The user runs this file which will take input path and file and generate the summary table in given output path.</p>    
</ul>    
    
## Data Dictionary 
### `covid` 

| Variable |Class  | Description|    
|--|--|--|    
|date  |date  |Date of collision death (ymd)|    
| County| factor | US County Names |     
| State| factor | US State Names |     
| FIPS| factor | US FIPS code|     
|Cases|    integer|Covid Cases reported per day|    
|Deaths|   integer|Covid Deaths reported per day|    

### `population` 
We are extracting only the required columns from the US Censes data.
| Variable |Class  | Description |    
| -- | -- | -- |    
| STATE | factor | US State FIPS ID |     
| County |   factor |    US County FIPS ID |    
| POPESTIMATE2019 |  integer |   US population estimate |    
  
    
## Data Cleaning and Preprocessing
 Below are the following steps used to clean and preprocess the data.    
    
### 1. Reading the Data 
The path to the input files are given in *config.py*. These files are read using pandas for analysis purposes.    
    
### 2. Cleaning the Data Files
 *Data_Process* class has all the necessary functions required to clean the data.    
    
Below are the steps used to clean the data file.    
 1. #### Cleaning and Mapping Columns    
 <p>I have used a column dictionarys to map the column names correctly which helps in standardizing the column names.</p>    
    
 2. #### Standardizing the Dates    
 <p>As a best practice, it is always recommended to standardize <i>Dates</i> columns. </p>    
  
3. #### Sort by Dates    
 <p>As a best practice, it is always recommended to sort data by <i>Dates</i> columns. </p>    
  
4. #### Standarizing FIPS columns.    
   1. <p>Population: Concatenating State_ID and County_ID to generate FIPS in population data, so that it can be joined with daily covid data.    
   2. Covid: Filling the empty and unknown FIPS IDs with a default value to standardize the column.</p> .    
    
## Merging the Data Frames
After doing the data preprocessing and clean, we obtain clean files that we can merge. <i>merge.final_merge</i> takes in two data frames and output one final data frame on which we can do our analysis.    
    
## Generating Summary File
The final step is generate the result. <i>summary_stats.SummaryStats.summarize</i> generates the summary file as a csv because it is very easy to interpret and do custom analysis on csv.    
    
## Future Edition

### Interactive Plots
We can include interactive plots using pyplot which help the end user analyze the data much more efficiently.