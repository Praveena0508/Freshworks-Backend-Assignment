#code.py
#function definition for create, read and delete operations

import globals

import sys 
try: color = sys.stdout.shell 
except AttributeError: raise RuntimeError("Use IDLE")   #For printing output in different colour 

#STRING means green colour
#KEYWORD means orange colour
#COMMET means red colour

def create(key,value):        
    if(len(globals.dataStore)<=1024*1024*1024): # for datastore size is less than 1GB
        if(key not in globals.dataStore): #To check for the key presence in data store
            if((key.isalpha()) and (len(key)<=32) and (len(value)<=16*1024*1024)): #To check given key is a string whose length is less than or equal to 32 char and value is less than or equal to 16KB
                globals.dataStore[key]=value
                color.write("Successfully added given key-value pair\n","STRING")
            else:
                if((key.isalpha())==0):
                    color.write("Given Key is not a string!!!\n","KEYWORD")
                elif(len(key)>32):
                    color.write("Key length is larger than specified limits!!!\n","KEYWORD")
                elif(value>16*1024*1024):
                    color.write("Value size is too large!!!\n","KEYWORD")
        else:
            color.write("Given key is already found in data store\n","COMMENT")
    else:
        color.write("!!! Data Store memory is full !!!\n","COMMENT")
        

def read(key):
    if(key in globals.dataStore):#To check for the key presence in data store
        print(globals.dataStore[key])
    else:
        color.write("Given key not found in dataStore!!!\n","KEYWORD")
    
def delete(key):
    if(key in globals.dataStore):#To check for the key presence in data store
        del globals.dataStore[key]
        color.write("Given Key-value pair deleted\n","STRING")
    else:
        color.write("Given key not found in dataStore!!!\n","KEYWORD")
