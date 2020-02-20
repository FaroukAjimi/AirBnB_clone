#!/usr/bin/python3
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import inspect

def ifclass(str):
    try:
        v = inspect.isclass(eval(str))
        return(v)
    except:
        return False
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ Quit command to exit the program
        """
        return True
    
    def emptyline(self):
        pass
<<<<<<< HEAD
    def do_create(self, line):
        {
        }
=======

    def do_create(self, name):
        """ Do_create creates another <name> object
        """
        if name is None or name == "":
            print("** class name missing **")
        elif name != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, name):
        """ shows instances of an obj
        """
        args = name.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if (
                    ifclass(args[0]) and     
                    issubclass(eval(args[0]), BaseModel) is True):
                if len(args) > 1:
                    for k,v in FileStorage().all().items():
                        Id = k.split('.')[1]
                        if Id == args[1]:
                            print(str(v))
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
  
>>>>>>> bb33fc56d74dbc4392c19587e5648facf7cfb801
if __name__ == '__main__':
    HBNBCommand().cmdloop()
