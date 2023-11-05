# admin/folder        шлях MacOS, Linux
# c:\folder           шлях Windows     

from pathlib import Path
import sys                  

def main():
    if len(sys.argv) < 2:
        user_input = ''
    else:
        user_input = sys.argv[1]   # аргумент командного рядка
    path = Path(user_input)
    if path.exists():           # чи існує обєкт шляху
        if path.is_dir():
            items = path.glob('**/*')      # знайти файли
            for item in items:
                print(item)
        else:
            print(f'{path} is a file')


    else:
        print(f'{path.absolute()} is not_exists')       # відображає повний шлях від кореню файлової системи

    
if __name__ == "__main__":     
    main()