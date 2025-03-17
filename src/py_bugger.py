import ast
import os
import random
from pathlib import Path

import cli


class ImportModifier(ast.NodeTransformer):
    """Modify imports in the user's project."""

    def visit_Import(self, node):
        """Modify a direct `import <package>` statement."""
        if node.names:
            print(node)
            breakpoint()

        return node


def main():

    args = cli.parse_cli_args()

    if args.exception_type == "ModuleNotFoundError":
        print("Introducing a ModuleNotFoundError...")

        # Get the first .py file in the project's root dir.
        path_project = Path(os.getcwd())
        py_files = path_project.glob("*.py")
        path = next(py_files)

        # Read user's code.
        source = path.read_text()
        tree = ast.parse(source)

        # Modify user's code.
        tree = ImportModifier().visit(tree)
        source_modified = ast.unparse(tree)

        # Rewrite user's code.
        path.write_text(source_modified)

        print("  Modified file.")


if __name__ == "__main__":
    main()