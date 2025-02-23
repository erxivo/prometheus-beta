def find_longest_common_substring(str1, str2):
    """
    Find the longest common substring between two input strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: The longest common substring
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store lengths of common substrings
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0
    
    # Dynamic programming approach to find longest common substring
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # Explicitly check exact character match (case-sensitive)
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                
                # Update max length and end index if needed
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_index = i
    
    # Return the longest common substring
    return str1[end_index - max_length:end_index] if max_length > 0 else ""