import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame

# Initialize pygame mixer
pygame.mixer.init()

sounds = []  # List to store sound objects

# Define the directory to save sound files
SAVE_DIR = "saved_sounds"

# Function to play sound based on index
def play_sound(index):
    if 0 <= index < len(sounds):
        sounds[index].play()

# Function to stop all currently playing sounds
def stop_all_sounds():
    pygame.mixer.stop()

# Function to add new sound file to the soundboard
def add_new_sound():
    file_path = filedialog.askopenfilename()
    if file_path:
        new_sound = pygame.mixer.Sound(file_path)
        sounds.append(new_sound)
        print("New sound added to the soundboard.")
        
        # Create a new button for the newly added sound
        new_sound_name = file_path.split("/")[-1]  # Extract sound name from file path
        new_sound_button = ttk.Button(root, text=new_sound_name, command=lambda idx=len(sounds)-1: play_sound(idx), style="Dark.TButton")
        new_sound_button.pack(pady=10)

# Create the UI with tkinter
root = tk.Tk()
root.title("Soundboard App")
root.geometry("800x600")  # Larger window size

# Configure the style for Dark Mode
style = ttk.Style()
style.theme_use('clam')  # Use the 'clam' theme for a clean and minimalistic design
style.configure('Dark.TButton', foreground='white', background='#818589', font=('Helvetica', 12))

# Button to stop all sounds
stop_button = ttk.Button(root, text="Stop All Sounds", command=stop_all_sounds, style="Dark.TButton")
stop_button.pack(pady=20)

# Button to add new sound
add_button = ttk.Button(root, text="Add New Sound", command=add_new_sound, style="Dark.TButton")
add_button.pack(pady=20)

# Set background color of the root window
root.configure(background='#818589')

# Start the UI main loop
root.mainloop()