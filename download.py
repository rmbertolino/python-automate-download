import os
import shutil

class Download():
    def __init__(self, **kwargs):
        self.path_download = kwargs.get('path_download', '')
        self.ext_office = kwargs.get('ext_office', [])
        self.ext_img = kwargs.get('ext_img', [])
        self.ext_video = kwargs.get('ext_video', [])
        self.folders_destination = kwargs.get('folders_destination', [])

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
        for extension in self.ext_video:
            if extension == ext:
                self.__moveFile(file+ext, 'Videos')
                return True

        for extension in self.ext_img:
            if extension == ext:
                self.__moveFile(file+ext, 'Images')
                return True
        
        for extension in self.ext_office:
            if extension == ext:
                self.__moveFile(file+ext, 'Office')
                return True
        
        self.__moveFile(file+ext, 'Otros')
        return True