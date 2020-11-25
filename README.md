
_Note: currently settings (urls, passwords) are stored in `settings.py` just for the sake of convenience.
 A better approach would be to pass this information as environmental variables or command line arguments._

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

## Installation

### For development / testing

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

### Installation for usage