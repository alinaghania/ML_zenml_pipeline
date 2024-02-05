# **ML PIPELINE**

##### Create an environement 


```
pyenv virtualenv 3.8.12 pipeline
```

```
pyenv activate pipeline
```

```
pip install "zenml["server"]"
```

##### To initialize a zenml project

```
zenml init
```

### To execute the pipeline 

```
python run_pipeline.py

```

#### Dashboard
```
zenml up
```