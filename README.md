# Containerized App Exercise

![CI Web App](https://github.com/software-students-fall2023/4-containerized-app-exercise-liatha4/actions/workflows/web_app_ci.yml/badge.svg)

![CI ML Client](https://github.com/software-students-fall2023/4-containerized-app-exercise-liatha4/actions/workflows/ml_client_ci.yml/badge.svg)

## Project Description
This project aims to create a user-friendly web application that utilizes machine learning to detect emotions through a webcam. The application, containerized using Docker for ease of deployment, employs Flask for the backend and HTML, CSS, and JavaScript for the frontend. Users grant webcam access, and upon clicking the "Capture" button, the system analyzes their emotion. Depending on the detected emotion, users are dynamically redirected to corresponding emotion-themed pages. The project showcases the integration of machine learning in a web application, offers a responsive UI, and can be deployed on various platforms using Docker containers, making it a versatile and engaging prototype for emotion-aware applications. 

### Mongo
The machine-learning-client logs facial data into the mongo container,
while the web-app just logs a simple message. <br> <br>
The machine-learning-client 
can be made to save data into mongo via clicking any of the 'how are you doing'
buttons, and the web-app will save data in the 'fancy-town' route, via pressing the
'are you looking fancy' button


## Project Members
- [Athena Leong](https://github.com/aleong2002)
- [Harry Minsky](https://github.com/hminsky2002)
- [Lianna Poblete](https://github.com/liannnaa)

## Configuration Instructions
To run the project:
- clone the repository, and make sure Docker is installed
- run  `docker-compose up --build` in the main directory
- access the web-app from `http://localhost:3001`
- click on a button to process the emotion!!

## Testing
To test the machine-learning-client or the web app
- cd to the relevant directory
- run ```pytest tests.py```