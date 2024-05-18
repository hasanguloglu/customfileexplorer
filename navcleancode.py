import os
import time
from simple_term_menu import TerminalMenu
from pathlib import Path
import folder_manager

def absolute_folder_paths(directory):
    import glob
    path = os.path.abspath(directory)
    return sorted([os.path.basename(item) for item in glob.glob(f"{path}/*") if os.path.isdir(item) if not "__" in item])

def get_folder_and_actions (folder_path):
    actions = ["[a]..", "", "[f] Folder Organize", "[s] Slugify Files", ""]
    return actions + absolute_folder_paths(folder_path)

def menu_generate(options, title = None):
    terminal_menu = TerminalMenu(options, skip_empty_entries = True, title=title)
    return terminal_menu

def show_folder(options): 
    terminal_menu = menu_generate(options)
    menu_entry_index = terminal_menu.show()
    main_menu_exit = False
    path_info = Path(__file__).resolve().parent

    while not main_menu_exit:
        if menu_entry_index == 0:
            path_info = path_info.parent
            print(path_info)
            options = get_folder_and_actions(path_info)  
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
            
        if menu_entry_index > 4: 
            path_info = path_info.joinpath(options[menu_entry_index]).resolve()
            options = get_folder_and_actions(path_info)
        title = f"Title: {os.path.basename(path_info)}"
        terminal_menu = menu_generate(options, title=title)       
        menu_entry_index = terminal_menu.show()

show_folder(get_folder_and_actions("."))


