import argparse

argparser = argparse.ArgumentParser(description = "this is wrong command")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True