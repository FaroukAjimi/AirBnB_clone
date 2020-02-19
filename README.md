# AirBnB_clone - the console


### Description
The console is a command line interpreter that takes a command written as input, interprets it and executes it.

### How to start it
First, you need a terminal and all the files and folders in your disk.

##### Files and Folders
- AUTHORS - list of contributors to this repository.
- README.md - the README markdown file.
- models - directory that contains all classes used for the entire project.
- tests - directory that contains all unit tests.
- console.py - entry point of the command interpreter.
- models/base_model.py - contains class that is base of all our models.
- models/user.py - contains child class that inherits from BaseModel (from models/base_model).
- models/engine - directory that contains all storage classes.
- file_storage - storage class

Second, all you need to do is run console
    $ ./console.py
and start typing your commands (try the command 'help')

### Commands

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Command | Description | Requirements |
|--------|--------|--------------|
| create | creates a new instance of BaseModel and prints its id | |
| show | prints the string representation of an instance | class name and id |
| destroy | deletes an instance | class name and id |
| all | prints all string representations | [class name] |
| update | updates an instance (add or update attribute) | class name and id |
| help | displays help with documentation | [command] |
| quit / EOF | exits the program | |

### Usage
    $ create <class name>
    $ show <class name> <id>
    $ destroy <class name> <id>
    $ all [<class name>]
    $ update <class name> <id> <attribute name> "<attribute value>"
### Examples
this is what you are supposed to experience in your terminal (the id are unique, they are random)
```sh
neiferanti@ubuntu-64:/AirBnB_clone$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```