# **ML PIPELINE**

##### Create an environement 


```
pyenv virtualenv 3.8.12 pipeline
```

```
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


#### Automated Data Monitoring
This project includes a data monitoring script (watch_data_folder.py) that automatically detects new data in a specified directory and triggers the pipeline execution.

Setting Up the Monitoring Script
- Ensure the watch_data_folder.py script is correctly set up with the path to your data directory.

Execute the monitoring script, This will run the script in the background, continuing even if the terminal is closed :

```
nohup python watch_data_folder.py &
```

How It Works ? :

The script uses watchdog to monitor changes in the data directory. When a new file is detected, it executes run_pipeline.py with the path of the new data file as an argument, thereby triggering the pipeline.