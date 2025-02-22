import os
import pytest
import shutil
from src.directory_utils import create_directory

def test_create_directory_success(tmp_path):
    """Test creating a new directory successfully."""
    test_dir = tmp_path / "new_directory"
    result = create_directory(str(test_dir))
    
    assert os.path.exists(test_dir)
    assert os.path.isdir(test_dir)
    assert result == str(test_dir)

def test_create_directory_nested(tmp_path):
    """Test creating a nested directory."""
    test_dir = tmp_path / "parent" / "child" / "grandchild"
    result = create_directory(str(test_dir))
    
    assert os.path.exists(test_dir)
    assert os.path.isdir(test_dir)
    assert result == str(test_dir)

def test_create_existing_directory(tmp_path):
    """Test that creating an existing directory raises FileExistsError."""
    existing_dir = tmp_path / "existing_dir"
    existing_dir.mkdir()
    
    with pytest.raises(FileExistsError):
        create_directory(str(existing_dir))

def test_create_directory_invalid_path():
    """Test creating a directory with an invalid path."""
    with pytest.raises(PermissionError):
        create_directory("/root/forbidden_dir")