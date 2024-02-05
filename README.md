# Coffee Brew Helper Application

## Introduction

We often think of brewing coffee as using an automatic drip machine where the process is hands-off for the most part. However, coffee ethusiasts have been exploring other brewing methods, such as pourover, french press and aeropress, to achieve the best cup possible. This application aims to help new coffee ethusiasts experiment with their coffee brewing technique.

Coffee brew recipes typically include the following key factors: 
- Brew ratio: Weight of Water / Weight of Coffee
- Coffee grind size
- Water temperature
- Brew process: speed of pouring (flow rate), number of pours, steep time, etc. 

There are many brew guides available online. Here is one by Pilot Coffee Roasters showing different coffee recipes for various methods: https://www.pilotcoffeeroasters.com/learn/brew-guides/

This application focuses on guiding the brew process and providing feedback on the executed performance. Espresso-based drinks are not yet covered.

## Features

### Library of Methods and Associated Recipes

https://www.subtext.coffee/pages/brew-guides
Brew methods and their associated recipes are uploaded manually to the database. The long-term goal is to allow user input to add or improve recipes based on their testing. Here is a list of supported methods and recipes:
- V60: Hario V60 pourover
   - James Hoffmann V60 1 cup
   - Pilot Coffee Roasters Pourover Brew Guide
   - Subtext Coffee Roasters V60 Brew Guide
- French press:
   - Pilot Coffee Roasters French Press Brew Guide
- Aeropress:
   - Pilot Coffee Roasters AeroPress Brew Guide
   - Subtext Coffee Roasters AeroPress Brew Guide
   
### Recipe

#### General Information
Each recipe lists:
- Name
- Description
- Reference (if applicable)

#### Equipment
List of equipment recommended to carry out each recipe.

#### Preparation Process
List of steps before brewing can begin.

#### Brewing Process
List of steps to brew coffee. These are time-sensitive steps, so complete the preparation entirely first.

#### Settings

##### Enable Read Steps Outloud
The target step to complete is read outloud. For brew steps, the target total water and time is read outloud after the step description.

##### Enable Voice commands
When enabled, the user can use the appplication by saying commands rather than pressing buttons or using the keyboard. See Usage section for more details on supported commands.

## Usage
Visit danielwai.pythonanywhere.com to try the application!

The typical workflow is as follows:
1. Select a Brew Method from the dropdown menu on the top left. The Recipe dropdown menu will populate with all recipes which use this brew method.
2. Select a recipe from the Recipe dropdown menu. Press Select. Recipe information will be loaded onto the page.
3. Use the Equipment list to gather all required tools before you begin.
3. Use the Preparation Steps to ensure the water, ground coffee beans and equipment are ready to begin the timed brewing process. 
	i. To highlight the first step, press the "Prepare" button, press the shift key or say "prepare" [1]
	ii. The current step will be highlighted in yellow and have a bolded outline. It will be read outloud if the Read Step Outloud checkbox is enabled [2]. 
	iii. To highlight the next step, press the "Next" button, press the spacebar or say "next" [1]
4. Use the Brew Steps to guide you through the timed brewing process where the coffee extraction takes place:
	i. Start the timer to begin brewing: press the "Start" button, press the shift key or say "start" [1]. The first brew step is highlighted with a bolded outline. You should hear an audible beep signifying the start of the brewing process. For all other brew steps, audible beeps start 3 seconds before the start of the step.
	i. Each time you finish a step, press the "Next" button, press the spacebar or say "next" to record the elapsed time to complete this step. This can be reviewed at the end to evaluate the timing compared to the coffee taste. The target step has a bolded outline, while the current step that you are working on is highlighted. 
	NOTE: 
		To pause the timer, press the Pause button, press the shift key or say "pause" [1]. Pausing the timer during brewing is not recommended as it doesn't allow for an accurate measurement of your performance
7. As your coffee cools, review the time you took to complete each step compared to the recipe. The key is not getting exact times and volumes, but rather how the process affects the taste. Let the taste decide how you adjust grind size, water, and process. 
8. To reset all steps, press the Reset button, press the ctrl key or say "reset" [1].

In any case, you are rewarded with a fresh cup of caffeine delight. Enjoy!

> [1] Enable Voice Command checkbox to be able to say commands to use the application
> [2] Enable Read Step Outloud checkbox to hear the step description read outloud

Here is the summary of various ways to achieve the same command. Try i. pressing a button, ii. pressing a keyboard key or iii. saying a key word.

| Command  | i. Button | ii. Keyboard | iii. Voice |
| ------------- | ------------- | ---- | ---- |
| Start Preparation steps  | Prepare  | shift | Prepare 
| Start/continue Brew step  | Start  | shift | Start 
| Pause Brew step   | Pause  | shift | Pause 
| Reset all steps  | Reset  | ctrl | Reset 
| Move to next Preparation step or record elapsed time to complete current Brew step | Next  | spacebar | Next

## Installation
Here is how you can clone the source repository to run locally.

### Cloning the Repository
Source repository: https://github.com/daniel-wai/CoffeeBrewHelperWeb.git
Please see https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository. 

### Installing python
1. Download Python:
	Visit the official Python website (https://www.python.org/downloads/) and download the latest version of Python for your operating system (Windows, macOS, or Linux).

2. Install Python:
	Run the installer and follow the on-screen instructions. Make sure to check the box that says "Add Python to PATH" during the installation process. This option makes it easier to run Python from the command line.

3. Verify Installation:
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
	
3. Activate the Virtual Environment:
	On Windows:
	```bash
	source ./venv/Scripts/activate
	```
	On Unix or MacOS:
	```bash
	source ./venv/bin/activate
	```
4. Installing Dependencies
	Install Dependencies Using pip:
	```bash
	pip install -r requirements.txt
	```
5. Create an environment variables file (.env)
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
	
6. Run the Application
	```bash
	python manage.py runserver
	```

7. Deactivate the Virtual Environment:

	When finished with your application, deactivate the virtual environment:
	```
	deactivate
	```

### Common Issues and Troubleshooting:

To be completed once user feedback has been processed.
