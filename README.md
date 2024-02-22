# Welcome to Socialize
## A simple social media posting application
### Description
This application provides an extensive dashboard for the user to create posts and view other user's posts. Further user can draft a post, and schedule a post according to their needs. 

Watch the working video of the application [here]().

### Installation
To Simply use the system, Clone this repository using ```git clone https://github.com/OsafAliSayed/Socialize.git```

You also must have Python installed on your system. install python [here](https://www.python.org/downloads/).

To keep the setup clean let's setup a virtual environment as follows: ``` python -m venv venv ```

for Windows start the environment by running ```venv/Scripts/activate``` and for Linux run ``` source venv/bin/activate ```.

then, install the dependencies using ```pip install -r requirements.txt```

Now, make the migrations ```python manage.py makemigrations``` and run them ```python manage.py migrate```.

Start the application by running ```python manage.py runserver```. Make sure you are in the socialize folder before running all of these commands.

### Screen Shots
This is what the application looks like. It is a simple interface that lets you perform CRUD operations with the posts.

Homescreen before login:

![image](https://github.com/OsafAliSayed/Socialize/assets/99737087/53301a3c-c1bf-4764-a0f4-bd8fe2d6cef8)

Login page:

![image](https://github.com/OsafAliSayed/Socialize/assets/99737087/f699c4cf-a81a-4b4a-8a58-91cf1c218643)

Register page:

![image](https://github.com/OsafAliSayed/Socialize/assets/99737087/2b67f5af-e755-4b81-86b1-24ab80335e84)

Homescreen after login:

![image](https://github.com/OsafAliSayed/Socialize/assets/99737087/ffe522a2-12f1-4cc2-9564-e3c61eaf58b2)

Create post page:

![image](https://github.com/OsafAliSayed/Socialize/assets/99737087/4cd48d60-6f38-4e1b-abb2-cbd9c0e3d9de)

Scheduled posts:

![image](https://github.com/OsafAliSayed/Socialize/assets/99737087/31370295-48f3-49aa-b34c-167da10a2dc8)

Draft:

![image](https://github.com/OsafAliSayed/Socialize/assets/99737087/827df8f9-2b42-405f-a101-7f6806f9563f)

### Challenges
- One of the challenges I faced during this assignment was to create the post-scheduling. That required a little bit of research to figure out a clever solution.
- Creating drafts was also a challenge to figure. However, I was able to set it up pretty nicely.
 
### Assumptions
- No image and video posts were allowed to be made.
- No user profile has been created
- Also no users can follow or unfollow each other, Everyone is public here.

### Deliverables
- [X] A functional web application that meets the given criteria.
- [X] Source code for your application hosted in a public GitHub repository.
- [X] A README file detailing setup instructions, key features, and usage of the dashboard, including any assumptions made.
- [X] A README file included in your GitHub repository that fulfills the documentation requirements.
- [X] A working video demonstration of the dashboard, including an explanation of the features and the codebase.
