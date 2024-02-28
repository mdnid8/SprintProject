
# Optimizing Wait Times at EV Charging Stations in Palo Alto

Data Science Program, Winter 2023


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#project-introduction">Project Introduction</a></li>
	<li><a href="#eda-and-initial-models">EDA and Initial Models</a></li>
	<ul>
	<li><a href="#data">Data</a></li>
	<li><a href="#prerequisites">Prerequisites</a></li>
		<li><a href="#prerequisites">About The Project</a></li>
	</ul>
     
    
   
  </ol>
</details>

## Project Introduction

The electric vehicle (EV) charging industry is undergoing significant expansion, driven by the increasing adoption of electric vehicles for various compelling reasons. Palo Alto stands as a pioneering city equipped with EV charging stations to accommodate the growing community of EV drivers. These charging stations play a crucial role in curbing greenhouse gas emissions, conserving gasoline, and fostering positive environmental impacts. Additionally, they present lucrative opportunities for business owners.

However, the challenge faced by EV adaptation lies in the extended duration of charging and associated wait times. Many EV drivers lack real-time information about wait periods or the availability of charging stations. Addressing these concerns by developing a solution for predicting wait times and charging durations can immensely benefit EV customers. It would not only save time but also optimize the waiting experience, resulting in a more efficient charging process.

It's noteworthy that the availability of charging stations doesn't necessarily translate to high costs, as numerous stations offer free charging services. Utilizing the provided dataset, our objective is to construct a predictive model that can anticipate the advantages of charging stations for the city of Palo Alto. Access the dataset here to explore the insights derived from the analysis.<a href='https://www.kaggle.com/code/prasaddevh/eda-evchargingpaloaltoca'>Click here to access the dataset</a>

## EDA and Initial Models

**EDA Summary:**
Original Dataset has 32 columns with 259415 rows. All columns describe important aspect of charging stations located in Palo Alto City. 
If you are not familar with EV charging stations, it is required to know some of the terms like MAC. 

MAC address (Media Access Control address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. It is a hardware address that uniquely identifies each device on a network. 

There are two types of charging port. type 1 and type 2. type 1 charging port is slower than type 2 charging port but it is cheaper and some stations provide free service.

For further details on level 1 and level 2 Type 1 (J1772): This is a standard charging port in North America and Japan. It is also known as SAE J1772.
Type 2 (Mennekes): This is a standard charging port in Europe. It is also known as IEC 62196-2.

EVSE ID use to identify charging location, track, manage and record charging history. It is important column to record all previous charging histories.

Plug type is similar to Port Type. It refers to the type of connector/plug used by EV to connect to a charging station. Different electric vehicles and charging stations may use different plug types, and the choice of plug type depends on factors such as regional standards, vehicle compatibility, and charging infrastructure specifications. At the moment, there are 5 different types of plug/port type available. Most popular one is Tesla upercharger in Palo Alto.


The features considered for the predictive model of total charging duration include:

Fee (varied rates across different stations)
Weekend charging indicator
Weekday charging indicator
Energy usage at charging stations (encompassing greenhouse gas saved and energy usage)
Port type
Port number
Utilizing these features, the model predicts that the total duration to fully charge an electric vehicle is approximately 64 minutes. Notably, the accuracy of both the training and test data surpasses 90%, aligning with expectations given the model's foundation on these features.

Insights from the Linear Regression Model:

The linear regression model adeptly captures a substantial portion of the variability in the target variable.
Additionally, explorations into Ridge and Lasso regression, as well as time series models, were undertaken, although they did not yield significant additional insights.

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
