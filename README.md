# **ML PIPELINE**

##### 1)Create an environement 


```
pyenv virtualenv 3.8.12 pipeline
```

```
pyenv activate pipeline
```

##### 2)Install zenml library 

```
pip install "zenml["server"]"
```

##### 3)To initialize a zenml project

```
zenml init
```

##### 4)To execute the pipeline 

```
python run_pipeline.py

```

##### 5)Dashboard
```
zenml up
```