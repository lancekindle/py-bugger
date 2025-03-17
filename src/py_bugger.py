import cli


def main():

    args = cli.parse_cli_args()

    if args.exception_type:
        print(f"args: exception_type: {args.exception_type}")

if __name__ == "__main__":
    main()