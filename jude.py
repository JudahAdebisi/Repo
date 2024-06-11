def christmas_tree(height):
    """
    Prints a Christmas tree of the given height using asterisks.
    
    Args:
        height (int): The height of the Christmas tree.
    """
    # Loop for each row of the tree
    for row in range(height):
        # Print spaces for the left padding
        for space in range(height - row - 1):
            print(" ", end="")
        
        # Print asterisks for the current row
        for asterisk in range(2 * row + 1):
            print("*", end="")
        
        # Move to the next line
        print()
    
    # Print the tree trunk
    for trunk in range(3):
        print(" " * (height - 2) + "***")

# Example usage
christmas_tree(10)
