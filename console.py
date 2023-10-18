#!/usr/bin/python3
"""Defs the Hbnb console"""
import re
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


def parse(input_string):
    """Parse arguments with optional curly braces."""
    curly_braces_match = re.search(r"\{(.*?)\}", input_string)
    brackets_match = re.search(r"\[(.*?)\]", input_string)
    
    if curly_braces_match is None:
        if brackets_match is None:
            return [item.strip(",") for item in split(input_string)]
        else:
            lexer = split(input_string[:brackets_match.span()[0]])
            result_list = [i.strip(",") for i in lexer]
            result_list.append(brackets_match.group())
            return result_list
    else:
        lexer = split(input_string[:curly_braces_match.span()[0]])
        result_list = [i.strip(",") for i in lexer]
        result_list.append(curly_braces_match.group())
        return result_list


class HBNBCommand(cmd.Cmd):
    """Defs the HolbertonBnB command interpreter

    Attributes:
        prompt (str): The cmd prmpt
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when inputis invalid"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "count": self.do_count
        }
        matchh = re.search(r"\.", arg)
        if matchh is not None:
            argl = [arg[:match.span()[0]], arg[matchh.span()[1]:]]
            matchh = re.search(r"\((.*?)\)", argl[1])
            if matchh is not None:
                command = [argl[1][:match.span()[0]], matchh.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal that exits the program"""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance then print its id
        """
        arg_list = parse(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the str representation of a class instance of given id
        """
        arglis = parse(arg)
        obj_dict = storage.all()
        if len(arglis) == 0:
            print("** class name missing **")
        elif arglis[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglis) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglis[0], arglis[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arglis[0], arglis[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delte an instance of a class of a gien id"""
        arglis = parse(arg)
        obj_dict = storage.all()
        if len(arglis) == 0:
            print("** class name missing **")
        elif arglis[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglis) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglis[0], arglis[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arglis[0], arglis[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display str representations class.
        If no class is given, displays all instantiated objs"""
        arglis = parse(arg)
        if len(arglis) > 0 and arglis[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objlis = []
            for o in storage.all().values():
                if len(arglis) > 0 and arglis[0] == o.__class__.__name__:
                    objlis.append(obj.__str__())
                elif len(arglis) == 0:
                    objlis.append(o.__str__())
            print(objlis)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the num of instances pf a given class"""
        arglis = parse(arg)
        count = 0
        for o in storage.all().values():
            if arglis[0] == o.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update instance of class of a given id by adding or updating
        a given attribute key/value pair or dict"""
        arglis = parse(arg)
        obj_dict = storage.all()

        if len(arglis) == 0:
            print("** class name missing **")
            return False
        if arglis[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arglis) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arglis[0], arglis[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arglis) == 2:
            print("** attribute name missing **")
            return False
        if len(arglis) == 3:
            try:
                type(eval(arglis[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arglis) == 4:
            o = obj_dict["{}.{}".format(arglis[0], arglis[1])]
            if arglis[2] in o.__class__.__dict__.keys():
                valtype = type(o.__class__.__dict__[arglis[2]])
                o.__dict__[arglis[2]] = valtype(arglis[3])
            else:
                o.__dict__[arglis[2]] = arglis[3]
        elif type(eval(arglis[2])) == dict:
            o = obj_dict["{}.{}".format(arglis[0], arglis[1])]
            for key, val in eval(arglis[2]).items():
                if (key in o.__class__.__dict__.keys() and
                        type(o.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(o.__class__.__dict__[key])
                    o.__dict__[key] = valtype(val)
                else:
                    o.__dict__[key] = val
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

