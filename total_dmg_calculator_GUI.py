import tkinter as tk
from tkinter import messagebox

# Diablo IV TotalDmg Calculator

# Define the calculate_damage function
def calculate_damage():
    # Convert the user input to numbers
    weapon_dps = int(weapon_dps_entry.get())
    skill_modifier = float(skill_modifier_entry.get()) / 100
    dexterity = int(dexterity_entry.get())

    # Calculate the base damage
    base_damage = weapon_dps * skill_modifier

    # Calculate the dexterity damage modifier
    dex_damage_modifier = (dexterity * 0.1)

    # Calculate the total damage
    total_damage = base_damage + dex_damage_modifier

    # Display the results in a message box
    messagebox.showinfo("Damage", "Weapon DPS - {} \nSkill Modifier - {} \nDexterity - {} \n\nBase Damage =  {} \nDexterity Modifier =  +{}% \nTotal Damage Per Second =  {}".format(weapon_dps, skill_modifier, dexterity, round(base_damage, 2), round(dex_damage_modifier, 2), round(total_damage, 2)))

    # Close the main window
    root.destroy()

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Diablo IV Total Damage Calculator")

# Set the window size
root.geometry("390x164")

# Create the labels for the three input fields
weapon_dps_label = tk.Label(root, text="Weapon DPS: ")
skill_modifier_label = tk.Label(root, text="Skill Modifier Percentage: ")
dexterity_label = tk.Label(root, text="Dexterity: ")

# Create the input fields for the three values
weapon_dps_entry = tk.Entry(root)
skill_modifier_entry = tk.Entry(root)
dexterity_entry = tk.Entry(root)

# Set the focus to the first input field
weapon_dps_entry.focus_set()

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=calculate_damage)

# Layout the labels and input fields
weapon_dps_label.grid(row=0, column=0)
weapon_dps_entry.grid(row=0, column=1)
skill_modifier_label.grid(row=1, column=0)
skill_modifier_entry.grid(row=1, column=1)
dexterity_label.grid(row=2, column=0)
dexterity_entry.grid(row=2, column=1)
submit_button.grid(row=3, column=0)

# Start the main loop
root.mainloop()