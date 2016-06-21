# Route53 Dead Domain Finder

## Development

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements/development.txt
```


## Usage

```
cp config.json.dist config.json
vi config.json
./run.py find --config=config.json
```


## Config
```
[
    {
        "name": "Business",
        "access_key_id": "AKIA1122222",
        "secret_access_key": "78N90K73425g54t546t4"
    },
    {
        "name": "Personal",
        "access_key_id": "AKIAIFBG65464",
        "secret_access_key": "78N9FDSGDGJ897987HHYB8HJB876"
    }
]
```

IAM users need read Route53 permissions