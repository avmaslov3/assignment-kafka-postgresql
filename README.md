
Database connection command

```
psql --host=pg-14bf6fb2-rus314-305c.aivencloud.com --port=29300 --username=avnadmin --dbname=metrics
```

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