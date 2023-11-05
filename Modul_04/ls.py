import sys

from pathlib import Path

def main(argv):
    print(f"Function argv {argv}")
    print("-------------------------------")

    for i in argv:
        path = Path(i)

        if not path.exists():
            print(f"Warning: {path.absolute()} is not found")
        else:
            if path.is_dir():
                for i in path.iterdir():
                    print(i.name)
            else:
                print(path.name)


if __name__ == "__main__":
    print(f"Usage: python 3 {sys.argv[0]} path/to/file")
    print(f"Initial argv {sys.argv[0]}")

    main(sys.argv[1:])