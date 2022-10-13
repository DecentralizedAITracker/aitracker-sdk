# AI Tracker SDK

This is a set of software made for easy encryption,decryption, signning and verifying messages sent from the machine learning dapp to the oracle dapp.

## How to use it

### Initialize keys
First you need to generate the keys for the oracle and ml dapp.
```
python aitracker_initkeys.py
```
### Copy files
There are 4 keys generated. Copy public_key_oracle and private_key_ml to the machine learning dapp. Copy public_key_ml and private_key_oracle to the oracle dapp.
### The ml dapp
The ml dapp should recieve a rsa public key from the user. The ml dapp result need to be encrypted with the user public key and oracle public key. The ml dapp needs to run in tee mode
### The oracle dapp
The oracle recieves the dapp result encrypted and can decrypt it with its private key. The oracle should run in tee mode.
### The user
The front end should create rsa keys and send the public key to the ml dapp.