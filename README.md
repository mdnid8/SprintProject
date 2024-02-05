# Brainstation_Capstone_Project
# Predictive Modeling and Optimization of Energy Consumption in Palo Alto City Using Charging Station Historical Data

Data Science Program, Winter 2023


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#about-the-project">Project Introduction</a></li>
	<li><a href="#EDA-and-Initial-Models">EDA</a></li>
	<ul>
	<li><a href="#data">Data</a></li>
	<li><a href="#prerequisites">Prerequisites</a></li>
		<li><a href="#prerequisites">About The Project</a></li>
	</ul>
     
    
   
  </ol>
</details>

## About The Project

The electric vehicle (EV) charging industry is undergoing significant expansion, driven by the increasing adoption of electric vehicles for various compelling reasons. Palo Alto stands as a pioneering city equipped with EV charging stations to accommodate the growing community of EV drivers. These charging stations play a crucial role in curbing greenhouse gas emissions, conserving gasoline, and fostering positive environmental impacts. Additionally, they present lucrative opportunities for business owners.

However, the challenge faced by EV adaptation lies in the extended duration of charging and associated wait times. Many EV drivers lack real-time information about wait periods or the availability of charging stations. Addressing these concerns by developing a solution for predicting wait times and charging durations can immensely benefit EV customers. It would not only save time but also optimize the waiting experience, resulting in a more efficient charging process.

It's noteworthy that the availability of charging stations doesn't necessarily translate to high costs, as numerous stations offer free charging services. Utilizing the provided dataset, our objective is to construct a predictive model that can anticipate the advantages of charging stations for the city of Palo Alto.
<a href='https://www.kaggle.com/code/prasaddevh/eda-evchargingpaloaltoca'>Click here to access the dataset</a>

## EDA and Initial Models

Originally, there were 30 columns to begin with, but some, like 'Currency' and 'Country,' were dropped as they are not necessary for the project. Some new columns were added after the initial exploratory data analysis (EDA), such as 'byWeek,' 'weekend,' and 'weekday,' to analyze additional data on charging station usage in Palo Alto.


### Data
For now: 1 dataset covering all common charging behaviors are explored in this project:

Public Palo Alto (California, USA)





### Prerequisites

Here are the various R packages that can be directly installed in Rstudio as follows:

```
Jupyternotebook   -pip install notebook
````


## Sprint 2
### Introduction
 
Initially, I faced challenges in defining a clear direction for my dataset analysis. After preprocessing, I established the objective of employing regression models to forecast energy consumption in three specific postal codes within Palo Alto over a 10-year span. Despite organizing crucial features by postal code on both daily and monthly scales, the regression models exhibited subpar performance, even when simplifying the task to predicting energy consumption based on the initial four energy-related columns. Consequently, I decided to explore potential enhancements by utilizing confusion matrices and scaling the existing data. In this notebook, our focus centers on logistic regression, with a key emphasis on optimizing the model through various methods. The primary goal is to leverage historical data, discern patterns, and construct a time series model that significantly improves predictive capabilities.

### Data Dictionary

| **Feature**  | **Description**                                                                                                                                                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charging Time      | Distributed in average value                                                                                                                                                                                                                            |
| Postal Code      | 94301, 94302,94306                                                                                                                                                                                                                   |
| GreenHouseGasSave (kg)      | Kg                                                                                                                                    |
| Energy Consumption (kWh) | Distributed in total sum                                                                                                                                                                          |
| Gasoline Savings (gal)     | Distributed in total sum                                                              
### EDA
Insights from the Linear Regression Model

The features considered for the predictive model of total charging duration include:

Fee (varied rates across different stations)
Weekend charging indicator
Weekday charging indicator
Energy usage at charging stations (encompassing greenhouse gas saved and energy usage)
Port type
Port number
Utilizing these features, the model predicts that the total duration to fully charge an electric vehicle is approximately 64 minutes. Notably, the accuracy of both the training and test data surpasses 90%, aligning with expectations given the model's foundation on these features.

Insights from the Linear Regression Model

The linear regression model adeptly captures a substantial portion of the variability in the target variable. Additionally, explorations into Ridge and Lasso regression, as well as time series models, were undertaken, although they did not yield significant additional insights.





## Author
* **Steve Kim** - mdnid@hotmail.com

## License
