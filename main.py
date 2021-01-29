from time import time
from download import Download

import json

def main():
    initial_time = time()
    print(f'Run...')

    descargas = Download('config.json')

    descargas.checkFolders()
    descargas.scanFolder()
    
    final_time = time()
    total_time = final_time - initial_time
    print(f'End - Time: {total_time} seconds')

if __name__ == "__main__":
    main()
