#Alex King
#Encrypts the message.txt file
#using the public_key.txt
#

from KeyGenerator import power

	


#Message--------------------------------
#Asks for message
message = open('message.txt','r')
m = message.read()
message.close()
m = m.rstrip()
m = int(m)
print("The message is", m)
#---------------------------------------
#Asks for the public_key
pub = open('public_key.txt', 'r')
pkey = pub.read()
#grabs e and n from the text
e , n = pkey.split(" ")
e = e.rstrip()
n = n.rstrip()
e = int(e)
n = int(n)
pub.close()

#Encrypting------------------------------
c =  power(m,e,n)
print("Ciphertext is",c)
#writes to file
ciphertext = open("ciphertext.txt","w")
ciphertext.write(str(c))
