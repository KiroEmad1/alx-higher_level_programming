#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id if id is not None else Base.__nb_objects + 1
        Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs] if list_objs else []))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        if dictionary:
            return cls(**dictionary)

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                return [cls.create(**d) for d in cls.from_json_string(jsonfile.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls._get_fieldnames())
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                return [cls.create(**{k: int(v) for k, v in row.items()}) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def _get_fieldnames():
        return ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]

    @staticmethod
    def draw(list_rectangles, list_squares):
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
            for _ in range(2):
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
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

