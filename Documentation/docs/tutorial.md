# Tutorial

In order to run the SMS Reminders application on a raspberry pi, you will need
to install docker and docker-compose. Since docker-compose does not come
included with docker on a pi, that will have to be installed separately.

To install docker, run this command on the command line.

`curl -sSL https://get.docker.com | sh <install docker>`

To install python pip, run this commond on the command line. Pip will allow you
to easily install docker-compose.

`sudo apt-get -y install python-pip`

Now you can install docker-compose. Using this command on the command line.

`sudo pip install docker-compose`

`fork repository from https://github.com/MoravianCollege/SMSReminders`

`go into the directory you want the project to be in`

`git clone <your fork URL>`

`download the twilio_secrets.txt file and place it in the Notifier folder`

Now that you have all the required dependancies run this command in the main
project directory

`sudo docker-compose up`
