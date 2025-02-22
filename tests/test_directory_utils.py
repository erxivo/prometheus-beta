import os
import pytest
import stat
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

def test_create_directory_no_permission(tmp_path):
    """Test creating a directory without permissions."""
    # Create a directory and remove write permissions
    no_perm_dir = tmp_path / "no_perm_dir"
    no_perm_parent = tmp_path / "no_perm_parent"
    no_perm_parent.mkdir()
    no_perm_parent.chmod(0o555)  # Read and execute permissions only
    
    with pytest.raises(PermissionError):
        create_directory(str(no_perm_parent / "test_dir"))