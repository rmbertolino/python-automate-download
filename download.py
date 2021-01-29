import os
import shutil
import json
class Download():
    def __init__(self, fileConfig):
        config = self.__getConfig('config.json')

        self.path_download = config['CONFIG']['PATHS']['Download']
        self.folders_destination = config['CONFIG']['FOLDERS']

    def __str__(self):
        return self.path_download

    def checkFolders(self):
        for folder in self.folders_destination:
            if not self.__folderIsCreated(folder):
                self.__createFolder(folder)

    def scanFolder(self):
        for item in os.listdir(self.path_download):
            if os.path.isfile(os.path.join(self.path_download, item)):
                name, ext = os.path.splitext(item)
                self.__sortFile(name, ext)

    def __folderIsCreated(self, folder):
        if os.path.isdir(self.path_download + folder):
            return True
        else:
            return False

    def __createFolder(self, folder):
        os.mkdir(self.path_download + folder)

    def __moveFile(self, file, destination):
        shutil.move(os.path.join(self.path_download, file), os.path.join(self.path_download + destination, file))
        print(f'File: {file} movido a {destination}')

    def __sortFile(self, file, ext):
        for folder in self.folders_destination:
            for extension in self.folders_destination[folder]:
                if extension == ext:
                    self.__moveFile(file+ext, folder)
                    return True
        return False

    def __getConfig(self, fileConfig):
        with open(fileConfig, 'r') as f:
            config = json.load(f)

        return config