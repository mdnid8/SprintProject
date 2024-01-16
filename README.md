# Brainstation_Capstone_Project
Data Science program, Winter 2023.  

## Project Introduction: Palo Alto EV Charging Stations Usage And Other Related Factors
The EV Charging Stations industry is expanding as people increasingly adopt electric vehicles for various reasons. Palo Alto stands out as one of the few cities equipped with EV charging stations to cater to the growing number of EV drivers. These charging stations have a significant impact on reducing greenhouse gas emissions, saving gasoline, and contributing to other positive environmental aspects. Moreover, EV charging stations prove to be profitable for business owners.

Importantly, the availability of charging stations does not necessarily equate to high costs, as many stations offer free charging services. Leveraging the dataset, our goal is to construct a model capable of predicting the benefits of charging stations for the city of Palo Alto.
<a href='https://www.kaggle.com/code/prasaddevh/eda-evchargingpaloaltoca'>Click here to access the dataset</a>

## Technologies
* Jupyternotebook
you can install Jupyternotebook by  -pip install notebook

## EDA and Initial Models
Originally, there were 30 columns to begin with, but some, like 'Currency' and 'Country,' were dropped as they are not necessary for the project. Some new columns were added after the initial exploratory data analysis (EDA), such as 'byWeek,' 'weekend,' and 'weekday,' to analyze additional data on charging station usage in Palo Alto.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
	<li><a href="#getting-started">Getting Started</a></li>
	<ul>
	<li><a href="#data">Data</a></li>
	<li><a href="#prerequisites">Prerequisites</a></li>
	</ul>
    <li><a href="#key-visual">Key visual</a></li>    
    <li><a href="#author">Author</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project

Numerous papers highlight the lack of charging station data available in order to build models that are consistent with reality. 
In this context, the purpose of this project to gather open EV charging datasets available in order to foster reproducible research in the field.
In particulare we explores electric vehicle charging session data from different open data sources which can be used for research purposes. 

A thorough walkthrough of the datasets as well as a review of EV load models are proposed in the following publication:

* **Yvenn Amara-Ouali, Yannig Goude, Pascal Massart, Jean-Michel Poggi, Hui Yan** - *A Review of Electric Vehicle Load Open Data and Models* (2021) - [Energies](https://doi.org/10.3390/en14082233)

Keywords: electric vehicles, charging point, load modelling, smart charging, open data, statistical modelling

## Getting Started

This repository contains the most relevant data and codes produced for the experiments detailed in our paper. 

[1. Input Data](./1.%20Input%20Data) contains the raw data we found in our research. Feel free to contact if you know of any additional open data sources which may not be present here.
[2. Scripts](./2.%20Scripts) gathers the R scripts used to preprocess and analyse the data.
[3. Output](./3.%20Output) assembles the csv outputs generated after the data preprocessing


### Data

8 datasets covering all common charging behaviours are explored in this project:
* Public
	* Dundee (UK)
	* Perth & Kinross (UK)
	* Palo Alto (California, USA)
	* Boulder (Colorado, USA)
	* Paris (France)
* Residential
	* Electric Chargepoint Analysis (Domestics UK)
* Workplace
	* SAP Labs (France)
	* ACN (California, USA)
	
The **Electric Chargepoint Analysis** dataset is too heavy for GitHub and is not directly available on this repository. 
Please refer to this [pdf file](./1.%20Input%20Data/6.%20Chargepoint%20Analysis) in order to retrieve the dataset and put it in the same folder for the code to run without errors. 

### Prerequisites

Here are the various R packages that can be directly installed in Rstudio as follows:

```
install.packages("tidyverse")
install.packages("lubridate")
install.packages("stringr")
install.packages("rjson")
install.packages("fitdistrplus")
````

## Key visual

- National EV market share per country coloured by data availability
	- HCS => Historical Charging Session (data)
	- RTCS => Real-Time Charging Session (data)
	- T => Traffic (or exogeneous data)
![National EV market share per country coloured by data availability](market.png)

## Author
* **Yvenn Amara-Ouali** - (https://www.yvenn-amara.com)

## License
