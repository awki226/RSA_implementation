# Author: Alex King
# Purpose: RSA cryptosystem implementation
# Date: 04-22-2020
# Course: CS 378

import random

#-------------------------------------------
#This is the extended Euler's extended algorithim
#Uses a recursive method to implement the EEA
#referenced pseduocode from this lecture
#https://www.csee.umbc.edu/~chang/cs203.s09/exteuclid.shtml
def extendEul(x,y):
	if x == 0:
		#This is our base case
		return y, 0, 1
	else:
		#Does y mod x 
		a = y % x
		#recursive step
		alpha, d, c = extendEul(a,x)
		#using the floor operator is faster than using math.ceil()
		b = c - (y // x) * d
		return alpha, b, d
#-------------------------------------------
#This is the Modular Inversion function 
#It utilizes the Euler extended algorithim
def mod_Inv(x,y):
	#calls our Euler function b is the only
	#value that won't be used in our function
	alpha, a, b = extendEul(x,y)
	
	#case if the modular inverse doesn't exist
	if alpha != 1:
		print("modular inverse DNE")
	else:
		return a % y
#--------------------------------------------
#The modular power function used for the 
#Uses the modular exponention method
#Uses bitwise operations as well to 
#speed up arthimtic
#Used https://en.wikipedia.org/wiki/Modular_exponentiation
#for Pseduocode
#miller-Rabin
#Encrption and Decrption method
def power(x,y,n):
	#alpha stores the results
	#due to modular exp
	alpha = 1

	x = x % n
	#Goes through until y has been
	#bit shifted to 0
	while y > 0:
		#determines if the last bit is 1 for y
		#to see if odd, faster than y % 2 != 0  
		if (y & 1 == 1):
			#alpha = alphax(modn)
			alpha = (alpha * x) % n
		
		x = (x * x) % n
		#y >> 1 is the same as divided by 
		# (2^1)^n, n is the loop iteration
		#y is now even 
		y = y>>1
	return alpha
#--------------------------------------------
# The function below is the 
# miller-Rabin test for determining primality
# Usually k is choosen for the number of trials
# K = 10 I have chossen to be safe in this case
# Uses the given odd value m, and n
def miller_Rabin(m, n): 
	# Pick a random number btw 1 and n -1  
	a = random.randint(1, n - 1)
	
	# b = a^m % n 
	b = power(a, m, n)
	
	#nontrival factor case 
	if (b == n - 1 or b == 1): 
		return True 
	
	#Using Chapter 6 format
    	# for the loop
	while (m != n - 1):
		b = power(b,b,n)
		m = m * 2 
		if (b == n - 1):
			#prime case 
            		return False
		if (b == 1):
			#composite case
			return True 

	#composite case since
	#odd case wasn't reached in the loop 
	return False 
#----------------------------------------
#isPrime(n) is a helper function for the 
#miller_Rabin function and does the k#
#loops for miller_Rabin
def isPrime(n): 
    # First half finds m using n     
    # n-1 = 2^k * m 
    m = n - 1;

    #This loop makes sure m is odd by using
    #floor division and checking if last bit = 0 
    while (m & 1 == 0): 
        m = m//2 
    
    #Typically k but k = 10 in this case
    for i in range(10): 
	#case if n is composite
        if (miller_Rabin(m, n) != True): 
            return False

    return True 
#---------------------------------------
# This function generates p & q which are large primes
# From 10^99 - 10^200 making sure the difference is > 10^95
def large_Prime():
	#generates p & q as prime numbers
	#uses 10^99 as the base since it's the smallest 100 digit number
	#sys.maxval ran into issues so 10 ** 100 works just as well
	p = random.randint((10 ** 99),(10 ** 200))
	while not isPrime(p):
		p = random.randint((10**99),(10 ** 200))	
	
	
	q = random.randint((10 ** 99),(10 ** 200))
	#checks to see if the differance is greater than 10^95)
	while not isPrime(q):
		q = random.randint((10 ** 99), (10 ** 200))	
	
	#Generates p and q until prime
	#Case where the differance is less than 10^95
	while abs(p - q) < (10 ** 95):
		#print("OUT OF RANGE")
		while not isPrime(q):
			#print("NOT PRIME Q")
			q = random.randint((10 ** 99), (10 ** 200))

	return(p,q)
#------------------------------------------
#Main function does encryption and decryption
#Generates n using p and q
if __name__ == "__main__" :
	#generates two primes with 100 digits each
	p,q =large_Prime()
	n = p * q
	
	#print(p)
	#print("\n",q)
	#Euler's toitent of n
	phi = (p-1)*(q-1)
	
	
	#Public key-------------------------------
	#checks to see if e is coPrime with phi
	e = (2 ** 16) +1
	coPrime, a, b = extendEul(e,phi)
	
	#This loop makes sure that the value of e is
	#co prime
	while coPrime != 1:
		e = e + 3
		coPrime = math.gcd(e,phi)
	public_key = open('public_key.txt','w')
	pub = str(e) + " " + str(n)
	public_key.write(pub)
	public_key.close()

	#Private key-----------------------------
	#does the modular inverse for and phi 
	d = mod_Inv(e,phi)
	private_key = open('private_key.txt','w')
	priv = str(d)
	private_key.write(priv)
	private_key.close()
