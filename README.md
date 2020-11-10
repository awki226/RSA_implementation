# RSA_implementation
How to compile in order:
	
	$python3 keyGenerator.py
	$python3 Encrypted.py
	$python3 Decrypted.py
	
In this program, I created three modules to implement the RSA cryptosystem: A key generator, encryption module, and a decryption module. The Key generator has all of the functions/algorithms implemented for the other two modules. The Functions I used in generating the public and private keys for the RSA cryptosystem where that of 
	
	extendEul(x,y)
	power(x,y)
	mod_Inv(x,y)
	miller_Rabin(m, n)
	isPrime(n)
	large_Prime()
	
I will discuss the process of generating the public and private keys. The project requires the
private key and a public key in order to encrypt and decrypt a message, in order to do the RSA algorithm you need a large number say n. n must consist of two large primes p and q. In my program I use the function large_Prime() to do this. This function returns two primes that are greater than 10^99  and more than 10^95  apart from each other. I used while loops that made sure of this cases for p & q. This loops generate random numbers using randint(10^99,10^200), then calling the function isPrime(n) to return a boolean value to make sure the loop exited once prime. The isPrime(n) is a helper function for the 
miller_Rabin(m,n) function. It first determines the value m used in the miller-Rabin equation

	n-1 ≡2^k m ,where m is odd

 To find m I used the bitwise method of checking if the last bit was 0, if so I used floor division of 2 to see if it was odd. From here I used a for loop of 10, for the value of k. This loop calls miller_Rabin(m,n). The reason I chose Miller-Rabin over Fermat’s primiality test is that, Miller-Rabin is much more accurate which was a determining factor when you have to do this operation on such large numbers. Within miller-Rabin I first calculated the number a which is a random integer from 2 to n -1. Next I used the power(x,y,n) to calculate the initial value of b for the miller-Rabin test

	b_0  ≡a^m (mod n)

The power function performs the modular power via  modular exponentiation, I used the shift operator by 1 to achieve this since it is just 〖2^1〗^n  ,n being my loop iteration. This ends the method of getting the large Prime numbers. To check to see if these were correct, I double checked this by using a large prime number checker online. After I got p & q I calculated n, then phi of n using (p-1) * (q-1).  Using my extendEul(x,y)to find the GCD of phi and e, e was set to 2^16 - 1. I had set up a conditional loop to make sure that the GCD was 1. The extendEul(x,y) function implements the extended Euclidian algorithm for calculating the GCD. Once that is found I used the mod_inv(m,n) to calculate the modular inverse between e and phi to find the private key. The modular inverse function utilizes the ExtendEul(x,y) to find the mod inverse. From the public key pair gets written to a file, and the public key gets written to a file. 

The Encrpyted.py file reads the message.txt file, and the public_key.txt file to this module using the encryption function c=m^e (mod n), this is done using the power function mentioned earlier. C is then written out to a file called ciphertext.txt
	
The Decrypted.py file reads the cipher.txt file, public key and the private_key.txt to this module using the decryption function m=c^d (mod n), this is done with using the power function mentioned earlier. M is then written out to decryptedtext.txt

The slowest part of this algorithm is generating the primes since they are so large, the range for the randint() function takes awhile.
