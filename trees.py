from decorators import method_expects


class Node:
    """Represents a single node within a tree data structure."""

    def __init__(self, value, children=None):
        if children is None:
            children = set()
        self._value = value
        self._children = children

    def __str__(self):
        return f"Node(value={self._value}, children={self._children})"

    def __repr__(self):
        return f"Node(value={self._value}, children={self._children})"

    @property
    def value(self):
        """Returns the value of the TreeNode."""
        return self._value

    @value.setter
    def value(self, new_name):
        """Sets the value of the TreeNode."""
        self._value = new_name

    @property
    def children(self):
        """Returns the set of all children of the TreeNode."""
        return self._children

    @method_expects(set)
    @children.setter
    def children(self, new_children):
        """Sets the children of the TreeNode.
        param new_children: Requires a set of TreeNodes. Raises a TypeError if this is not met."""
        for element in new_children:
            if not isinstance(element, Node):
                TypeError(f'"{element}" of type {type(element)} must be of type Node.')
        self._children = new_children

    @method_expects(Node)
    def add(self, new_child):
        """Adds a new child node."""
        self._children.add(new_child)

    def add_all(self, *children):
        """Adds an indefinite number of children nodes."""
        for param in children:
            if not isinstance(param, Node):
                raise TypeError(f'"{param}" of type {type(param)} must be of type Node.')

        for child in children:
            self._children.add(child)

    @method_expects(Node)
    def remove(self, child):
        """Removes the child node specified from the set of children."""
        self._children.remove(child)

    def remove_all(self, *children):
        """Removes an indefinite number of children nodes."""
        for param in children:
            if not isinstance(param, Node):
                raise TypeError(f'"{param}" of type {type(param)} must be of type Node.')

        for child in children:
            self._children.remove(child)

    def children_count(self):
        """Returns the number of children that the node has."""
        return len(self._children)

    def is_leaf(self):
        """Returns true if the node is a leaf node (i.e. has no children) and false otherwise."""
        return self.children_count() == 0


node = Node(1)
node.add_all(Node(5), Node(8), Node(7))
print(node)
