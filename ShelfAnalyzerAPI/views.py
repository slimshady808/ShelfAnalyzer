from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import identify_brands, identify_shape, identify_location


@api_view(['POST'])
def analyze_shelf(request):
    """
    Analyzes a shelf layout and identifies the shape and location of each brand.

    Args:
        request (HttpRequest): The HTTP POST request containing the shelf layout data.
    
    Returns:
        Response: A JSON response with the identified brand shapes and locations.


    """
    try:
        # Get the 2D array from the request data
        shelf_layout = request.data

        # Check if the received data is a valid 2D array
        if not isinstance(shelf_layout, list) or not all(isinstance(row, list) for row in shelf_layout):
            return Response({"error": "Invalid input format. Please provide a 2D array."}, status=status.HTTP_400_BAD_REQUEST)

        # Identify unique brands on the shelf
        brands = identify_brands(shelf_layout)

        # Create a dictionary to store the results
        results = {}

        # Iterate through each brand and identify its shape and location
        for brand in brands:
            # Find the coordinates of each instance of the brand
            brand_coordinates = [(row_idx, col_idx) for row_idx, row in enumerate(shelf_layout) for col_idx, cell in enumerate(row) if cell == brand]
            # Identify the shape and location of the brand
            shape = identify_shape(brand_coordinates)
            location = identify_location(brand_coordinates,shelf_layout)
            
            # Store the results in the dictionary
            results[brand] = {'shape': shape, 'location': location}
            
        # Return the results as a JSON response
        return Response(results, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
