# Chat-App Django Channels

## Project Description

### What the application does?
The Application has basic CRUD Functionalities for Users to Create Rooms and Chat with there users.
Apart from that, whenever a Chat Room is opened the Client sends a Socket Connection request to the server.
If the client is not authenticated a random 6 digit user ID is added to the session to differentiate the user. With the help of this Anonymous users can visit and access
the various features of a chat room.

### What Technologies are Used?
The Technologies Used are:-
- Django
- Django Channels
- Web Sockets
- JavaScript
- Bootstrap

![Image](https://i.imgur.com/oqhwOSO.png?1)


## How to Install and run the project
Activate your Python Virtual Enviornment and just run the following commands
```
pip install -r requirements.txt
python manage.py runserver
```

Then goto http://127.0.0.1:8000/ to access the project.
