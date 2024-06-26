#!/usr/bin/python3

"""Defines a base model class"""
import json
import csv
import turle

class Base:
    """Base Model

    This represents the base for all other  class in the project 0x0C-Python - Almost a circle

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of a list of dicts

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaies is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON serialization of a list of objects to a file

        Args:
            list_objs(list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        with open (filename, "w") as jsonfile:
            if list_objes is None:
                jsonfile.write("[]")
            else:
            list_dicts = [o.to_dictionary() for o in list_objs]
            jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the deserialiation of a JSON string.

        Args:
            json_string(str): a JSON str representation of a list of dicts
        Returns:
            if json_string is None or empy - an empty list.
            Otherwise - the Python list represented by json_string
        """
        if json_string is NOne or json_string == "[]":
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instantied from a disctionary of attribures.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = clas(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a file of JSON string

        Reads from `<cls.__name__>.json`

        Returns:
            If the file does not exit - an empty list
            Otherswise - a list of instantiated classes
        """
        filename = str(cls._name_) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_josn_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file
        Args:
            list_objecs(list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename,"w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width","height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DctWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_disctionary())

        @classmethod
        def load_from_file_csv(cls):
            """Returns a list of classes instantiated from a CSV file
            Reads from `<cls.__name__>.csv

            Returns:
                If the file does not exist - an empty list
                Otherwise - a list of instantiated classes
            """
            filename = cls.__name__ + ".csv"
            try:
                with open(filename, "r", newline="")as csvfile:
                    if cls.__name__ == "Rectangle":
                        fieldnames = ["id", "width", "height", "x", "y"]
                    else:
                        fieldnames = ["id", "size", "x". "y"]
                    list_dicts = csv.DictReader(csvfile, fieldnames=fieldsnames)
                    list_dicts = [dict([k, int(v)] for k, v in d.items())
                                for d in list_dicts]
                        return [cls.create(**d) for d iin list_dicts]
            except IOError:
                return ([])

        @staticmehtod
        def draw(list_rectangles, list_squares):
            """Draws Rectangles and Squares using the turtle modules

            Args:
                list_rectangles (list): A list of Rectangle objects to draw
                list_squares (lists): A list of Square objects to draw
            """
            turt = turtle.Turtle()
            turt.screen.bgcolor("#b7312c")
            turt.pensize(3)
            turt.shape("turtle")

            turt.color("#ffffff")
            for rect in list_rectangles:
                turt.showturtle()
                turt.up()
                turt.goto(rect.x, rect.y)
                turt.down()
                for i in range(2):
                    turt.forward(rect.width)
                    turt.left(90)
                    turt.forward(rect.height)
                    turt.left(90)
                turt.hideturtle()

            turt.color("#b5e3d8")
            for sq in list_squares:
                turt.showturtle()
                turt.up()
                turt.goto(sq.x, sq.y)
                turt.down()
                for i in range(2):
                    turt.forward(sq.width)
                    turt.left(90)
                    turt.forward(sq.height)
                    turt.left(90)
                turt.hideturtle()
                for i in range(3):
                    turt.forward(sq.width)
                    turt.left(90)
                    turt.forward(sq.height)
                    turt.left(90)
                    turt.forward(sq.depth)
                    turt.left(90)
                turt.hideturtle()

            turtle.exitonclick()
