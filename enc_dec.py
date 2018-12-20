#intializing 
password_out=''
case_changer=ord('a')-ord('A')
encryption_key=(('a','m'),('b','h'),('c','t'),('d','f'),('e','g'),('f','k'),('g','b'),
	('h','p'),('i','j'),('j','w'),('k','e'),('l','r'),('m','q'),('n','s'),('o','l'),
	('p','n'),('q','i'),('r','u'),('s','o'),('t','x'),('u','z'),('v','y'),('w','v'),
	('x','d'),('y','c'),('z','a'))

print ('Python program to Encrypt and Decrypt password\n')

#select encrypt or decrypt
select=input('Enter (e) to encrypt a password / (d) to decrypt a password: ')
while select !='e' and select !='d':
	select=input('\nInvalid Entry - Enter (e) to encrypt a password / (d) to decrypt a password: ')
encrypting=(select=='e') #returns boolean value True/False

#get password
password_in=input('Enter password: ')

#start encrytion / decryption
if encrypting:
	from_index=0
	to_index=1
else:
	from_index=1
	to_index=0

#encrytion/decrytion actual logic begins here
for ch in password_in:
	letter_found=False

	for t in encryption_key:
		if('a'<=ch and ch<='z') and ch==t[from_index]:
			password_out=password_out + t[to_index]
			letter_found=True

		elif('A'<=ch and ch<='z') and chr(ord(ch)+32)==t[from_index]:
			password_out=password_out + chr(ord(t[to_index]) - case_changer)
			letter_found=True

	if not letter_found:
		password_out=password_out+ch

#printing output
if encrypting:
	print ('Your encrypted password is: ',password_out)
else:
	print ('Your encrypted password is: ',password_out)
