import hashlib
from db import connect

def hash_passowrd(p):
	return hashlib.sha256(p.encode()).hexdigest()

def register():
	conn=connect()
	cur=conn.cursor()

	print("\n\t\t\t\t\t1. Employer\n\t\t\t\t\t2. Applicant")
	role="employer" if input("\n\t\t\t\tChooose: ")=="1" else "applicant"

	name= input("\t\t\t\tName: ")
	email=input("\t\t\t\tE-mail: ")
	password=hash_passowrd(input("\t\t\t\tPassword: "))

	try:
		cur.execute(
			"INSERT INTO users(name, email, password, role) VALUES(%s,%s,%s,%s)",
			(name, email, password, role)
		)
		conn.commit()
		print("\n\t\t\t\t====Account Created Successfully.======\n")
		print("____________________________________________________________________________________________________________________________________________________________\n")
	except:
		print("\t\t\t\t_____________________")
		print("\t\t\t\tEmail Already exists.")
		print("\t\t\t\t_____________________")
	conn.close()

def login():
	conn=connect()
	cur=conn.cursor()

	email=input("\n\t\t\t\tE-mail: ")
	password=hash_passowrd(input("\t\t\t\tPassword: "))

	cur.execute(
		"SELECT user_id, role FROM users WHERE email=%s AND password=%s",
		(email, password)
	)

	user=cur.fetchone()
	conn.close()
	return user

def reset_password():
	conn=connect()
	cur=conn.cursor()

	email=input("\t\t\t\tEnter E-mail: ")
	cur.execute("SELECT user_id FROM users WHERE email=%s",(email,))
	user=cur.fetchone()

	if not user:
		print("\t\t\t\t!!!E-mail not found.!!!")
		conn.close()
		return
	
	new_pass=hash_passowrd(input("\t\t\t\tEnter new password: "))
	cur.execute("UPDATE users SET password=%s WHERE email=%s", (new_pass, email))

	conn.commit()
	print("\n\t\t\t\t=====password updated successfully.======")
	conn.close()