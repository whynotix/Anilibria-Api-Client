# Anilibria-Api-Client (tests)\*


## Setup 

1. Create ```.env``` file
2. Copy from .env.example ```ANILIBRIA_API_TOKEN```
3. Get token by ```/accounts/users/auth/login``` method

## Run tests
```
pytest -q tests/methods/test_account.py -s  
```