# Advanced Classification Predict Velly Shishoka

---


## Predict Overview: Climate Change Belief Analysis 2022

#### Climate Change
Climate change refers to long-term shifts in temperatures and weather patterns.


Many companies are built around lessening one’s environmental impact or carbon footprint. They offer products and services that are environmentally friendly and sustainable, in line with their values and ideals. They would like to determine how people perceive climate change and whether or not they believe it is a real threat. This would add to their market research efforts in gauging how their product/service may be received.

With this context, Our Company has been challenged with the task of creating a Machine Learning model that is able to classify whether or not a person believes in climate change, based on their novel tweet data.


-  analyse the supplied data;
-  identify potential errors in the data and clean the existing data set;
-  determine if additional features can be added to enrich the data set;
-  build a model that is capable of forecasting the three hourly demand shortfalls;
-  evaluate the accuracy of the best machine learning model;
-  perform the feature selection for most important features in the model’s prediction decision, and
-  explain the inner working of the model to a non-technical audience.

## Problem Statement


In this project we determine how people perceive climate change and whether or not a person believes in climate change. This will be done by Building a Natural Language Processing model which will classify whether or not a person believes in climate change, based on their novel tweet data. The Sentiment of tweet, which will be referred to as the target variable, will be modelled as a function of Tweet bodies from massage.


###  **Data Description**

>    The collection of this data was funded by a Canada Foundation for Innovation JELF Grant to Chris Bauch, University of Waterloo. The dataset aggregates tweets pertaining to climate change collected between Apr 27, 2015 and Feb 21, 2018. In total, 43943 tweets were collected. Each tweet is labelled as one of the following classes
Class Description 

 **Class Description**

- 2 News: the tweet links to factual news about climate change 

- 1 Pro: the tweet supports the belief of man-made climate change 

- 0 Neutral: the tweet neither supports nor refutes the belief of man-made climate change 

- -1 Anti: the tweet does not believe in man-made climate change

**Variable definitions:**

- ***sentiment***: Sentiment of tweet

- ***message***: Tweet body

- ***tweetid***: Twitter unique id

<a id="cont"></a>

## Table of Contents

<a href=#one>1. Importing Packages</a>

<a href=#two>2. Loading Data</a>

<a href=#three>3. Exploratory Data Analysis (EDA)</a>

<a href=#four>4. Data Engineering</a>

<a href=#five>5. Modeling</a>

<a href=#six>6. Model Performance</a>

<a href=#seven>7. Model Explanations</a>