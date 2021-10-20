# Blockchain

## Overview
A proof of concept blockchain that I wrote to create Nigecoin, my own crypto coin / token. 

## Blocks
```python
{
	'index': <int>, # blockchain index
	'timestamp': <str>, # datetime timestamp
	'proof': <int>, #proof of work
	'previous_hash': <str>, # previous block hash
	'transactions': [<transactions>], # list of transactions
	'merkle_root': <str>, # root of transactional merkle tree
	'merkle_tree': [[<transactions>]],
}
```
## Transactions
```python
{
	'sender': <str>, # transaction sender
	'receiver': <str>, # transaction recipient
	'amount' <int>, # transaction amount
}
```

## Routing


`GET /mine_block`

`GET /get_chain`

`GET /is_valid`

`POST /add_transaction`

`POST /connect_node`

`GET /replace_chain`

## Run Locally

`export FLASK_APP=blockchain`

`flask run`