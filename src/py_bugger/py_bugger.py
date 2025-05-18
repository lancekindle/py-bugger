import os
import random

from py_bugger import buggers
from py_bugger.utils import file_utils

from py_bugger.cli.config import pb_config
from py_bugger.cli import cli_messages


# Set a random seed when testing.
if seed := os.environ.get("PY_BUGGER_RANDOM_SEED"):
    random.seed(int(seed))


def main():
    print("Starting py-bugger with exception type:", pb_config.exception_type)
    
    # Get a list of .py files we can consider modifying.
    py_files = file_utils.get_py_files(pb_config.target_dir, pb_config.target_file)
    print(f"Found {len(py_files)} Python files to consider")
    for file in py_files:
        print(f"  - {file}")

    # Track how many bugs have been added.
    bugs_added = 0

    # Currently, handles just one exception type per call.
    # When multiple are supported, implement more complex logic for choosing which ones
    # to introduce, and tracking bugs. Also consider a more appropriate dispatch approach
    # as the project evolves.
    if pb_config.exception_type == "ModuleNotFoundError":
        print("Running ModuleNotFoundError bugger")
        new_bugs_made = buggers.module_not_found_bugger(py_files)
        bugs_added += new_bugs_made
    elif pb_config.exception_type == "AttributeError":
        print("Running AttributeError bugger")
        new_bugs_made = buggers.attribute_error_bugger(py_files)
        bugs_added += new_bugs_made
    elif pb_config.exception_type == "IndentationError":
        print("Running IndentationError bugger")
        new_bugs_made = buggers.indentation_error_bugger(py_files)
        bugs_added += new_bugs_made
    elif pb_config.exception_type == "NoneTypeAttributeError":
        print("Running NoneTypeAttributeError bugger")
        new_bugs_made = buggers.nonetype_attribute_error_bugger(py_files)
        bugs_added += new_bugs_made
    else:
        print(f"Unknown exception type: {pb_config.exception_type}")

    # Show a final success/fail message.
    msg = cli_messages.success_msg(bugs_added, pb_config.num_bugs)
    print(msg)
