import rsa

if __name__ == '__main__':
    print("generating keys...")
    publicKeyML, privateKeyML = rsa.newkeys(2048)

    # Export public key in PKCS#1 format, PEM encoded 
    publicKeyMLPkcs1PEM = publicKeyML.save_pkcs1()
    f_ml_pub = open('keys/public_key_ml.pem', 'wb')
    f_ml_pub.write(publicKeyMLPkcs1PEM)
    f_ml_pub.close()
    # Export private key in PKCS#1 format, PEM encoded 
    privateKeyMLPkcs1PEM = privateKeyML.save_pkcs1()
    f_ml = open('keys/private_key_ml.pem', 'wb')
    f_ml.write(privateKeyMLPkcs1PEM)
    f_ml.close()

    publicKeyOracle, privateKeyOracle = rsa.newkeys(2048)
    # Export public key in PKCS#1 format, PEM encoded
    publicKeyOraclePkcs1PEM = publicKeyOracle.save_pkcs1()
    f_oracle_pub = open('keys/public_key_oracle.pem', 'wb')
    f_oracle_pub.write(publicKeyOraclePkcs1PEM)
    f_oracle_pub.close()
    # Export private key in PKCS#1 format, PEM encoded 
    privateKeyOraclePkcs1PEM = privateKeyOracle.save_pkcs1()
    f_oracle = open('keys/private_key_oracle.pem', 'wb')
    f_oracle.write(privateKeyOraclePkcs1PEM)
    f_oracle.close()
 