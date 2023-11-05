from py_1 import get_name

def goodbye(name):
    print(f'Good bye {name}')


def main():
    name = get_name()
    goodbye(name)


if __name__ == "__main__":     # не прошел проверку, ОБЩЕПРИНЯТОЕ ПРАВИЛО!!!

    print(f'__name__  == {__name__}')
    main()

 