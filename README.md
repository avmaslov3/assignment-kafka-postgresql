# Documentation

<img src="scheme.png" width=450>

## Installation for usage

- _Note: for security reasons all settings like password, host adress, etc. are accessed through environmental variables. Please activate them using `setenv.sh` - I will send it by e-mail._
- Also `service.cert, ca.pem, service.key` files are needed, paths to them are set in `setenv.sh`.

```
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/al31415/assignment-kafka-postgresql
```

download example files 

```
wget https://github.com/al31415/assignment-kafka-postgresql/raw/master/src/lib/examples/run_producer.py
wget https://github.com/al31415/assignment-kafka-postgresql/raw/master/src/lib/examples/run_consumer.py
```

set environmental variables

```
source setenv.sh
```

run producer and consumer

```
python3 run_producer.py https://docs.python.org/3/library/re.html --sleep_interval 1 --regexp "[a]{6}"
python3 run_consumer.py --sleep_interval 1
```


check out what is written into PostgreSQL

```
python3 -c "from lib import request_db; print(request_db('select * from metrics;'))" 
```


## Installation for local development / testing / debugging

In order to run tests repository should be cloned and editable installation should be done.

```
git clone https://github.com/al31415/assignment-kafka-postgresql.git
cd assignment-kafka-postgresql
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

Run tests on local machine

```
pytest
```

