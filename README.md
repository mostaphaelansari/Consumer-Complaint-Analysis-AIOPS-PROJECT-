﻿# Consumer-Complaint-Analysis-AIOPS-PROJECT-

Project Overview
This project aims to design and build a scalable machine learning pipeline to predict whether a consumer complaint will be disputed or not. The pipeline will be deployed on a cloud platform and exposed as an API for easy access. The project also includes integration with an online MySQL database for metadata storage, logging of actions performed by the code, and optimization of the solution at both the code and architecture levels.

Dataset
The dataset used for this project is available from the Consumer Financial Protection Bureau (CFPB) website. You can download the dataset in either CSV or JSON format from the following links:

Download CSV : https://files.consumerfinance.gov/ccdb/complaints.csv.zip
Download JSON : https://files.consumerfinance.gov/ccdb/complaints.json.zip

├── data/                          # Folder for storing dataset files
│   └── complaints.csv             # CSV dataset file
├── models/                        # Folder for storing trained models
│   └── model.pkl                  # Trained machine learning model
├── notebooks/                     # Folder for Jupyter notebooks (if any)
│   └── exploratory_analysis.ipynb # Jupyter notebook for exploratory data analysis
├── src/                           # Source code directory
│   ├── data_processing.py         # Code for data preprocessing
│   ├── model_training.py          # Code for training the machine learning model
│   ├── model_evaluation.py        # Code for evaluating model performance
│   ├── api.py                     # Flask API code for serving the model
│   └── logging_config.py          # Configuration file for logging
├── requirements.txt               # File containing Python dependencies
├── README.md                      # This file


