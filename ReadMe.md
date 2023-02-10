Django To-Do List Application


To build the image, run the following command in the same directory as the Dockerfile:

docker build -t todo-list-image .


To create a container from the image, run the following command:

docker run -p 80:80 -d --name todo-list-container todo-list-image



This maps port 80 in the container to port 80 on the host machine and runs the container in the background with the name "todo-list-container".