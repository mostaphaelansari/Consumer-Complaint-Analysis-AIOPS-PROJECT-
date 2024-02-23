# Consumer-Complaint-Analysis-AIOPS-PROJECT-

Project Overview
This project aims to design and build a scalable machine learning pipeline to predict whether a consumer complaint will be disputed or not. The pipeline will be deployed on a cloud platform and exposed as an API for easy access. The project also includes integration with an online MySQL database for metadata storage, logging of actions performed by the code, and optimization of the solution at both the code and architecture levels.

Dataset
The dataset used for this project is available from the Consumer Financial Protection Bureau (CFPB) website. You can download the dataset in either CSV or JSON format from the following links:

    Download CSV : https://files.consumerfinance.gov/ccdb/complaints.csv.zip

    Download JSON : https://files.consumerfinance.gov/ccdb/complaints.json.zip


        Consumer-Complaint-Analysis-AIOPS-PROJECT-
    │   README.md                    # This README file
    │   requirements.txt             # Python dependencies
    │   .gitignore                   # Specifies intentionally untracked files
    │
    ├── data/                        # Directory for dataset storage
    │   └── complaints.csv           # Dataset file
    │
    ├── src/                         # Source code directory
    │   ├── data_processing.py       # Code for data preprocessing
    │   ├── model_training.py        # Code for model training
    │   ├── model_evaluation.py      # Code for model evaluation
    │   ├── api.py                   # Flask API for serving the model
    │   └── logging_config.py        # Configuration file for logging
    │
    ├── models/                      # Directory for storing trained models
    │   └── model.pkl                # Trained machine learning model
    │
    └── docs/                        # Directory for project documentation
    ├── HLD_document.pdf         # High-Level Design document
    ├── LLD_document.pdf         # Low-Level Design document
    └── wireframe.pdf            # System architecture wireframe document

