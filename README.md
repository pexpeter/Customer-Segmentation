# Credit Clustering with KMeans Model and Jupyter Dash

[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)](https://jupyter.org/) [![Dash](https://img.shields.io/badge/Dash-Plotly-blue?style=flat&logo=plotly)](https://plotly.com/dash/) [![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)](https://www.python.org/) [![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-blueviolet?style=flat&logo=scikit-learn)](https://scikit-learn.org/)

## TABLE OF CONTENTS

----

- [Introduction](#introduction)
  - [Objectives](#objectives)

----

- [Workflow](#workflow)

----

- [Getting Started](#getting-started)

----

- [Acknowledgments](#acknowledgments)

----

## Introduction

This project aims to cluster credit data using the KMeans model and visualize the results using Jupyter Dash. The dataset used in this project is the US Survey Data from 2019.

### Objectives

1. Identify columns or features with large variances.
2. Perform data processing using the trimmed variance method to handle outliers.
3. Build an unsupervised model to cluster credit unworthy individuals or those at risk of credit decline.
4. Create centroids for the different clusters.
5. Visualize the clusters using Principal Component Analysis (PCA) in Jupyter Dash.

## Workflow

The project follows the following workflow:

1. Importing Packages: This section imports the necessary packages and libraries for data analysis, visualization, and Jupyter Dash.
2. Data Import and Cleaning: The 2019 Survey dataset is imported, and initial cleaning operations are performed.
3. Exploratory Data Analysis (EDA): This section explores the dataset, examines its shape and characteristics, and prepares the data for clustering.
4. KMeans Clustering: The KMeans model is applied to the preprocessed data to cluster credit unworthy individuals.
5. Centroid Creation: Centroids are generated for each cluster.
6. Visualization with Jupyter Dash: The clusters are visualized using Principal Component Analysis (PCA) within a Jupyter Dash application.

## Getting Started

To run this project, you need to have Jupyter Notebook and Jupyter Dash installed. Clone the repository and open the Jupyter Notebook file (.ipynb) in your Jupyter environment. Ensure that the required packages mentioned in the "Importing Packages" section are installed in your Python environment.

The [dataset](Data/SCFP2019.csv) used in this project should be named "SCFP2019.csv" and placed in the data folder.

To launch the Jupyter Dash application, execute the provided code in the [Jupyter Dash](JupyterDash/app.py). The application will launch a web server, and you can access the dashboard by opening the displayed URL in your web browser. The dashboard will be interactive, allowing you to explore the dataset and analyze the credit clusters using the provided features.

## Acknowledgments

- The 2019 Survey dataset used in this project was sourced from [federal reserve source](https://www.federalreserve.gov/econres/files/scfp2019excel.zip).
- The KMeans algorithm is implemented using the scikit-learn library.
- Principal Component Analysis (PCA) is performed using the scikit-learn library.
- Jupyter Dash is used for creating the interactive dashboard.

For any improvement don't fail to reach out through.

- [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/pexpeterr.svg?style=social&label=Follow%20%40pexpeterr)](https://twitter.com/pexpeterr)

- [![Gmail URL](https://img.shields.io/badge/Connect%20with-Gmail-red.svg?style=flat&logo=gmail)](mailto:peterkgathoni@gmail.com)

- [![Medium URL](https://img.shields.io/badge/Follow%20%40peterkgathoni-%2312100E.svg?style=flat&logo=medium)](https://medium.com/@peterkgathoni)

- [![LinkedIn URL](https://img.shields.io/badge/Connect%20with%20Me-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/peterkamaugathoni)
