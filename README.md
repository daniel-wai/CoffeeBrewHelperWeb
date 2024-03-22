# Coffee Brew Helper Application
[![CoffeeBrewHelper1000_withTitle_Thumbnail](https://github.com/daniel-wai/CoffeeBrewHelperWeb/assets/83196054/f5370b8c-86d1-4997-bfd5-82d144e10a4f)](https://youtu.be/fjCw9sn6c1k?si=RKWY-41fv2gSa4qQ)

[Click here to try the application!](https://danielwai.pythonanywhere.com)

## Introduction

We often think of brewing coffee as using an automatic drip machine where the process is hands-off for the most part. However, coffee ethusiasts have been exploring other brewing methods, such as pourover, french press and aeropress, to achieve the best cup possible. This application aims to help new coffee ethusiasts experiment with their coffee brewing technique.

Coffee brew recipes typically include the following key factors: 
- Brew ratio: Water Weight / Coffee Weight
- Coffee grind size
- Water temperature
- Brew process: speed of pouring (flow rate), number of pours, steep time, etc. 

There are many brew guides available online. Here is [Pilot Coffee Roasters Brew Guide](https://www.pilotcoffeeroasters.com/learn/brew-guides/) showing different coffee recipes for various methods.

This application guides users through the brew process and provides feedback on their performance. Espresso-based drinks are not yet covered.

## User Guide
Check out the [user guide](https://danielwai.pythonanywhere.com/user-guide/) for details on using the application.

## Installation
Here is how you can clone the source repository to run locally.

### Cloning the Repository
1. Please see https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository 
1. Source repository: https://github.com/daniel-wai/CoffeeBrewHelperWeb.git

### Installing python
1. Download Python:
   
	Visit the official Python website (https://www.python.org/downloads/) and download the latest version of Python for your operating system (Windows, macOS, or Linux).

3. Install Python:
   
	Run the installer and follow the on-screen instructions. Make sure to check the box that says "Add Python to PATH" during the installation process. This option makes it easier to run Python from the command line.

5. Verify Installation:

	Open a command prompt (Windows) or terminal (macOS/Linux) and type the following command to check if Python is installed:
	
	```bash
	python --version
	```
	or for Python 3:
	
	```bash
	python3 --version
	```
	You should see the installed Python version.

### Setting up a virtual environment and running application

1. Navigate to the Project Directory:
	```bash
	cd coffee
	```
2. Create a Virtual Environment using venv:
   
	It is recommended to create a virtual environment before installing the dependencies to keep the global environment clean. However, you don't have to do step 2 and 3.
	```bash
	python -m venv venv
	```
	
4. Activate the Virtual Environment:

	On Windows:
	```bash
	source ./venv/Scripts/activate
	```
	On Unix or MacOS:
	```bash
	source ./venv/bin/activate
	```
 
5. Installing Dependencies:
   
	```bash
	pip install -r requirements.txt
	```

7. Create an environment variables file (.env):
   
	In the project folder, create a .env file which is used by settings.py to initialize key parameters
	The .env file should contain the following: 
	```
	DEBUG=True
	SECRET_KEY=[your_generated_secret_key_here]
	ALLOWED_HOSTS=localhost,127.0.0.1
	```

	DEBUG=[True/False]: The DEBUG setting in Django determines whether your project is in debug mode. Debug mode provides additional information in error pages and enables certain development features. It is recommended to set DEBUG to True during development but to set it to False in a production environment for security reasons.
	
	SECRET_KEY=[your_generated_secret_key_here]: The SECRET_KEY is a cryptographic key used for various security purposes, such as creating secure hashes and generating session keys. It is crucial to keep the SECRET_KEY secret and not share it publicly. The value should be a long, random string. You can generate a secure key using Django's default value or by using a tool/library to create one.
	
	ALLOWED_HOSTS=[ex. localhost,127.0.0.1]: The ALLOWED_HOSTS setting is a security measure that specifies which host/domain names can serve the Django application. In production, you should set this to the domain names or IP addresses that will be used to access your application. For development, you might include localhost and 127.0.0.1 to allow access from your local machine.
		
9. Run the Application:
	```bash
	python manage.py runserver
	```

10. Deactivate the Virtual Environment:

	When finished with your application, deactivate the virtual environment:
	```
	deactivate
	```

### Common Issues and Troubleshooting

To be completed once user feedback has been processed.

## Theme

The SB Admin 2 free Boostrap 4 theme is used with the following source repository: https://github.com/StartBootstrap/startbootstrap-sb-admin-2.git

The relevant files are copied to the static folder at the root folder level. 



