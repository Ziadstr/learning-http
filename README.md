# Simple Flask Project

This is a simple Flask project that demonstrates a basic web application using Flask. It includes a Docker configuration for easy deployment. Run the docker image and then answer the question you have in the learning path. All of the APIs in this project are numbers from one to eight, you can access them using the following example: `http://<ip of the docker>/one`

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

To run this project, you'll need the following tools:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

### Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/Ziadstr/learning-http

```

### Build and Run the Docker Image

1. Change your working directory to the project's root folder:

   ```bash
   cd simple-flask-app
   ```

2. Build the Docker image from the provided Dockerfile:
   ```bash
   docker build -t flask-app .
   ```
3. Run the Docker container:
   ```bash
   docker run -p 5000:5000 flask-app
   ```
4. Now in your terminal you will see instruction on how to access the application, after that answer the questions in your tasks.
