import sys
import pathlib


def print_file_name(file_name, full_name=False, margin=0, margin_item=" "):
    margin = margin * margin_item
    if full_name:
        print(margin + str(file_name.absolute()))
    else:
        print(margin + str(file_name.name))


def main():
    file_name = pathlib.Path(sys.argv[1])
    print_file_name(file_name, full_name=True, margin_item='*', margin=30)
    










if __name__ == "__main__":     # ОБЩЕПРИНЯТОЕ ПРАВИЛО!!!
    main()