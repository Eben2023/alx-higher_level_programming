#!/usr/bin/python3
"""
Define a class Node that represents a node of a singly linked list.
Define a class SinglyLinkedList that represents a singly linked list.
"""


class Node:
    """Represents a node of a singly linked list."""
    def __init__(self, data, n_node=None):
        """
        Initialize a new node.

        Args:
            data (int): The data value of the node.
            n_node (Node): The next node in the linked list.
        """
        self.data = data
        self.n_node = n_node

    @property
    def data(self):
        """Get/set the data value of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Args:
            value (int): The data value to be set.

        Raises:
            TypeError: If the data value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def n_node(self):
        """Get/set the next node in the linked list."""
        return self.__next_node

    @n_node.setter
    def n_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The next node to be set.

        Raises:
            TypeError: If the next node is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("n_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        """Initialize a new singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position in the linked list.

        Args:
            value (int): The data value of the new node.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.n_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.n_node is not None and current.n_node.data < value:
                current = current.n_node
            new_node.n_node = current.n_node
            current.n_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: The linked list represented as a string with each node
            value on a new line.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.n_node
        return '\n'.join(nodes)
