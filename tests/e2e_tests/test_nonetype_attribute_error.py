"""Test for NoneTypeAttributeError bugs.

- Copy sample code to a temp dir.
- Run py-bugger against that code.
- Verify correct exception is raised.
"""

import shutil
import shlex
import subprocess
from pathlib import Path


def test_nonetype_attribute_error(tmp_path_factory, e2e_config):
    """py-bugger --exception-type NoneTypeAttributeError"""

    # Create a simple script with direct function call attribute access
    tmp_path = tmp_path_factory.mktemp("nonetype_test")
    print(f"\nCreating test in: {tmp_path.as_posix()}")
    
    test_script = '''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_info(self):
        return f"{self.name} is {self.age} years old"


def create_person(name, age):
    """Create and return a Person object."""
    return Person(name, age)


# Direct function call attribute access
print(f"The person's name is {create_person('Bob', 25).name}")
'''
    
    path_dst = tmp_path / "direct_attribute_access.py"
    path_dst.write_text(test_script)

    # Run py-bugger against directory
    cmd = f"py-bugger --exception-type NoneTypeAttributeError --target-dir {tmp_path.as_posix()}"
    cmd_parts = shlex.split(cmd)
    stdout = subprocess.run(cmd_parts, capture_output=True).stdout.decode()

    assert "All requested bugs inserted." in stdout

    # Verify the file was modified
    modified_source = path_dst.read_text()
    
    # The function should have been modified to have a bare return
    assert "def create_person" in modified_source
    assert "return Person(name, age)" not in modified_source
    assert "return" in modified_source
    
    # Run file, should raise AttributeError on NoneType
    cmd = f"{e2e_config.python_cmd.as_posix()} {path_dst.as_posix()}"
    cmd_parts = shlex.split(cmd)
    result = subprocess.run(cmd_parts, capture_output=True)
    stdout = result.stdout.decode()
    stderr = result.stderr.decode()
    
    print(f"Script stdout: {stdout}")
    print(f"Script stderr: {stderr}")
    
    assert "Traceback (most recent call last)" in stderr
    assert "AttributeError: 'NoneType' object has no attribute " in stderr

    # Read modified file; should have changed the create_person function
    modified_source = path_dst.read_text()
    # The function should now have a bare return statement
    assert "def create_person" in modified_source
    assert "return Person(name, age)" not in modified_source
    assert "return" in modified_source