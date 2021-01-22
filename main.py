from time import time
from download import Download

import json

def main():
    initial_time = time()
    print(f'Run')

    descargas = Download(path_download=path_download, 
                            ext_office=ext_office, 
                            ext_img=ext_img, 
                            ext_video=ext_video, 
                            folders_destination=folders_destination)

    descargas.checkFolders()
    descargas.scanFolder()
    
    final_time = time()
    total_time = final_time - initial_time
    print(f'End - Time: {total_time} seconds')


if __name__ == "__main__":
    
    file = open('config.json','r')
    config = json.load(file)
    
    path_download = config['CONFIG']['PATHS']['DOWNLOAD']
    ext_office = config['CONFIG']['EXTENSIONS']['OFFICE']
    ext_img =  config['CONFIG']['EXTENSIONS']['IMAGE']
    ext_video = config['CONFIG']['EXTENSIONS']['VIDEO']

    folders_destination = config['CONFIG']['PATHS']['DESTINATION']
  
    main()
