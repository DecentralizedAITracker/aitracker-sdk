import keypair  from 'keypair';
import * as fs from 'fs';
import JSEncrypt from 'jsencrypt'
import { promises as fsAsync } from "fs"
import EncryptRsa from 'encrypt-rsa';
var forge = require('node-forge');
let QuickEncrypt = require('quick-encrypt')

let pair = keypair();
//console.log(pair.public.toString());

/*
fs.writeFile('public_key_web.pem', pair.public.toString(), err => {
    if (err) {
      console.error(err);
    }
    // file written successfully
  });

  fs.writeFile('private_key_web.pem', pair.private.toString(), err => {
    if (err) {
      console.error(err);
    }
    // file written successfully
  });

*/
  let main = async () => {
    let data = await fsAsync.readFile("encrypted.txt", "ascii");
    let privateKey = await fsAsync.readFile('keys/private_key_web.pem','utf8')
    //console.log(privateKey)

    //var rsa = forge.pki.

    //var decrypted = privateKey.decrypt(data);
}

main()