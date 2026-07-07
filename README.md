# DSM6332: Cloud Computing and Web Programming

# NGO Donor & Project Fund Tracking System

## Student Information


- **Name:** Clementine Nyiraneza
- **Student ID:** 224020421
- **Module Code:** DSM6332
- **Project Title:** NGO Donor & Project Fund Tracking System

## Project Description

This project is a web-based NGO Donor & Project Fund Tracking System developed using Django. It allows NGOs to manage donors, projects, donations, milestones, project photos, and includes a Machine Learning model to predict project funding.

## Technologies Used

- Django
- Django REST Framework
- SQLite
- HTML5
- CSS3
- JavaScript
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Git & GitHub
- Ubuntu Server
- Gunicorn
- Nginx
- SQLite (Development Database)

## Features

- User Registration
- Login & Logout
- Role-Based Access Control
- Donor Management
- Project Management
- Donation Management
- Milestone Management
- Project Photo Upload
- Search Functionality
- REST API
- Machine Learning Funding Prediction
- Analytics Dashboard

## Setup Instructions

```bash
git clone <repository-url>
cd NGO_Donor_Tracking
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Ubuntu

```bash
source venv/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Create Superuser

```bash
python manage.py createsuperuser
```

Run Server

```bash
python manage.py runserver
```

## REST API

```
/api/projects/<project_id>/total-donations/
```

## Machine Learning

Funding prediction using a trained Scikit-learn Regression model.

## GitHub

Submitted for DSM6332 Final Examination.

## Database

The application was developed and tested using SQLite during development.
The project structure supports migration to MySQL for production deployment.

Main database entities include:

- Donor
- Project
- Donation
- Milestone
- ProjectPhoto