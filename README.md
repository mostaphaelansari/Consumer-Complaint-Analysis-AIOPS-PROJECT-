# Consumer Complaint Analysis AIOPS Project

## Overview
This project develops a scalable machine learning pipeline to predict whether a consumer complaint will be disputed. It leverages the Consumer Financial Protection Bureau's complaints dataset and incorporates various data science and machine learning techniques for accurate predictions.

## Installation

### Prerequisites
- Python 3.8+
- pip and virtualenv

### Setup
1. Clone this repository:

         git clone https://github.com/mostapha.elansari/Consumer-Complaint-Analysis-AIOPS-PROJECT.git

3. Navigate to the project directory:

         cd Consumer-Complaint-Analysis-AIOPS-PROJECT

virtualenv venv
      
      source venv/bin/activate # On Windows use venv\Scripts\activate

4. Install the dependencies: 

            pip install -r requirements.txt


## Usage
- To conduct exploratory data analysis, open the `EDA (AIOPS_PROJECT).ipynb` notebook in the `notebook/` directory with Jupyter Notebook or JupyterLab.
- To run the training pipeline, execute the following command:

      python -m src.pipeline.train_pipeline
  



