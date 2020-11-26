# Documentation

## Installation for usage

```
source setenv.sh
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
```


## Installation for development / testing / debugging

In order to run tests repository should be cloned and editable installation should be done.

```
git clone ...
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip install -e .
```

Run tests

```
pytest
```

