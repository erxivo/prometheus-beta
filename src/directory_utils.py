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
        
        # Get the parent directory
        parent_dir = os.path.dirname(normalized_path)
        
        # Check write permissions on parent directory
        if not os.access(parent_dir, os.W_OK):
            raise PermissionError(f"No write permission for parent directory {parent_dir}")
        
        # Create the directory (with parents if needed)
        os.makedirs(normalized_path, exist_ok=False)
        
        return normalized_path
    
    except PermissionError:
        raise
    except FileExistsError:
        raise
    except OSError as e:
        # Convert other OS-related errors to PermissionError if appropriate
        if e.errno in [13, 30]:  # Permission denied or Read-only file system
            raise PermissionError(f"Could not create directory {path}: {str(e)}")
        raise