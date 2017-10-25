# Route53 Dead Domain Finder

## Requirements

 - Python 2 or 3
 - virtualenvwrapper


## Setting Up Environment

```bash
mkvirtualenv route53-dead-domain-finder
pip install -r requirements/development.txt
```


## Usage

```bash
cp config.json.dist config.json
vi config.json
python ./run.py find --config=config.json
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
