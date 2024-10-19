from colorama import Fore
from pathlib import Path
import sys

path = sys.argv[1]
parent_folder_path = Path(path)

def main(path):
    'Function to analyze directory'
    try:
        for element in path.iterdir():
            if element.is_dir():
                print (Fore.GREEN + ' ' + f'{element.name}')
                main(element)
            if element.is_file():
                print(Fore.LIGHTCYAN_EX + ' ' + f'{element.name}')
    except (NotADirectoryError, FileNotFoundError):
        print(Fore.RED + 'There is no such directory!')
         

main(parent_folder_path)



