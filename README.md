# Jokes service
> Daily jokes for IOS


### Dependencies
* [Python 3.6](https://www.python.org/)
* [bottlepy](https://bottlepy.org/docs/dev/)

To connect to the database, you must pass the path to the settings file to the PropertyReader class. 
To do this, specify the parameter db "path" when starting the service.

Sample file:
```ini
host=localhost
database=jokes
user=user
password=pass
```

Example run service:
```python
python JokesServer.py -db "path"
```