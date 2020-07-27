# input passwords
#create hash password
# looking for leak
#print output


import requests
import hashlib
import sys

#This function requests the API for password database which match the hash head of our password  
def request_api_for_data(hash_head):                             
	url = 'https://api.pwnedpasswords.com/range/' + hash_head
	re = requests.get(url)
	# print(re.text)
	if re.status_code == requests.codes.ok:
	#	print(f'API is working fine')
		re.raise_for_status()
	return re

#This function loops through the API data to match hash_tail of the password 
def hash_tail_check_APIdata(hashed_APIdata,hash_to_check):
	hashed_APIdata = (line.split(':') for line in hashed_APIdata.text.splitlines())
	for h, count in hashed_APIdata:
		if h == hash_to_check:
			return count
	return 0

#Generate Hashed paassword
def sha1password_creater(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	hash_head, hash_tail = sha1password[:5], sha1password[5:]
	# print(hash_head,hash_tail)
	response = request_api_for_data(hash_head)
	return hash_tail_check_APIdata(response, hash_tail)

def main(args):
	for password in args:
		count = sha1password_creater(password)
		if count:
			print(f'your password {password} was found {count} times...you should probably change your password')
		else:
			print(f'your password {password} is secure')
	return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

			



