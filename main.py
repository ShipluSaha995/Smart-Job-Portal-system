from auth import register, login
from job import *
from application import *
from admin import *


def admin_menu():
    while True:
        print("\n 1. Dashboard\n2. All Users\n3. All Jobs\n4. All applicatios\n5. MST\n 6. Logout ")
        c=input("Enter Your Choice: ")

        if(c=="1"):
            dashboard()
        elif(c=="2"):
            view_all_users()
        elif(c=="3"):
            view_all_jobs()
        elif(c=="4"):
            view_all_applications()
        elif(c=="5"):
            show_mst()
        else:
            break


def employer_menu(uid):
    while True:
        print("\n1. Post Job(uid)\n 2. View Jobs\n 3. View Applicants\n 4. Logout")
        c=input("Enter Your Choice: ")

        if(c=="1"):
            post_job(uid)
        elif(c=="2"):
            view_jobs()
        elif(c=="3"):
            view_applicants(int(input("Job ID: ")))


def applicant_menu(uid):
    while True:
        print("\n1. View Jobs\n 2. Apply\n 3. Search\n 4. Catagory\n 5. Logout\n")
        c= input("Enter your choice: ")

        if(c=="1"):
            view_jobs()
        elif(c=="2"):
            apply_job(uid)
        elif(c=="3"):
            search_jobs()
        elif(c=="4"):
            search_by_catagory()
        else:
            break