import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r" um ", s)
    return len(ums)


if __name__ == "__main__":
    main()