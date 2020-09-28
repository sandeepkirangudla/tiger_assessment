# Bird Collision vs Artificial Light

##### The below project is a part of Tiger Machine Learning Engineer position. 
[Winger et al, 2019](https://royalsocietypublishing.org/doi/10.1098/rspb.2019.0364#d3e550) examined nocturnal flight-calling behavior and vulnerability to artificial light in migratory birds.

> "Understanding interactions between biota and the built environment is increasingly important as human modification of the landscape expands in extent and intensity. For migratory birds, collisions with lighted structures are a major cause of mortality, but the mechanisms behind these collisions are poorly understood. Using 40 years of collision records of passerine birds, we investigated the importance of species' behavioural ecologies in predicting rates of building collisions during nocturnal migration through Chicago, IL and Cleveland, OH, USA. "

> "One of the few means to examine species-specific dynamics of social biology during nocturnal bird migration is through the study of short vocalizations made in flight by migrating birds. Many species of birds, especially passerines (order Passeriformes), produce such vocal signals during their nocturnal migrations. These calls (hereafter, ‘flight calls’) are hypothesized to function as important social cues for migrating birds that may aid in orientation, navigation and other decision-making behaviours.not all nocturnally migratory species make flight calls, raising the possibility that different lineages of migratory birds vary in the degree to which social cues and collective decisions are important for accomplishing migration. "

As per the researcher the bird collision with buildings in the metropolitan cities are mainly caused by artificial light. Birds react to this artificial light and initiate a flight call which attracts other birds for flight and results in collision with the building structure.

## Citations

When using this data, please cite the original publication:

> Winger BM, Weeks BC, Farnsworth A, Jones AW, Hennen M, Willard DE (2019) Nocturnal flight-calling behaviour predicts vulnerability to artificial light in migratory birds. Proceedings of the Royal Society B 286(1900): 20190364.  [https://doi.org/10.1098/rspb.2019.0364](https://doi.org/10.1098/rspb.2019.0364)

If using the data alone, please cite the  [Dryad data package](https://cran.r-project.org/web/packages/rdryad/rdryad.pdf):

> Winger BM, Weeks BC, Farnsworth A, Jones AW, Hennen M, Willard DE (2019) Data from: Nocturnal flight-calling behaviour predicts vulnerability to artificial light in migratory birds. Dryad Digital Repository.  [https://doi.org/10.5061/dryad.8rr0498](https://doi.org/10.5061/dryad.8rr0498)
> 
# Program Execution
The goal of the project is to generate a summary table of all given 3 data files. Below is the step by step process of executing this program.
The user import *Tiger_Assessment* library from pip by running the following command. 
(<b>pip install Tiger-Assessment </b>). This opens up a GUI in which the user have to provide


 **1. Input Path and File Name
 
2. Output Folder Path**

## Data Files

As a part of this project, there are 3 JSON files ( Collision, Flight_Call, Light_Levels). These 3 files are placed in the landing zone. The path of the landing zone is given by the user and the output file directory is also given by the user.

## Libraries
Below are the libraries used as a part of this project.

 - pandas
 - numpy
 - matplotlib
 - seaborn
 - logging
 - os
 - datetime
 - zipfile
 - json
 - subprocess
 - sys

## Project Files & Folders

 <ul>
 <li><b>Data</b></li>
	<p>This folder will have the data files required to for the program. Below is the file structure and description.</p>
	 <ul>
	 <li><b>Input</b></li>
	 <p>This folder will have the input files required to for the program.</p>
	 <li><b>Ouput</b></li>
	 <p>This folder will have the output files required to for the program.</p>
	</ul>
	<li><b>Tiger Assessment</b></li>
	<p>This folder just has the init.py file required to initiate the package</p>
	<li><b>Logs</b></li>
	<p>This folder has all the logs generated by program</p>
	<li><b>config.py</b></li>
	<p>This file initial configuration setting like paths etc.</p>
	<li><b>requrirements</b></li>
	<p>This file has all the required packages</p>
	<li><b>LICENSE</b></li>
	<p>This is an MIT license</p>
	<li><b>setup.py</b></li>
	<p>This is a setup file required by python to package and distribute the code. This file has all the indetail description and specifications.</p>
	<li><b>my_functions.py</b></li>
	<p>This file has all the classes and functions required for the project</p>
	<li><b>Tiger_Assessment.py</b></li>
	<p>This is the main file of the project. The user runs this file which will take input path and file and generate the summary table in given output path.</p>
</ul>

## Data Dictionary
### `chicago_collision_data`
| Variable |Class  | Description|
|--|--|--|
| genus | factor | Bird Genus | 
|species|	factor|	Bird species|
|date	|date	|Date of collision death (ymd)|
|locality|	factor|	MP or CHI - recording at either McCormick Place or greater Chicago area|

### `flight_call`
| Variable |Class  | Description|
|--|--|--|
| genus | factor | Bird Genus | 
|species|	factor|	Bird species|
|family|	factor|	Bird Family|
|flight_call|	factor|	Does the bird use a flight call - yes or no|
|habitat|	factor	|Open, Forest, Edge - their habitat affinity
|stratum|	factor	|Typical occupied stratum - ground/low or canopy/upper|
|collisions|	integer | The total number of collision in the last 40 year|

### `light_levels`
| Variable |Class  | Description|
|--|--|--|
|date	|date	|Date of light level observed|
|light source|	integer | Number of windows lit at the McCormick Place, Chicago - higher = more light|


## Data Cleaning and Preprocessing
Below are the following steps used to clean and preprocess the data.

### 1. UnZipping
The data files are extracted from zip, they are placed in *./Data/Input/* directory and the originial zip file is deleted.

### 2. JSON to Data Frame
The files received are in JSON format. These files have to be processed and converted into data frame for analysis purposes. I have created *my_func.json_df* that take path of json files from config file and returns a data frame

### 3. Cleaning the Data Files
*Data_Process* class has all the necessary functions required to clean the data.

Below are the steps used to clean the data file.

 1. #### Cleaning and Mapping Columns
     <p>We see that <i>flight_call</i> has its column order wrong. I have used a dictionary to map the columns correctly. I also stripped the white space in columns which helps in standardizing column names.</p>
 2. #### Trimming the Leading and Trailing whitespaces
     <p>As a best practice, it is always recommended to clean the leading and trailing whitespaces. <i>data_process.trim</i> fuction trim the leading an trailing whitespace for non-numeric columns.</p>
3. #### Standardizing the Dates
     <p>As a best practice, it is always recommended to standardize <i>Dates</i> columns. </p>
4. #### Sort by Dates
     <p>As a best practice, it is always recommended to sort data by <i>Dates</i> columns. </p>
5. #### Dropping rows with missing Date in <i>light_levels</i> data
     <p>Since the light_source is recorded by date, we can drop rows with empty dates. </p>
6. #### Capitalize the non-numeric columns
     <p>As a best practice, it is always recommended to Capitalize the factor (non-numeric) columns, especially identifiers like names, places, etc, so that some of the Data Entry errors (like <i>John Doe</i> entered as <i>john Doe</i>) can be fixed.</p>     
7. #### Dropping duplicate
     <p>As a best practice, it is always recommended to drop duplicate records if, it has any unique or key values. In our case, <i>flight_call</i> and <i>light_level</i> have data column as unique value. The function <i>data_process.drop_dup</i> take in data frame and drop duplicate records.
8. #### Interpolating
     <p>As a best practice, it is always recommended to interpolate missing values where ever deemed necessary, but with extreme caution. In our case, <i>light_level</i> has missing records. We can use a simple linear interpolate method because the light_source levels, on an average don't change drastically from the previous few days.
9. #### In depth cleaning
     <p>It is observed that <i>flight_call</i> column of <i>flight_call</i> data has an extra <i>Rare</i> factor. Since it can only have <i>Yes/No</i>, we can assume that <i>Rare</i> is <i>Yes</i>.

## Merging the Data Frames
After doing the data preprocessing and clean, we obtain clean files that we can merge. <i>my_func.file_merge</i> takes in 3 data frames and output 1 final data frame on which we can do our analysis.

## Generating Summary File and Plots
The final step is generate the result and plots. <i>my_func.summary_stats.summarize</i> generates the summary file as a csv because it is very easy to interpret and do custom analysis on csv. <i>my_func.summary_stats.count_plot</i> generate bar plot of different features like <i>family, genus, Locality</i> etc.

## Insights
#### Collision by Flight Call of Birds
We can see that birds that employ flight calls have significantly (almost 35000 times) more collision than the birds that don't employ flight calls.
![Flight Call_bar_plot](https://github.com/sandeepkirangudla/tiger_assessment/blob/master/Data/Output/flight_call_bar_plot.png)

We can see here that the flight call is a significant factor but we may need futher testing to be sure.

#### Collision by Family of Birds
We can see that Passerellidae Family of birds have the highest collisions followed by Parulidae and Turdidae.
![Family Bar Plot](https://github.com/sandeepkirangudla/tiger_assessment/blob/master/Data/Output/Family_bar_plot.png)

Here we observe that Passerellidae is most common family that have collisions. But its is highly possible that Passerellidae may be majority in the observed cities. If we an estimate of percentage distribution of birds by family we can take a weighted proportion and then check for most common family of birds.
#### Collision by Genus of Birds
We can see that Melospiza Genus of birds have the highest collisions followed by Zonotrichia and Catharus.
![Genus_bar_plot](https://github.com/sandeepkirangudla/tiger_assessment/blob/master/Data/Output/Genus_bar_plot.png)

Here we observe that Melospiza is most common genus that have collisions. But its is highly possible that Melospiza may be majority in the observed cities. If we an estimate of percentage distribution of genus by family we can take a weighted proportion and then check for most common genus of birds.

#### Collision by Species of Birds
We can see that Albicollis species of birds have the highest collisions followed by Hyemalis and Melodia.
![Species_bar_plot](https://github.com/sandeepkirangudla/tiger_assessment/blob/master/Data/Output/Species_bar_plot.png)

Here we observe that Albicollis is most common species that have collisions. But its is highly possible that Albicollis may be majority in the observed cities. If we an estimate of percentage distribution of species by family we can take a weighted proportion and then check for most common species of birds.

#### Collision by Habitat of Birds
We can see that birds that usually dwell in Forest are twice as much as birds that live on edge and almost 7 times as much as birds who live in the open.
![Habitat_bar_plot](https://github.com/sandeepkirangudla/tiger_assessment/blob/master/Data/Output/Habitat_bar_plot.png)

Here we can see that birds that are not used to artificial lighting are more susuptible for collisions. This could be a compelling feature.

#### Collision by Locality of Birds
We can see that there is an equal distribution of birds in both localities.
![Locality_bar_plot](https://github.com/sandeepkirangudla/tiger_assessment/blob/master/Data/Output/Locality_bar_plot.png)

#### Collision by Stratum of Birds
We can see that the lower stratum birds have twice as much as collision than upper stratum birds.![Stratum_bar_plot](https://github.com/sandeepkirangudla/tiger_assessment/blob/master/Data/Output/Stratum_bar_plot.png)

Here we can see that birds who live on lower stratum are more susuptible for collisions. This could be a compelling feature.

# Summary & Findings

#### 1. Passerellidae Family of birds have the highest collisions followed by Parulidae and Turdidae
#### 2. Melospiza Genus of birds have the highest collisions followed by Zonotrichia and Catharus
#### 3. Albicollis species of birds have the highest collisions followed by Hyemalis and Melodia
#### 4. Birds that usually dwell in Forest are twice as much as birds that live on edge and almost 7 times as much as birds who live in the open
#### 5. The lower stratum birds have twice as much as collision than upper stratum birds
#### 6. Birds who employ flight calls have twice as much as collision than the birds who don't employ flight calls