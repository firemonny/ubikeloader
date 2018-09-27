# Taipei Ubike data Saver
# Data is from "http://data.taipei/youbike"
# Under liscense "https://data.taipei/rule/rule"

## Start

1.  Create your python virtual environment

```bash
$ sudo apt-get install python3-venv
$ python3 -m venv venv
```

2.  Use your virtual environment

```bash
$ source venv/bin/activate
```

3.  Install dependent python package

```bash
$ python3 -m pip install -r requirements.txt
```

5.  Run the script for save data under `/ubike_data` folder

```bash
$ python3 ubike-saver.py
```

## Create Cron Jobs (This example is base on Ubuntu Linux system)

```bash
$ crontab -e
* * * * * /home/ubuntu/ubike/venv/bin/python /home/ubuntu/ubike/ubike-saver.py
```

## Check if the python is hanging

```bash
$ ps -ef | grep python
```

## Kill the process if the python programming is hanging
```bash
$ pkill python
```

## Authors

* **Nung-Shun (Monny) Chou** - [Firemonny](https://github.com/firemonny)
