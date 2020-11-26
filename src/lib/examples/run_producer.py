from lib.producer import checker
import argparse

parser = argparse.ArgumentParser('REPL')
parser.add_argument("url")
args = parser.parse_args()

if __name__ == "__main__":
    checker(args.url)
