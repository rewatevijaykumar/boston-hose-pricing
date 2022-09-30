### Boston House Pricing Prediction

### Software and Tools Requirements

1. [Github Account](https://github.com)
2. [RailwayAccount](https://railway.app)
3. [VSCodeIDE](https://code.visualstudio.com)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


Create a new environment

```
conda create -p venv python==3.7 -y
```

Activate new environment

```
conda activate venv/
```

Install required libraries

```
pip install -r requirements.txt
```


Sample Test Data for API
```
{
  "data":{
    "CRIM": 1,
    "ZN": 18,
    "INDUS": 2.5,
    "CHAS": 0.0,
    "NOX": 0.6,
    "RM": 4.0,
    "AGE": 25.0,
    "DIS": 2.0,
    "RAD": 1.0,
    "TAX": 295,
    "PTRATIO": 10.5,
    "B": 350.00,
    "LSTAT": 3.5
  }
}
```