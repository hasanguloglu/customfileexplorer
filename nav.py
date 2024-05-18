# 25.04.2024_ExplorerProject 4. DERS

# simple-term-menu kütüphanesi --> terminal submenu / mainmenu ararken çıkıyor.

# bir gui'ye bağlanabilir yazılan kod. Mouse ile işlem yapılabile.
    #* PyQT5, Tkinter, Kivy, Simple Gui 

# Total commander benzeri bir uygulama yapacağız, 

#^ Breadcrumbs -- Hansel ve Gretel masalında iki kardeşin eve dönüş yolunu hatırlamak için yerlere serptiği ekmek kırıntılarından faydalanmalarına dayanır.

#! back tuşu bir üst klasöre geç demek değildir. En sona geri dön anlamına gelir.

from simple_term_menu import TerminalMenu
import time
import os
from pathlib import Path
import pathlib
import folder_manager

# BASE_DIR = Path(__file__).resolve().parent.parent
# def main(): 
#     options = ["entry 1", "entry 2", "entry 3"]
#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show()
#     print(f"You have selected {options[menu_entry_index]}!")

# main() --> bir liste var oradan seçenekleri alıyor ve endeksine göre gösteriyor.

# dinamik bir liste yapsam ve optionsa koysam dosyaları seçtirebilirim.
import os

folders = [item for item in os.listdir('.') if os.path.isdir(item)] 

def show_folder(options): 
    options = options
    terminal_menu = TerminalMenu(options, skip_empty_entries = True)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

# üst klasöre geçmek istiyorum. Yapabileceklerimi yapmak istiyorum
upfolder = ["[a]..", ""] # total commanderdaki gibi üst menüye gitmek için

actions = ["", "[f] Folder Organize", "[s] Slugify Files"]

options = upfolder + folders + actions # her zaman son iki tanesi actionlar oluşturur.

# NOT : mac ve linuxta Cat preview gösterir, içindekiler döker. Windowsta da Bat kütüphanesini alıp yapmışlar. 

#* NOT: if __name__ = "__main__" dersek bu dosya import edilerek çalışmaz. __name__ aslında tüm dosyalarda __main__ geçer. bu dosyayı çağırırsan çalış diyor. Tüm dosyalar classtır. OOP diye bir dosya açsam ve içine _init.py__ oluştursam klasörü import edip çalıştırabilir. Klasör ilk çağrıldığında init işleri yapılır. 
# * CLASS OOP:
# *       def __init__(self):
# *               print("Hello")



#! folders = [os.path.basename(f) for f in os.scandir(folder_path) if f.is_dir()]

def absolute_folder_paths(directory):
    path = os.path.abspath(directory)
    return sorted([entry.path for entry in os.scandir(path) if entry.is_dir() if not "__" in entry.path])


def get_folder_and_actions (folder_path): # dinamik hale getirmeliyim.
    actions = ["[a]..", "", "[f] Folder Organize", "[s] Slugify Files", ""]
    #* folders = [item for item in os.listdir(folder_path) if os.path.isdir(item) and not "__" in item] 
    #? if koşuluyla beraber subfolderları getirmiyor. dolayısıyla değiştiriyoruz. yukardaki fonksiyonlar birleştiriyoruz.
    return actions + absolute_folder_paths(folder_path)

def menu_generate(menu_options_list, title = None):
    terminal_menu = TerminalMenu(menu_options_list, skip_empty_entries = True, title = title)
    return terminal_menu

def show_folder(options): 
    # TODO: terminal_menu = TerminalMenu(options, skip_empty_entries = True) bu her zaman gerekeceği için fonk yazıp koyalım
    terminal_menu = menu_generate(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    main_menu_exit = False
    path_info = Path(__file__).resolve().parent # başta parent almazsak ilk 0 bastığımda üste gitmez. Zaten diğer 0 hariç seçeneklere basınca path değişiyor.  

    while not main_menu_exit:
# BASE_DIR = Path(__file__).resolve().parent.parent bir üst menü için Djangodaki yapı
# resolve dosyanın yolunu söylüyor, parent ise bir üst klasörünü buluyor
        if menu_entry_index == 0:
            # Path(options[5]).resolve().parent bir üst klasörü alsa da options buna bağımlı olacak
            path_info = Path(path_info).resolve().parent
            # options = get_folder_and_actions(Path(path_info).resolve().parent) # path_infonun değişmesi gerek
            options = get_folder_and_actions(path_info)
            # terminal_menu = menu_generate(options, title = f"Title: {str(path_info)}")
            # menu_entry_index = terminal_menu.show()  #! refactor ederken ihtiyaç yok

        if menu_entry_index == 2:
            print("Folder Organize")
            title = f"Folder Organize..: {path_info}" 
            with open('lorem.txt', 'w') as file:
                folder = folder_manager.FolderOrganize(path_info)
                file.write(f"{folder.is_folder_organize()} {path_info}")

        if menu_entry_index == 3:
            title = f"Make Slugify Files: {path_info}"

            folder = folder_manager.FolderOrganize(path_info)
            folder.make_slugify_files()
            

        if menu_entry_index > 4: # çünkü sub menü index 5ten başlıyor
            path_info = options[menu_entry_index]
            options = get_folder_and_actions(options[menu_entry_index]) # 6 numaralı endeks olan documents get_folder_and_actions'a gider.
        title = f"Title: {path_info}"
        terminal_menu = menu_generate(options, title=title)       
        menu_entry_index = terminal_menu.show()
    



        

show_folder(get_folder_and_actions("."))













#! SUB Menu ilham alacağımız kısım
import time

from simple_term_menu import TerminalMenu

def main():
    main_menu_title = "  Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_items = [item for item in os.listdir('.') if os.path.isdir(item)] 
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    edit_menu_title = "  Edit Menu.\n  Press Q or Esc to back to main menu. \n"
    edit_menu_items = ["[f] Folder Organize", "[s] Slugify Files"]
    edit_menu_back = False
    edit_menu = TerminalMenu(
        edit_menu_items,
        title=edit_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            while not edit_menu_back:
                edit_sel = edit_menu.show()
                if edit_sel == 0:
                    print("Edit Config Selected")
                    time.sleep(5)
                elif edit_sel == 1:
                    print("Save Selected")
                    time.sleep(5)
                elif edit_sel == 2 or edit_sel == None:
                    edit_menu_back = True
                    print("Back Selected")
            edit_menu_back = False
        elif main_sel == 1:
            print("option 2 selected")
            time.sleep(5)
        elif main_sel == 2:
            print("option 3 selected")
            time.sleep(5)
        elif main_sel == 3 or main_sel == None:
            main_menu_exit = True
            print("Quit Selected")
