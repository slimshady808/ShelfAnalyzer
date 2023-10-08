# ShelfAnalyzerAPI/utils.py

def is_square_length(length):
    """
    Check if a given length can form a square.

    Args:
        length (int): The length to check.

    Returns:
        bool: True if the length can form a square, False otherwise.
    """
    if length <= 2:
        return False

    i = 1
    while i * i <= length:
        if i * i == length:
            return True
        i += 1

    return False



def is_isolated(coordinate, coordinates):
    """
    Check if a coordinate is isolated (not adjacent to other coordinates).

    Args:
        coordinate (tuple): The coordinate to check.
        coordinates (list of tuples): List of coordinates to check against.

    Returns:
        bool: True if the coordinate is isolated, False otherwise.
    """
    x, y = coordinate
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for neighbor in neighbors:
        if neighbor in coordinates:
            return False
    return True

def remove_isolated_coordinates(coordinates):
    """
    Remove isolated coordinates from a list of coordinates.

    Args:
        coordinates (list of tuples): List of coordinates to filter.

    Returns:
        list of tuples: List of coordinates with isolated ones removed.
    """
    updated_coordinates = []

    for coordinate in coordinates:
        if not is_isolated(coordinate, coordinates):
            updated_coordinates.append(coordinate)

    return updated_coordinates




def identify_square(cordinates):

    """
    Identify if a set of coordinates forms a square.

    Args:
        coordinates (list of tuples): List of (row, column) coordinates.

    Returns:
        bool: True if it forms a square, False otherwise.
    """
    
    if not is_square_length(len(cordinates)):
        return False
    rows = [row for (row, col) in cordinates]
    cols = [col for (row, col) in cordinates]

    # Check if the difference between max and min rows and columns is the same
    rows_diff = max(rows) - min(rows)
    cols_diff = max(cols) - min(cols)

    if rows_diff == cols_diff:
        return True
    else:
        return False
    
def identify_vertical_rectangle(cordinates):

    """
    Identify if a set of coordinates forms a vertical rectangle.

    Args:
        coordinates (list of tuples): List of (row, column) coordinates.

    Returns:
        bool: True if it forms a vertical rectangle, False otherwise.
    """

    if len(cordinates)<2:
        return False
    
    cols = [col for (row, col) in cordinates]
    if len(set(cols))==1:
        return True
    
def identify_horizontal_rectangle(cordinates):

    """
    Identify if a set of coordinates forms a horizontal rectangle.

    Args:
        coordinates (list of tuples): List of (row, column) coordinates.

    Returns:
        bool: True if it forms a horizontal rectangle, False otherwise.
    """

    if len(cordinates)<2:
        return False
    rows = [row for (row, col) in cordinates]
    if len(set(rows))==1:
        return True
    
    

    

def identify_brands(shelf_layout):

    """
    Identify unique brands on the shelf layout.

    Args:
        shelf_layout (list of lists): 2D array representing the shelf layout.

    Returns:
        list: List of unique brands found on the shelf.
    """

    unique_brands = set()
    for row in shelf_layout:
        unique_brands.update(row)
    return list(unique_brands)



def identify_shape(cordinates):

    """
    Identify the shape of a set of coordinates.

    Args:
        coordinates (list of tuples): List of (row, column) coordinates.

    Returns:
        str: The shape ('square', 'vertical rectangle', 'horizontal rectangle', or 'polygon').
    """

    updated_cordinates=remove_isolated_coordinates(cordinates)



    if identify_square(updated_cordinates):
        return 'square'
    if identify_vertical_rectangle(updated_cordinates):
        return 'vertical rectangle'
    if identify_horizontal_rectangle(updated_cordinates):
        return 'horizontal rectangle'
    else:
        return 'polygon'
    

def identify_location(brand_coordinates_list, shelf_layout):

    """
    Identify the location of a brand's area on the shelf.

    Args:
        brand_coordinates_list (list of tuples): List of (row, column) coordinates for a brand.
        shelf_layout (list of lists): 2D array representing the shelf layout.

    Returns:
        str: The location of the brand's area.
    """

    brand_coordinates=remove_isolated_coordinates(brand_coordinates_list)
    if not brand_coordinates:
        brand_coordinates=brand_coordinates_list
    # Get the dimensions of the shelf layout
    num_rows = len(shelf_layout)
    num_cols = len(shelf_layout[0]) if num_rows > 0 else 0
   
    # Check if the brand is positioned on the left boundary
    if all(col == 0 or col == 1 for row, col in brand_coordinates) and \
            set(range(num_rows)) == set([row for row, _ in brand_coordinates]):
        return 'left'

    # Check if the brand is positioned on the right boundary
    if all(col == num_cols - 1 or col==num_cols-2  for _, col in brand_coordinates) and \
            set(range(num_rows)) == set([row for row, _ in brand_coordinates]):
        return 'right'
    
    
    # Check if the brand is positioned on the top boundary
    if all(row == 0 or row==1 for row, _ in brand_coordinates) and \
            set(range(num_cols)) == set([col for _, col in brand_coordinates]):
        return 'top'

    # Check if the brand is positioned on the bottom boundary
    if all(row == num_rows - 1 or num_rows-2  for row, _ in brand_coordinates) and \
            set(range(num_cols)) == set([col for _, col in brand_coordinates]):
        return 'bottom'


    # Calculate the center point of the shelf layout
    center_row = num_rows // 2
    center_col = num_cols // 2

    # Determine the quadrant based on brand coordinates
    row, col = brand_coordinates[0]  # Assuming only one set of coordinates
    if row < center_row:
        if col < center_col:
            return 'top left'
        else:
            return 'top right'
    else:
        if col < center_col:
            return 'bottom left'
        else:
            return 'bottom right'



    



  
    

