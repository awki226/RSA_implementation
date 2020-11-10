#Author: Alex King
#This module decrypts the cipher text
# using private key and public key
#

from KeyGenerator import power

	


#Cipher--------------------------------
#Asks for cipher
cipher = open('ciphertext.txt','r')
c = cipher.read()
cipher.close()
c = c.rstrip()
c= int(c)
print("The cipher is", c)

#Getting n from public key--------------
#Asks for the public_key
pub = open('public_key.txt', 'r')
pkey = pub.read()
e , n = pkey.split(" ")
n = n.rstrip()
n = int(n)
pub.close()

#Getting d from private key-------------
#asks for the private_key
pri = open('private_key.txt', 'r')
d = pri.read() 
d = d.rstrip()
d = int(d)

#Decrypting------------------------------
m =  power(c,d,n)
print("plaintext is", m)
#writes to file
plain = open("decrypted_message.txt","w")
plain.write(str(m))
