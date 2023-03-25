from decorators import expects


class TreeNode:
    """Represents a single node within a tree data structure."""

    def __init__(self, value, children=None):
        if children is None:
            children = set()
        self._value = value
        self._children = children

    def __str__(self):
        return f"({self._value}, {self._children})"

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
    def children(self) -> set:
        """Returns the set of all children of the TreeNode."""
        return self._children

    @children.setter
    @expects(set, method=True)
    def children(self, new_children: set):
        """Sets the children of the TreeNode.
        param new_children: Requires a set of TreeNodes. Raises a TypeError if this is not met.
        """
        for element in new_children:
            if not isinstance(element, TreeNode):
                TypeError(f'"{element}" of type {type(element)} must be of type Node.')
        self._children = new_children

    def add(self, new_child):
        """Adds a new child node."""
        self._children.add(new_child)

    def add_all(self, *children: tuple):
        """Adds an indefinite number of children nodes."""
        for param in children:
            if not isinstance(param, TreeNode):
                raise TypeError(f'"{param}" of type {type(param)} must be of type Node.')

        for child in children:
            self._children.add(child)

    def remove(self, child):
        """Removes the child node specified from the set of children."""
        self._children.remove(child)

    def remove_all(self, *children: tuple):
        """Removes an indefinite number of children nodes."""
        for param in children:
            if not isinstance(param, TreeNode):
                raise TypeError(f'"{param}" of type {type(param)} must be of type Node.')

        for child in children:
            self._children.remove(child)

    def children_count(self) -> int:
        """Returns the number of children that the node has."""
        return len(self._children)

    def is_leaf(self) -> bool:
        """Returns true if the node is a leaf node (i.e. has no children) and false otherwise."""
        return self.children_count() == 0


class BinaryTreeNode:
    """Represents a single node within a binary tree."""

    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def __str__(self):
        return f"({self._value}, {self._left}, {self._right})"

    def __repr__(self):
        return f"Node(value={self._value}, left={self._left}, right={self._right})"

    @property
    def value(self):
        """Returns the value of the TreeNode."""
        return self._value

    @value.setter
    def value(self, new_name):
        """Sets the value of the TreeNode."""
        self._value = new_name

    @property
    def left(self) -> BinaryTreeNode:
        """Returns the value of left."""
        return self._left

    @left.setter
    @expects(BinaryTreeNode)
    def left(self, new_left):
        """Sets the value of left."""
        self._left = new_left

    @property
    def right(self) -> BinaryTreeNode:
        """Returns the value of left."""
        return self._right

    @right.setter
    @expects(BinaryTreeNode)
    def right(self, new_right):
        """Sets the value of left."""
        self._right = new_right

    def children_count(self) -> int:
        """Returns the number of children that the node has."""
        count = 0
        if self._right is not None:
            count += 1
        if self._left is not None:
            count += 1
        return count

    def is_leaf(self) -> bool:
        """Returns true if the node is a leaf node (i.e. has no children) and false otherwise."""
        return self.children_count() == 0


def main():
    my_node = TreeNode(5, {
        TreeNode(1),
        TreeNode(4, {
            TreeNode(8), TreeNode(10)
        }),
        TreeNode(2, {
            TreeNode(13)
        }),
        TreeNode(10),
    })
    print(str(my_node))


if __name__ == "__main__":
    main()
