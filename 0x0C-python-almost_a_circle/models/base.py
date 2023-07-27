#!/usr/bin/python3
""" Module defining the Base class """


class Base:
    """ Base class for managing id attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method for Base class """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file.

        Args:
            cls (class): The class.
            list_objs (list): A list of objects.
        """
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(cls.to_dictionary(obj))
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(Base.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a string into an object.

        Args:
            json_string (str): The JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new object of the class.

        Args:
            cls (class): The class.
            **dictionary (dict): Keyword arguments of the object.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        List of objects from a file.

        Args:
            cls (class): The class.
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                string = f.read()
                lst = cls.from_json_string(string)
                inst = []
                for item in lst:
                    inst.append(cls.create(**item))
                return inst
        except FileNotFoundError:
            return []
