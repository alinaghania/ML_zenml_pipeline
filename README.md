# ML Pipeline

## Introduction

This project provides a streamlined machine learning pipeline utilizing ZenML, an MLOps framework designed to simplify and manage ML workflows. It includes features for environment setup, library installation, project initialization, pipeline execution, dashboard visualization, data updating, and automated data monitoring.

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

To create a virtual environment for the project, use the following commands:

```bash
pyenv virtualenv 3.8.12 pipeline
pyenv activate pipeline

pyenv activate pipeline
```

##### Install zenml library 

```
pip install "zenml["server"]"
```

##### To initialize a zenml project

```
zenml init
```

##### To execute the pipeline (if it doesn't work run zenml disconnect)

```
python run_pipeline.py

```

##### Dashboard
```
zenml up
```

#### To Update the Data you juste have to change the path on the file "run_pipeline.py"

#### In case of any issues, you might want to disconnect ZenML and retry:

```
zenml disconnect
python run_pipeline.py
```


## Updating Data

To ensure your ML pipeline processes the latest data, update the data source path in the `run_pipeline.py` script. Modify the file to point to the new data location, enabling the pipeline to access and process the updated dataset.

## Automated Data Monitoring

The project is equipped with an automated data monitoring system, implemented through the `watch_data_folder.py` script. This system is designed to watch for new data in a predefined directory, automatically initiating the pipeline execution upon detecting new files.

### Setting Up the Monitoring Script

Before activating the monitoring script, confirm that `watch_data_folder.py` is correctly configured with the path to your designated data directory. This setup is crucial for ensuring the script accurately monitors the correct location for new data inputs.

### Executing the Monitoring Script

To run the monitoring script in the background, allowing it to continuously monitor for new data even when the terminal is closed, use the following command:

```bash
nohup python watch_data_folder.py &

```

## How It Works ? :

The script uses watchdog to monitor changes in the data directory. When a new file is detected, it executes run_pipeline.py with the path of the new data file as an argument, thereby triggering the pipeline.