import pytest
from src.longest_common_substring import find_longest_common_substring

def test_basic_common_substring():
    """Test finding a basic common substring"""
    assert find_longest_common_substring("hello", "world") == ""
    assert find_longest_common_substring("hello", "hell") == "hell"
    assert find_longest_common_substring("programming", "program") == "program"

def test_identical_strings():
    """Test when strings are identical"""
    assert find_longest_common_substring("python", "python") == "python"

def test_partial_match():
    """Test finding partial common substring"""
    assert find_longest_common_substring("abcdef", "bcd") == "bcd"
    assert find_longest_common_substring("mississippi", "sip") == "sip"

def test_empty_strings():
    """Test handling of empty strings"""
    assert find_longest_common_substring("", "") == ""
    assert find_longest_common_substring("hello", "") == ""
    assert find_longest_common_substring("", "world") == ""

def test_no_common_substring():
    """Test when there's no common substring"""
    assert find_longest_common_substring("abc", "xyz") == ""

def test_multiple_common_substrings():
    """Test finding the longest substring when multiple exist"""
    assert find_longest_common_substring("abcdaf", "zbcdx") == "bcd"

def test_case_sensitivity():
    """Test case sensitivity of substring matching"""
    assert find_longest_common_substring("Hello", "hello") == ""  # Different cases
    assert find_longest_common_substring("HeLLo", "heLLo") == ""  # Different cases
    assert find_longest_common_substring("Hello", "Hello") == "Hello"  # Exact same case
    assert find_longest_common_substring("hello", "Hello") == ""  # Case mismatch

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_longest_common_substring(123, "hello")
    with pytest.raises(TypeError):
        find_longest_common_substring("hello", [1, 2, 3])
    with pytest.raises(TypeError):
        find_longest_common_substring(None, "test")