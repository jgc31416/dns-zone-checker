"""Console script for dns_zone_checker."""

import fire


def help() -> None:
    print("dns_zone_checker")
    print("=" * len("dns_zone_checker"))
    print("Small tool to check DNS zone files against DNS servers")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
