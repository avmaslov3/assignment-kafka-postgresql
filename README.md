# Documentation

## Installation for usage

```
source setenv.sh
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/al31415/assignment-kafka-postgresql
python3 -c "from lib import checker; checker('https://www.python.org/')"
```

## Usage examples 

- Usage examples file `examples/usage_example.py`

See help on arguments

```
python3 src/lib/producer.py -h  
```

Database connection command from terminal

```
psql --host=pg-14bf6fb2-rus314-305c.aivencloud.com --port=29300 --username=avnadmin --dbname=metrics
```


## Installation for development / testing / debugging

Install dev version

```
git clone
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip install -e .
```

Run tests

```
pytest
```

