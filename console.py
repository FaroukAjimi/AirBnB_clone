#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_quit(self, line):
        """Quit command to exit the program
"""
        return True
    def do_EOF(self, line):
        """Quit command to exit the program
"""
        return True
    def emptyline(self):
        pass
        def do_create(self, line):
            {
                
            }
if __name__ == '__main__':
    HBNBCommand().cmdloop()
