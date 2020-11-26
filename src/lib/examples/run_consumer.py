from lib.consumer import consumer
import argparse

parser = argparse.ArgumentParser('REPL')
parser.add_argument("--sleep_interval",
                    type=float,
                    help="Sleep interval in seconds",
                    default=1.0)
args = parser.parse_args()

if __name__ == "__main__":
    consumer(args.sleep_interval)
