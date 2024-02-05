# Brainstation_Capstone_Project
# Total Charging Duration At EV Charging Stations In Palo Alto
Data Science program, Winter 2023.  


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#about-the-project">Project Introduction</a></li>
	<li><a href="#EDA-and-Initial-Models">EDA</a></li>
	<ul>
	<li><a href="#data">Data</a></li>
	<li><a href="#prerequisites">Prerequisites</a></li>
	</ul>
     
    
   
  </ol>
</details>

## About The Project

Palo Alto EV Charging Stations Usage And Other Related Factors
The EV Charging Stations industry is expanding as people increasingly adopt electric vehicles for various reasons. Palo Alto stands out as one of the few cities equipped with EV charging stations to cater to the growing number of EV drivers. These charging stations have a significant impact on reducing greenhouse gas emissions, saving gasoline, and contributing to other positive environmental aspects. Moreover, EV charging stations prove to be profitable for business owners.

Importantly, the availability of charging stations does not necessarily equate to high costs, as many stations offer free charging services. Leveraging the dataset, our goal is to construct a model capable of predicting the benefits of charging stations for the city of Palo Alto.
<a href='https://www.kaggle.com/code/prasaddevh/eda-evchargingpaloaltoca'>Click here to access the dataset</a>

## EDA and Initial Models

Originally, there were 30 columns to begin with, but some, like 'Currency' and 'Country,' were dropped as they are not necessary for the project. Some new columns were added after the initial exploratory data analysis (EDA), such as 'byWeek,' 'weekend,' and 'weekday,' to analyze additional data on charging station usage in Palo Alto.


### Data
For now:
1 datasets covering all common charging behaviours are explored in this project:
* Public
	* Palo Alto (California, USA)





### Prerequisites

Here are the various R packages that can be directly installed in Rstudio as follows:

```
Jupyternotebook   -pip install notebook
````


## Sprint 2
### Introduction
 
Previously, I lacked a clear direction for my dataset analysis. Following preprocessing, I determined the goal of employing regression models to predict energy consumption in three distinct postal codes within Palo Alto over a 10-year period. Despite grouping essential features by postal code on both daily and monthly bases, the regression models yielded poor performance, even when simplifying the task to predicting energy consumption based on the initial four energy-related columns. Consequently, I opted to explore the potential improvements offered by confusion matrices and scaling the existing data.
In this notebook, our focus will be on logistic regression, with an emphasis on optimizing the model through various methods. The primary objective is to leverage historical data to learn patterns and construct a time series model that enhances predictive capabilities.

### Data Dictionary

| **Feature**  | **Description**                                                                                                                                                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charging Time      | Distributed in average value                                                                                                                                                                                                                            |
| Postal Code      | 94301, 94302,94306                                                                                                                                                                                                                   |
| GreenHouseGasSave (kg)      | Kg                                                                                                                                    |
| Energy Consumption (kWh) | Distributed in total sum                                                                                                                                                                          |
| Gasoline Savings (gal)     | Distributed in total sum                                                              
### EDA
The dataset we've loaded is the same as in Sprint 1; however, for Sprint 2 model building, I've created a new dataset, df1. In this dataset, I've performed grouping for columns related to energy consumption. Additionally, I've crafted a straightforward time series model utilizing 'GreenHouseGasSaved (kg)' and 'Gasoline Savings (gal)'.





## Author
* **Steve Kim** - mdnid@hotmail.com

## License
