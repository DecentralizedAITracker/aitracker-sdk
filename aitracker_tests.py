from aitracker_ml import AITrackerML
from aitracker_oracle import AITrackerOracle
import json

if __name__ == '__main__':
    print("online")
    ait_ml = AITrackerML('keys/public_key_oracle.pem','keys/private_key_ml.pem','keys/public_key_web.pem')
    ait_oracle = AITrackerOracle('keys/public_key_ml.pem','keys/private_key_oracle.pem')

    #encryption test
    message = 'does it work'
    message_encrypted = ait_ml.encrypt(message)

    #encrypt web
    message_encrypted = ait_ml.encrypt_for_user(message)
    print(type(message_encrypted))
    f_web = open('encrypted.txt', 'w')
    f_web.write(message_encrypted)
    f_web.close()

    #encode to json and decode test
    message_object = {
        'prediction' : message_encrypted
    }
    message_json_string = json.dumps(message_object)
    message_object_loaded = json.loads(message_json_string)
    message_from_json = message_object_loaded['prediction']

    #decryption test
    message_decrypted = ait_oracle.decrypt(message_from_json)
    print(message_decrypted)

    #signing test
    signature = ait_ml.sign(message_json_string)

    #encode to json and decode test
    signature_object = {
        'signature' : signature
    }

    signature_json_string = json.dumps(message_object)
    signature_object_loaded = json.loads(message_json_string)
    signature_from_json = message_object_loaded['prediction']
    #verifying test
    verified = ait_oracle.verify('test',signature_from_json)
    print(verified) #false

    verified = ait_oracle.verify(message_json_string,signature)
    print(verified) #true

