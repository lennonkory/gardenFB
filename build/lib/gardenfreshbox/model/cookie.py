from operator import itemgetter
from Crypto.Cipher import AES
import json
import base64

class Cookie():
	
	def __init__(self):
		self.user_name = None
		self.password = None
		self.role = None

	def __init__(self,user_name,password,role):
		self.user_name = user_name
		self.password = password
		self.role = role

	def encryptCookie(self):
		dict = {'user_name' : self.user_name, 'password' :self.password, 'role' : self.role}
		return self.encrypt(json.dumps(dict))

	def encrypt(self, message):
		if(len(message)%16 != 0):
			r = 16 - (len(message)) % 16
			for i in range(0,r):
				message = message + ' '

		cipher = AES.new('449jgrj4ojagfkngkk f9y5c',AES.MODE_ECB)
		encoded = base64.b64encode(cipher.encrypt(message))
		return encoded

	@staticmethod
	def decryptCookie(cookie):
		return json.loads(Cookie.decrypt(cookie))

	@staticmethod
	def decrypt(text):
		cipher = AES.new('449jgrj4ojagfkngkk f9y5c',AES.MODE_ECB)
		decode = cipher.decrypt(base64.b64decode(text))
		return decode
