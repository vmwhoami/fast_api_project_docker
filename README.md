

### Show all python packages installed
```
pip3 list
```

### Build fastAPI environment, in this case was 'fastapienv' name you set!
```
python3 -m venv fastapienv
```

### Activate the environment, in this case

```
source fastapienv/bin/activate 
```

### To see what is inside the environment

```
pip list
```

### To deactivate the environment
```
deactvivate
```

### In the environment install fastAPI and uvicorn

```
pip install fastapi

pip install "uvicorn[standart]"
```

## How to check your python version:

```
python3 -m -pip --version
```


### Freeze requirments txt
```
 pip freeze > requirements.txt
```

 ### Run with Uvicorn command
 ```
 uvicorn books:app --reload
 ```


