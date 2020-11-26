from lib.producer import checker
import argparse

parser = argparse.ArgumentParser('REPL')
parser.add_argument("url")
parser.add_argument("--regexp", type=str,
                    help="Optional regexp pattern",
                    default=None,
                    )
parser.add_argument("--sleep_interval",
                    type=float,
                    help="Sleep interval in seconds",
                    default=1.0,
                    )
args = parser.parse_args()

if __name__ == "__main__":
    checker(args.url, sleep_interval=args.sleep_interval,
            regexp_pattern=args.regexp)
