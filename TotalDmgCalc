# Diablo IV TotalDmg Calculator

import tkinter as tk
from tkinter import messagebox

# Create the root window
root = tk.Tk()
root.withdraw()

# Function to handle the submit button click
def submit():
    global WeaponDmg, SkillModifier, Dexterity
    WeaponDmg = float(entry_weapon.get())
    SkillModifier = float(entry_skill.get()) / 100
    Dexterity = float(entry_dex.get())
    root.destroy()
    calculate_damage()

# Create the input dialogs
label_weapon = tk.Label(root, text="What is the Weapon DPS? (Use the max DPS from the tooltip): ")
label_skill = tk.Label(root, text="What is the skill modifier percentage?: ")
label_dex = tk.Label(root, text="Enter your Dexterity stat: ")
entry_weapon = tk.Entry(root)
entry_skill = tk.Entry(root)
entry_dex = tk.Entry(root)
button_submit = tk.Button(root, text="Submit", command=submit)

# Position the input dialogs
label_weapon.pack()
entry_weapon.pack()
label_skill.pack()
entry_skill.pack()
label_dex.pack()
entry_dex.pack()
button_submit.pack()

# Function to calculate damage
def calculate_damage():
    # Base Damage Formula
    BaseDmg = WeaponDmg * SkillModifier

    # Dex Damage Modifier Formula
    DexDmgModifier = (Dexterity * 0.1) * 100

    # Total Damage Formula
    TotalDmg = BaseDmg + DexDmgModifier

    # Create the result message box
    messagebox.showinfo("Total Damage Calculation", f"Base Damage: {BaseDmg}\nDex Damage Modifier: {DexDmgModifier}\nTotal Damage: {TotalDmg}")

# Run the main event loop
root.mainloop()
