#This file will take the name, age and address of the person and log it
#if the data is already present we will throw an error

import logging
import os

def namecheck(name):
    if os.path.exists("data.txt"):
        with open("data.txt",'r') as readFile:
            for line in readFile:
                if line.lower().startswith(f'Name: {name}'):
                    logging.error(f"Name: {name} already exists")
                    return False
                if len(name) == 0:
                    logging.critical("Name cannot be blank")
                    return False
                elif not name.isalpha():
                    logging.critical("Name should be alphanumeric")
                    return False
                else:
                    logging.error(f"check successful")
                    return True
    else:
        logging.debug('No data found')
        return True      

def saveData(name, age, email):
    with open("data.txt", 'a') as appendFile:
        appendFile.write(f"Name: {name} - Age: {age} - Email: {email}")
        print("Details saved successfully")

