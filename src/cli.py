import argparse


def parse_cli_args():
    """Parse all options for the CLI."""
    parser = argparse.ArgumentParser(
        description="Practice debugging, by intentionally introducing bugs into an existing codebase."
    )

    parser.add_argument(
        "-e",
        "--exception-type",
        type=str,
        help="What kind of exception to induce.",
    )

    args = parser.parse_args()

    return args
