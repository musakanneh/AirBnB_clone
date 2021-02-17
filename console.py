#!/usr/bin/python3
"""The console v: 0.0.1
Contains the entry point of the command interpreter

"""
import cmd
import json
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Custom console class"""

    def handle_errors(self, line, num_of_agrs):
        """Displays error messages to user

        Args:
            line(any): line inputs
            num_of_args(int): number of input arguments

        """
        classes = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]

        msg = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(msg[0])
            return 1
        args = line.split()
        if num_of_agrs >= 1 and args[0] not in classes:
            print(msg[1])
            return 1
        elif num_of_agrs == 1:
            return 0
        if num_of_agrs >= 2 and len(args) < 2:
            print(msg[2])
            return 1
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if num_of_agrs >= 2 and key not in d:
            print(msg[3])
            return 1
        elif num_of_agrs == 2:
            return 0
        if num_of_agrs >= 4 and len(args) < 3:
            print(msg[4])
            return 1
        if num_of_agrs >= 4 and len(args) < 4:
            print(msg[5])
            return 1
        else:
            return 0

    def handle_empty_line(self, line):
        """Eliminates empty lines"""
        return False

    def do_quit(self):
        """Handles the 'quit' command"""
        return True

    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d"""
        return True

    def do_create(self):
        """ Creates a new instance of @cls_name class,
        and prints the new instance's ID.
        Arguments to enter with command: <class name>
        Example: 'create User'
        
        """
        if self.handle_empty_line()

if __name__ == '__main__':
    cli = HBNBCommand()
    cli.cmdloop()
