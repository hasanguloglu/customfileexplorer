from tkinter import *
import os
from pathlib import Path
import folder_manager

def absolute_folder_paths(directory):
    path = os.path.abspath(directory)
    return sorted([os.path.basename(item) for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)) and not "__" in item])

class FolderMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Browser")
        self.path_info = Path(__file__).resolve().parent
        self.create_widgets()
        self.update_listbox()
        self.listbox.focus_set()
        self.root.bind("<Escape>", self.on_escape_press)

    def create_widgets(self):
        self.label = Label(self.root, text=f"Current Folder: {self.path_info}")
        self.label.pack()

        self.listbox = Listbox(self.root, width=60, height=10)
        self.listbox.pack()
        
        self.listbox.bind("<Double-1>", self.on_double_click)
        
        self.listbox.bind('<Return>',self.on_enter_press)

        self.go_up_button = Button(self.root, text="Go Up", command=self.go_up)
        self.go_up_button.pack()

        self.organize_button = Button(self.root, text="Organize Folder", command=self.organize_folder)
        self.organize_button.pack()

        self.slugify_button = Button(self.root, text="Slugify Files", command=self.slugify_files)
        self.slugify_button.pack()

        self.select_button = Button(self.root, text="Select", command=self.select_folder)
        self.select_button.pack()


    def update_listbox(self):
        self.listbox.delete(0, END)
        folders = absolute_folder_paths(str(self.path_info))
        self.listbox.insert(END, "[Go Up]") 
        for folder in folders:
            self.listbox.insert(END, folder)
            
    def on_double_click(self, event):
        FolderMenuApp.select_folder(self)

    def on_enter_press(self, event):
        FolderMenuApp.select_folder(self)

    def go_up(self):
        new_path = self.path_info.parent
        if new_path != self.path_info:
            self.path_info = new_path
            self.label.config(text=f"Current Folder: {self.path_info}")
            self.update_listbox()
        else:
            print("Already at the root folder.")

    def organize_folder(self):
        print("Organizing folder...")
        folder_manager.FolderOrganize(self.path_info).is_folder_organize()

    def slugify_files(self):
        print("Slugifying files...")
        folder_manager.FolderOrganize(self.path_info).make_slugify_files()

    def select_folder(self):
        selected_index = self.listbox.curselection() 
        if selected_index:
            selected_text = self.listbox.get(selected_index)
            if selected_text == "[Go Up]":
                self.go_up()
            else:
                self.path_info = self.path_info.joinpath(selected_text)
                self.label.config(text=f"Current Folder: {self.path_info}")
                self.update_listbox()

    def on_escape_press(self, event):
        self.root.quit()

root = Tk()
app = FolderMenuApp(root)
root.mainloop()