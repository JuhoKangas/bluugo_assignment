# bluugo_assignment
My assignment for Bluugo oy. I have no prior experience on django but thought it would be fun opportunity to learn what it takes to make simple full-stack app to run. I learned a lot about django and python and really liked the process. 

## App deployed here
https://fast-mountain-08252.herokuapp.com/

## Deploy on your own machine
For this app we need to have pipenv installed to create the virtual environment for the project. If you don't have pipenv installed, installation instruction for your system can be found [here](https://pypi.org/project/pipenv/).

After installation, clone this project `git clone https://github.com/JuhoKangas/bluugo_assignment.git` in directory of your chose and `cd` into it. 

Inside the directory run `pipenv install` to install all needed dependencies listen in Pipfile.lock file.

Then run `pipenv shell` to open virtual shell for the project.

Finally to get the application running run `python manage.py migrate` and `python manage.py runserver`.

You can now find the application running in http://localhost:8000/
