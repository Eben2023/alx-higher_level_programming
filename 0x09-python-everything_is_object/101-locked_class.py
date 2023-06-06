#!/usr/bin/python3
class LockedClass:
    """
    Class that prevents dynamic creation of instance attributes,
    except for 'first_name'.
    """

    __slots__ = ["first_name"]
