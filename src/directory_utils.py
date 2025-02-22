import os

def create_directory(path):
    """
    Create a new directory at the specified path.
    
    Args:
        path (str): The path of the directory to create.
    
    Raises:
        FileExistsError: If the directory already exists
        PermissionError: If there are insufficient permissions to create the directory
    
    Returns:
        str: The path of the created directory
    """
    try:
        # Normalize the path to handle relative paths
        normalized_path = os.path.normpath(path)
        
        # Check if directory already exists
        if os.path.exists(normalized_path):
            raise FileExistsError(f"Directory {normalized_path} already exists")
        
        # Create the directory (with parents if needed)
        os.makedirs(normalized_path, exist_ok=False)
        
        return normalized_path
    
    except (OSError, PermissionError) as e:
        # Re-raise with more context
        raise type(e)(f"Could not create directory {path}: {str(e)}")