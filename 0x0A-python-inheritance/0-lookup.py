#!/usr/bin/python3
"""A module for returning a list of objects"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    attributes = []
    methods = []

    # Iterate over the object's attributes
    for attribute_name in dir(obj):
        # Skip attributes that start with underscore
        if not attribute_name.startswith('_'):
            attribute_value = getattr(obj, attribute_name)
            # Check if the attribute is a method
            if callable(attribute_value):
                methods.append(attribute_name)
            else:
                attributes.append(attribute_name)

    # Sort the attributes and methods alphabetically
    attributes.sort()
    methods.sort()

    # Return the combined list of attributes and methods
    return attributes + methods
