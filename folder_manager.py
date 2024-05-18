# bazi dosya uzantilari bilinmiyor olabilir ? 
# OK --- bu klasor organize mi ? 
# bu klasorde bilinmeyen dosya uzantilari va mi ?
# dosyalari organize et
# hangi klasordeyiz ? 

# gui (graphic user interface) ile eşleştirildiğinde file manager olur. 
  # 'Typer' terminal interface, gui çok maliyetlidir.
  # Linux tercih edilir çok büyük işler yapılır, yer kaplamaz.
  # django guisi son kullanıcı içindir, developerda gui yoktur.
    # terminalde ports'a 8000 yazılırsa bir adres açılır bu projeyi yayına almadan başkalarıyla paylaşmayı sağlar.

# tui - text user interface - Nano

# cli - command line interface ( siyah ekran )


class FolderOrganize:
    """
    FolderOrganize Class Yapisi Bir Folderda Asagidaki islemleri yapar..
    """
    import os
    
    IGNORED_FILE_TYPES = ['py', 'exe', 'app', 'sqlite3'] # geri kalan varsa organize değil

    FILE_TYPES = {
        "xls": "Sheets",
        "xlsx": "Sheets",
        "doc": "Documents",
        "docx": "Documents",
        "txt": "Documents",
        "pdf": "Documents",
        "jpg": "Pictures",
        "mp3": "Musics",
    }

    # initial method olmalı mı? 
    def __init__(self, folder_path):
        #* init bulunduğumuz klasörü alabilir. 
        self.folder_path = folder_path # path verebilir veya
        # self.folder_path = input("Folder Path Bilgisini Giriniz..: ")

        if not self.is_folder_path_correct(): #^ Klasör yoksa 
            raise ValueError("Klasor Bilgisi Dogru Degildir..")

        # os.path.isdir('/') --> True döner / -> "root" demektir.
        # Linuxda C D sürücüleri yok, her şey roottan başlar volumelara tabidir.

    def is_folder_path_correct(self): #^ Klasör var mı kontrol etmeliyim
        return self.os.path.isdir(self.folder_path)
    
    
    def is_folder_organize(self):
        """
        is_folder_organize check islemi folder bilgisinin organize olup olmadigini kontrol eder
        """
        file_types = self.get_file_types()
        
        for item in file_types:
            if not item in self.IGNORED_FILE_TYPES:
                return False
        return True
    
    # def is_folder_organize(self): önce böyle yazmıştık sonra ayrı bir methoda aldık
        self.os.listdir(self.folder_path) # dosyalara ulaşır
        files = [
            item for item in self.os.listdir(self.folder_path) 
            if not item.startswih('.') and self.os.path.isfile(item)
        ]
        file_types = list()
        for file in files:
            try:
                file_types.append(file.split('.')[1])
            except:
                pass
        for item in file_types:
            if not item in self.IGNORED_FILE_TYPES:
                return False
        return True

    def get_files(self):   
        import glob, os
        return [
            os.path.basename(item) for item in glob.glob(f"{self.folder_path}/*")
            if not item.startswith('.') and  
                self.os.path.isfile(item) and 
                len(item.split('.')) == 2  
        ]
        # return [
        #     item for item in self.os.listdir(self.folder_path) 
        #     if not item.startswith('.') and  #* cache dosyaları . ile başlar
        #         self.os.path.isfile(item) and #* folderları getirmemeli file getirmeli
        #         len(item.split('.')) == 2 #* dosyada tek nokta olmalı. 
        # ]
    
    def get_organizable_files(self):
        files = self.get_files()
        return [
            file for file in files
            if not file.split('.')[1] in self.IGNORED_FILE_TYPES
        ]
    
    def make_slugify_files(self):
        from slugify import slugify
        import pathlib
        files = self.get_organizable_files()
        with open('slugify.txt', 'w') as file:
            file.write(f"{self.folder_path} \n")
            
            for item in files:
                file.write(f"{slugify(item.split('.')[0])} \n")

    def get_file_types(self):
        files = self.get_files()
        file_types = set() #* aynı uzantıları tekleştirmek için set kullanırız.
        for file in files:
            try:
                file_types.add(file.split('.')[1])
            except:
                pass
        return list(file_types)
    
    def has_folder_unknown_file_types(self):
        file_types = self.get_file_types()
        for file_type in file_types:
            if not file_types in list(self.FILE_TYPES.keys()):
                return True
        return False
    

    def create_folder(self):
        file_types = self.get_file_types()
        for file_type in file_types:
            folder_name = self.FILE_TYPES.get(file_type, 'Unknown')
            if not self.os.path.isdir(folder_name):
                self.os.mkdir(folder_name)
        return 
    
    # def organize(self): önce böyle yazmıştık 
        import shutil
        files = self.get_organizable_files()
        for file in files:
            file_type = file.split('.')[1]
            folder_name = self.FILE_TYPES.get(file_type, "Unknown")
            if not self.os.path.isdir(folder_name):
                self.os.mkdir(folder_name)  #* folder yoksa üret.
            shutil.move(file, f"{folder_name}/{file}")

    def organize(self):
        import shutil
        files = self.get_organizable_files()
        self.create_folder()
        
        for file in files:
            file_type = file.split('.')[1]
            folder_name = self.FILE_TYPES.get(file_type, 'Unknown')
            shutil.move(file, f"{folder_name}/{file}")

    


