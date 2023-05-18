# COMP90024ASS2 Backend
## Welcome to the Backend project!

Version: 1.0.0, 18 May, 2023
Contributors: Jinhua Fan, Yuxuan Zeng

### Project Overview
Backend is a Python-based web application that utilizes the Django framework and CouchDB database to implement functionality. The project aims to provide a scalable and customizable backend solution for building web applications and APIs.

### Project Structure
The file structure of the Backend project is as follows:

```markdown
├── backend/
│   ├── manage.py
│   ├── mainapp/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── Backend/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── venv/
│       └── ...
├── Dockerfile
├── requirements.txt
└── README.txt
```

* manage.py: Django management tool used for running the development server and executing management commands.
* mainapp/: Directory containing the main application, including models, views, and URL configuration.
* Backend/: Root directory of the Django project, including project configuration files and URL configuration.
* venv/: Virtual environment directory for isolating project dependencies and environment.
* Dockerfile: Configuration file for building the Docker container.
* requirements.txt: Lists the project dependencies.

### Quick Start
1. Ensure that you have Docker installed.
2. Navigate to the root directory of the project in the command line.
3. Build the Docker container:
```cmd
docker build -t backend-app .
```
4.Run the Docker container:
```python
docker run -p 8000:8000 backend-app
```
The project will run on port 8000 inside the container and can be accessed via port 8000 on the host machine.


### Configuration
* The project's configuration file is located at Backend/settings.py, where you can customize the configuration as per your requirements, such as database settings, security settings, logging, etc.
* You can customize the run configuration of the Docker container by modifying the CMD command in the Dockerfile.


