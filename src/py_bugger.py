import argparse


parser = argparse.ArgumentParser()

parser.add_argument(
    "-e",
    "--exception-type",
    type=str,
    help="What kind of exception to induce.",
    )

args = parser.parse_args()

if args.exception_type:
    print(f"args: exception_type: {args.exception_type}")