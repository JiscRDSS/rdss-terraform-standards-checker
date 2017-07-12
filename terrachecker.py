import logging
import argparse
import sys

from app import TerraformChecker


def main():
    """Main function"""

    args = parse_args()

    checker = TerraformChecker(args.terraform_path)
    if not checker.is_valid():
        for error in checker.validation_errors:
            print('{}: {}'.format(error['path'], error['error']))
        sys.exit(1)

    sys.exit(0)


def parse_args():
    """Setup the argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "terraform_path",
        help="Path to directory containing Terraform configs."
    )
    return parser.parse_args()


if __name__ == '__main__':
    main()
