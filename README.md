# Customer Churn Prediction for Telecommunications company

<img src="assets/FastAPI.png" height="140"> <img src="assets/scikit-learn.png" height="140"> <img src="assets/Matplotlib.png" height="140"> <img src="assets/Pandas.png" height="140"> <img src="assets/NumPy.png" height="140">

## Overview 
We do exploratory analysis of telecommunications data with python
and matplotlib. Then we train a classification model with scikit-learn, and
create a pipeline for potential retraining. The model will be wrapped in a
fastapi API and build into a container with docker. The pipeline and the code
is built using OOP and tested with unittest.

## Intro
Customer turnover (churn) is the rate at which customers cease to be customers.
For companies, it is an important metric to track, as high churn rate can lead
to loss of revenue, damage reputations and lower employee morale.
Addiditionally, gaining a new customer is much more expensive than retaining an
existing one. For these reasons, companies are motivated to investigate which
customer is likely to churn. If high risk customers can be identified before
leaving the company, companies can proactively adress them with tailored
interventions to increase their customer satisfaction.

This repo explores telecommunications data in order to analyze demographic and
operational variables and their influence on the customers proclivity to churn.
The following questions will be investigated:
- which variables are predictive of churn?
- what is the distribution of churn generally and in relationship to the
independent variables?
- are there products that perform particularly well/bad with regards to churn
and overall profitability?

After the main features are identified, classification models are trained and
selected models packaged with fastapi and docker to do on demand predictions in
production environments.

<!-- ## Results -->
<!---->
<!-- To see results of the analysis, see the exploration.py file. -->
<!---->
<!-- ## Installation and Usage -->
<!---->
<!-- Ensure you have docker installed. -->
<!-- Open a terminal and clone the repository -->
<!---->
<!-- ```{bash} -->
<!-- #git clone https: -->
<!-- cd  -->
<!-- ``` -->
<!---->
<!-- Run the analysis.py file or build directly from the pkl file. -->
<!---->
<!-- ```{bash} -->
<!-- docker build -t image name -->
<!-- ``` -->
<!---->
<!-- Run the container and execute the send_test_data.py script -->
<!-- ```{bash} -->
<!-- docker run --rm image_name -->
<!-- ``` -->
<!---->

Based on dataset acquired from Kaggle

