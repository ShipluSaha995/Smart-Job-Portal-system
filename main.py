from auth import register, login, reset_password
from job import *
from application import *
from admin import *


def admin_menu():
    while True:
        print("Admin Menu: ")
        print("___________")
        print("\n\t\t\t\t1. Dashboard\n\t\t\t\t2. All Users\n\t\t\t\t3. All Jobs\n\t\t\t\t4. All applicatios\n\t\t\t\t5. MST\n\t\t\t\t6. Logout ")
        c=input("\n\t\t\t\tEnter Your Choice: ")

        if c=="1":
            dashboard()
        elif c=="2":
            view_all_users()
        elif c=="3":
            view_all_jobs()
        elif c=="4":
            view_all_applications()
        elif c=="5":
            show_mst()
        else:
            break


def employer_menu(uid):
    while True:
        print("Employer Menu: ")
        print("_______________")
        print("\n\t\t\t\t1. Post Job\n\t\t\t\t2. View Jobs\n\t\t\t\t3. View Applicants\n\t\t\t\t4. Logout")
        c=input("\n\t\t\t\tEnter Your Choice: ")

        if c=="1" :
            post_job(uid)
        elif c=="2":
            view_jobs()
        elif c=="3":
            view_applicants(int(input("Job ID: ")))
        else:
            break
        


def applicant_menu(uid):
    while True:
        print("Appplicant Menu: ")
        print("________________")
        print("\n\t\t\t\t1. View Jobs\n\t\t\t\t2. Apply\n\t\t\t\t3. Search\n\t\t\t\t4. Catagory\n\t\t\t\t5. Logout\n")
        c= input("\t\t\t\tEnter your choice: ")

        if c=="1":
            print("\nJobs: ")
            print("_______\n")
            view_jobs()
            print("\n")
        elif c=="2":
            apply_job(uid)
        elif c=="3":
            search_jobs()
        elif c=="4":
            search_by_category()
        else:
            break
            
        


while True:
    print("\n\t\t\t\t*****Smart Job Portal******")
    print("\t\t\t\t____________________________")
    print("\n\t\t\t\t1. Register\n\t\t\t\t2. Login\n\t\t\t\t3. Reset Password\n\t\t\t\t4. Exit")
    ch=input("\n\t\t\t\tEnter your choice: ")
    print("____________________________________________________________________________________________________________________________________________________________\n")

    if(ch=="1"):
        print("\n\t\t\t\tRegister: ")
        print("\t\t\t\t__________")
        register()
    elif(ch=="2"):
        print("\n\t\t\t\tLogin: ")
        print("\t\t\t\t__________")
        user=login()

        if user:
            uid, role=user
            if role=="admin":
                admin_menu()
            elif role=="employer":
                employer_menu(uid)
            else:
                applicant_menu(uid)
        else:
            print("\n\t\t\t\t!!!Invalid E-mail/password!!!")
            print("____________________________________________________________________________________________________________________________________________________________\n")    
    elif ch=="3":
       reset_password()
    
    elif ch=="4":
        break

    else:
        print("Invalid choice.")
    