#!/usr/bin/python3
"""the console to test my works"""
import cmd
from models import BaseModel, storage, City, State, Place, Amenity, Review, User
import json


class_names = ["BaseModel", "City", "State",
        "Place", "Amenity", "Review", "User"]


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
        """create new oject and show id"""
        if not obj:
            print("** class name missing **")
        else:
            if obj in class_names:
                new = eval(obj)()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args=None):
        """shows all object's string representatin,
        if object and also thi id exists"""
        arg = args.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in class_names:
            print("** class doesn't exist **")
        else:
            is_ins = False
            if len(arg) == 1:
                print("** instance id missing **")
            else:
                all_ob = storage.all()
                for key, item in all_ob.items():
                    if key == f"{arg[0]}.{arg[1]}":
                        print(item)
                        is_ins = True
                    else:
                        continue
                if not is_ins:
                    print("** no instance found **")

    def do_destroy(self, args=None):
        """ Deletes an instance based on the class name and id """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in class_names:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args=None):
        """Prints all string representation of all instances
        based or not on the class name"""
        lis = []
        if not args:
            for key, value in storage.all().items():
                keys = key.split('.')
                value.id = keys[1]
                lis.append(str(value))
        else:
            if args not in class_names:
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    keys = key.split('.')
                    value.id = keys[1]
                    if keys[0] == args:
                        lis.append(str(value))
        print(lis)

    def do_update(self, args):
        """ Updates an instance based on the class name and id """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_names:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
