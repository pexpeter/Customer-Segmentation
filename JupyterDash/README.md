# Jupyter Dash:  Credit Clustering USA Survey (2019) with KMeans Model

[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)](https://jupyter.org/) [![Dash](https://img.shields.io/badge/Dash-Plotly-blue?style=flat&logo=plotly)](https://plotly.com/dash/) [![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)](https://www.python.org/) [![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-blueviolet?style=flat&logo=scikit-learn)](https://scikit-learn.org/)

## Introduction

This project showcases an interactive dashboard created using Jupyter Dash to analyze the USA Survey data from 2019. The dashboard provides insights into household features variance and performs K-Means clustering on the dataset. The objective is to explore and understand the survey data in an intuitive and interactive manner.

## Getting Started

To run this project, you need to have Jupyter Dash installed. Clone the repository and open the [Jupyter Dash app file](app.py). Ensure that the required packages mentioned in the previous sections are installed in your Python environment.

The dataset used in this project should be named "survey_data_2019.csv" and placed in the same directory as the Jupyter Notebook file.

## Dashboard Layout

The Jupyter Dash application consists of the following components:

- **Title**: The dashboard starts with a title displaying "USA SURVEY (2019) HOUSEHOLD ANALYSIS".

- **Features Variance**: This section displays a bar chart showing the variance of different features in the dataset. There is a radio button allowing you to switch between trimmed and non-trimmed variance calculation.

- **K-Means Clustering**: This section includes the following components:
  - "Number of Clusters [k]" Slider: You can adjust the number of clusters (k) using this slider, which ranges from 2 to 12.
  - "Metrics" Output: The inertia and silhouette score metrics for the selected clustering configuration are displayed here.
  - "PCA Scatter Plot" Graph: This scatter plot visualizes the clusters' representation in the Principal Component Analysis (PCA) space.

## Running the Dashboard

To run the Jupyter Dash application, execute the provided code for the [app](app.py). The application will launch a web server, and you can access the dashboard by opening the displayed URL in your web browser. The dashboard will be interactive, allowing you to explore the dataset and analyze the survey data using the provided features.

## Acknowledgments

- The dataset used in this project was sourced from [federal reserve archive](https://www.federalreserve.gov/econres/files/scfp2019excel.zip).
- The Jupyter Dash framework is used for creating the interactive dashboard.
- Data analysis and visualization are performed using the Plotly Express library.

For any improvement don't fail to reach out through.

- [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/pexpeterr.svg?style=social&label=Follow%20%40pexpeterr)](https://twitter.com/pexpeterr)

- [![Gmail URL](https://img.shields.io/badge/Connect%20with-Gmail-red.svg?style=flat&logo=gmail)](mailto:peterkgathoni@gmail.com)

- [![Medium URL](https://img.shields.io/badge/Follow%20%40peterkgathoni-%2312100E.svg?style=flat&logo=medium)](https://medium.com/@peterkgathoni)

- [![LinkedIn URL](https://img.shields.io/badge/Connect%20with%20Me-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/peterkamaugathoni)
