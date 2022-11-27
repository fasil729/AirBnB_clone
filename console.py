#!/usr/bin/python3
"""the console to test my works"""
import cmd
from models import BaseModel

class_names = ["BaseModel"]


class HBNBCommand(cmd.Cmd):
    """a class use for console """
    prompt = "(hbnb) "

    def emptyline(self):
        """empty line """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, obj=None):
        if not obj:
            print("** class name missing **")
        else:
            if obj in class_names:
                new = eval(obj)()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
