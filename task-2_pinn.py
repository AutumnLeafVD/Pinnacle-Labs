import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import os

class BlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Blog Application")

        # Frame for Blog Posts
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Listbox to display blog posts
        self.post_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.post_listbox.pack(side=tk.LEFT)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.post_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.post_listbox.yview)

        # Text area for editing blog post
        self.text_area = tk.Text(root, width=60, height=15)
        self.text_area.pack(pady=10)

        # Buttons for actions
        self.create_button = tk.Button(root, text="Create Post", command=self.create_post)
        self.create_button.pack(pady=5)

        self.edit_button = tk.Button(root, text="Edit Post", command=self.edit_post)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Post", command=self.delete_post)
        self.delete_button.pack(pady=5)

        self.load_posts()

    def load_posts(self):
        """ Load posts from a file """
        if os.path.exists('posts.txt'):
            with open('posts.txt', 'r') as file:
                posts = file.readlines()
                for post in posts:
                    self.post_listbox.insert(tk.END, post.strip())

    def save_posts(self):
        """ Saving posts to a file """
        with open('posts.txt', 'w') as file:
            posts = self.post_listbox.get(0, tk.END)
            for post in posts:
                file.write(post + "\n")

    def create_post(self):
        """ Creating a new blog post """
        title = simpledialog.askstring("Post Title", "Enter the title of the post:")
        if title:
            content = self.text_area.get("1.0", tk.END).strip()
            if content:
                self.post_listbox.insert(tk.END, title)
                self.save_posts()
                self.text_area.delete("1.0", tk.END)
            else:
                messagebox.showwarning("Warning", "Content cannot be empty!")

    def edit_post(self):
        """ Editing the selected blog post """
        selected_index = self.post_listbox.curselection()
        if selected_index:
            title = self.post_listbox.get(selected_index)
            content = self.text_area.get("1.0", tk.END).strip()
            if content:
                self.post_listbox.delete(selected_index)
                self.post_listbox.insert(selected_index, title)
                self.save_posts()
                self.text_area.delete("1.0", tk.END)
            else:
                messagebox.showwarning("Warning", "Content cannot be empty!")
        else:
            messagebox.showwarning("Warning", "Select a post to edit!")

    def delete_post(self):
        """ Deleting the selected blog post """
        selected_index = self.post_listbox.curselection()
        if selected_index:
            self.post_listbox.delete(selected_index)
            self.save_posts()
            self.text_area.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Warning", "Select a post to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlogApp(root)
    root.mainloop()
