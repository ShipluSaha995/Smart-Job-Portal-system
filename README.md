# 💼 Smart Job Portal System

A console-based Job Portal System built using Python and MySQL. This system allows employers and applicants to interact efficiently, while also integrating algorithms like Dijkstra and Kruskal for smarter decision-making.

---

## 🚀 Features

### 👤 User System
- User Registration & Login
- Password Reset
- Role-based Access (Admin, Employer, Applicant)

### 🧑‍💼 Employer
- Post Jobs
- View Jobs
- View Applicants with details

### 👨‍💻 Applicant
- View Jobs
- Apply for Jobs
- Search Jobs (with distance & travel cost)
- Search by Category

### 🛠️ Admin Panel
- View all Users
- View all Jobs
- View all Applications
- Dashboard (stats)
- View MST (Minimum Spanning Tree)

---

## 🧠 Algorithms Used

- **Dijkstra’s Algorithm** → Shortest path (distance calculation)
- **Kruskal’s Algorithm (MST)** → Minimum cost network
- **Sorting** → Ranking jobs & applicants

---

## 🗄️ Database Structure

Tables used:
- `users`
- `jobs`
- `applications`

---

## ⚙️ Requirements

- Python 3.x
- MySQL Server (XAMPP or standalone)
- MySQL Connector

Install dependency:

```bash
pip install mysql-connector-python

To run this project:
git clone https://github.com/your-username/job-portal.git
cd job-portal

Smart-Job-Portal-System/
│
├── main.py                # Entry point of the application
├── db.py                  # Database connection
├── auth.py                # Login, Register, Reset Password
├── job.py                 # Job posting & searching
├── application.py         # Apply & applicant management
├── admin.py               # Admin panel features
│
├── dijkstra.py            # Shortest path algorithm
├── kruskal.py             # Minimum Spanning Tree (MST)
├── graph.py               # Graph data for locations
├── edges.py               # Edge list for MST
│
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
└── .gitignore             # Ignore unnecessary files

Database Tables:

CREATE DATABASE job_portal;
USE job_portal;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role ENUM('admin','employer','applicant')
);

CREATE TABLE jobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    company VARCHAR(100),
    location VARCHAR(100),
    salary INT,
    required_skills TEXT,
    category VARCHAR(50),
    employer_id INT,
    FOREIGN KEY (employer_id) REFERENCES users(user_id)
);

CREATE TABLE applications (
    app_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    job_id INT,
    skills TEXT,
    experience INT,
    score INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

Insert Admin Information:

INSERT INTO users (name,email,password,role)
VALUES ('Admin','admin@gmail.com',SHA2('admin123',256),'admin');

## 👨‍💻 Author

- **Shiplu Saha**