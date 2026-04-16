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
	conn=connect()
	cur=conn.cursor()

	email=input("E-mail: ")
	password=hash_passowrd(input("Password: "))

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

	email=input("Enter E-mail: ")
	cur.execute("SELECT user_id FROM users WHERE email=%s",(email,))
	user=cur.fetchone()

	if not user:
		print("E-mail not found.")
		conn.close()
		return
	
	new_pass=hash_passowrd(input("Enter new password: "))
	cur.execute("UPDATE users SET password=%s WHERE email=%s", (new_pass, email))

	conn.commit()
	print("password updated successfully.")
	conn.close()