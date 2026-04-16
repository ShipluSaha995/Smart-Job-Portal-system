import hashlib
from db import connect

def hash_passowrd(p):
	return hashlib.sha256(p.encode()).hexdigest()

def register():
	conn=connect()
	cur=conn.cursor()

	print("\n 1.Employer\n2. Applicant")
	role="employer" if input("Chooose: ")=="1" else "applicant"

	name= input("Name: ")
	email=input("E-mail: ")
	password=hash_passowrd(input("Password: "))

	try:
		cur.execute(
			"INSERT INTO users(name, email, password, role) VALUES(%s,%s,%s,%s)",
			(name, email, password, role)
		)
		conn.commit()
		print("Account Created Successfully.")
	except:
		print("Email Already exists.")
	conn.close()

def login():
	pass

def reset_password():
	pass 