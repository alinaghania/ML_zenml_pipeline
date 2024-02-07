# ML Pipeline Project

## Introduction

This project utilizes ZenML for creating a streamlined Machine Learning (ML) pipeline, incorporating features such as environment setup, library installation, project initialization, pipeline execution, dashboard visualization, data updating, and automated data monitoring. It aims to simplify ML workflows, ensuring efficient data integration and management.

## Table of Contents

- [Introduction](#introduction)
- [Environment Setup](#environment-setup)
- [Installation](#installation)
- [Project Initialization](#project-initialization)
- [Executing the Pipeline](#executing-the-pipeline)
- [Dashboard](#dashboard)
- [Updating Data](#updating-data)
- [Automated Data Monitoring](#automated-data-monitoring)
- [Troubleshooting](#troubleshooting)
- [Dependencies](#dependencies)

## Environment Setup

```bash
# Create a virtual environment
pyenv virtualenv 3.8.12 pipeline

# Activate the virtual environment
pyenv activate pipeline
````


## Installation

```
# Install ZenML and its server extension
pip install "zenml[server]"
```

## Project Initialization


```

zenml init 
```

## Executing the Pipeline


```
python run_pipeline.py

# If the above fails, disconnect ZenML and retry
zenml disconnect
python run_pipeline.py
```

## Dashboard

```
# Access the ZenML dashboard
zenml up
```

## Updating Data
To update the data for your pipeline, simply change the path in the run_pipeline.py file to the new data location.

## Automated Data Monitoring
This feature uses watch_data_folder.py for real-time data monitoring. It automatically triggers pipeline execution upon detecting new data in the specified directory.

##Setting Up the Monitoring Script
Ensure watch_dat a_folder.py is configured with your data directory's path.


## Executing the Monitoring Script

```
# Run the script in the background to continuously monitor for new data
nohup python watch_data_folder.py &

```

## Troubleshooting
If you encounter any issues:

## Ensure your virtual environment is activated and correctly set up.
Confirm the ZenML library and its dependencies are correctly installed.
Use zenml disconnect followed by python run_pipeline.py if pipeline execution fails.
Dependencies
Python 3.8.12
ZenML
Watchdog (for automated data monitoring)

Thank you :) 