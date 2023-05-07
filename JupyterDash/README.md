# Jupyter Dash: USA Survey (2019) Household Analysis

This project showcases an interactive dashboard created using Jupyter Dash to analyze the USA Survey data from 2019. The dashboard provides insights into household features variance and performs K-Means clustering on the dataset. The objective is to explore and understand the survey data in an intuitive and interactive manner.

## Getting Started

To run this project, you need to have Jupyter Notebook installed. Clone the repository and open the Jupyter Notebook file (.ipynb) in your Jupyter environment. Ensure that the required packages mentioned in the previous sections are installed in your Python environment.

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

To run the Jupyter Dash application, execute the provided code in the Jupyter Notebook. The application will launch a web server, and you can access the dashboard by opening the displayed URL in your web browser. The dashboard will be interactive, allowing you to explore the dataset and analyze the survey data using the provided features.

## Acknowledgments

- The dataset used in this project was sourced from [source_name].
- The Jupyter Dash framework is used for creating the interactive dashboard.
- Data analysis and visualization are performed using the Plotly Express library.

Please refer to the Jupyter Notebook file for the complete code implementation and further details.


