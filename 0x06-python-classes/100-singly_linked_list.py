#!/usr/bin/python3
"""Defining class Node"""


class Node:
    """Representing a Node"""

    def __init__(self, data, next_node=None):
        """Constructing a node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter of data"""
        return self.__data

    @property
    def next_node(self):
        """Getter of next_node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Setter of data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Setter of next_node"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defining class SinglyLinkedList"""


class SinglyLinkedList:
    """Representing a single linked list"""

    def __init__(self):
        """Constructing single linked list"""
        self.__head = None

    def __str__(self):
        """print the entire list in stdout"""
        linked_list = []
        while self.__head is not None:
            linked_list.append(str(self.__head.data))
            self.__head = self.__head.next_node
        return "\n".join(linked_list)

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            copy = self.__head
            while copy.next_node is not None and value >= copy.next_node.data:
                copy = copy.next_node
            new_node.next_node = copy.next_node
            copy.next_node = new_node
