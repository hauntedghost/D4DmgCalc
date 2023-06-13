import tkinter as tk
from tkinter import messagebox

# Diablo IV TotalDmg Calculator

# Declare variables.
weapon_dps = 0
skill_modifier = 0
dex = 0
weapon_dps_entry = None
skill_modifier_entry = None
dex_entry = None
character_class_var = None
dex_label = None

def main():
    global weapon_dps_entry, skill_modifier_entry, dex_entry, character_class_var, dex_label, dex_entry

    # Create the main window.
    root = tk.Tk()

    # Set the window title
    root.title("Diablo IV Total Damage Calculator")

    # Set the window size
    root.geometry("390x200")

    # Create the labels for the user input.
    character_class_label = tk.Label(root, text="Character Class")
    weapon_dps_label = tk.Label(root, text="Weapon DPS")
    skill_modifier_label = tk.Label(root, text="Skill modifier percentage")
    dex_label = tk.Label(root, text="Character dexterity")
    dex_label.grid_forget()  # Hide the "Character Dexterity" label initially

    # Create the dropdown menu for character class selection.
    character_class_var = tk.StringVar(root)
    character_class_var.set("Barbarian")  # Set default value
    character_class_menu = tk.OptionMenu(root, character_class_var, "Barbarian", "Druid", "Necromancer", "Rogue", "Sorcerer")
    character_class_var.trace("w", on_character_class_change)

    # Create the entry boxes for the user input.
    weapon_dps_entry = tk.Entry(root)
    skill_modifier_entry = tk.Entry(root)
    dex_entry = tk.Entry(root)
    dex_entry.grid_forget()  # Hide the "Character Dexterity" entry initially

    # Create the button that will calculate the damage.
    calculate_damage_button = tk.Button(root, text="Calculate damage", command=calculate_damage)

    # Add the labels, entry boxes, and dropdown menu to the main window.
    character_class_label.grid(row=0, column=0)
    character_class_menu.grid(row=0, column=1)
    weapon_dps_label.grid(row=1, column=0)
    weapon_dps_entry.grid(row=1, column=1)
    skill_modifier_label.grid(row=2, column=0)
    skill_modifier_entry.grid(row=2, column=1)
    calculate_damage_button.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

    # Bind the Enter key to the calculate_damage function
    root.bind('<Return>', calculate_damage)

    # Start the main loop.
    root.mainloop()

def on_character_class_change(*args):
    selected_class = character_class_var.get()

    # Hide "Character Dexterity" label and entry for all classes except "Rogue"
    if selected_class != "Rogue":
        dex_label.grid_forget()
        dex_entry.grid_forget()
    else:
        dex_label.grid(row=3, column=0)
        dex_entry.grid(row=3, column=1)

def on_character_class_change(*args):
    selected_class = character_class_var.get()
    print("Selected Class:", selected_class)  # Debugging statement
    if selected_class == "Rogue":
        dex_label.grid(row=3, column=0)
        dex_entry.grid(row=3, column=1)
        print("Character Dexterity Input Shown")  # Debugging statement
    else:
        dex_label.grid_forget()
        dex_entry.grid_forget()
        print("Character Dexterity Input Hidden")  # Debugging statement

def calculate_base_damage(weapon_dmg, skill_modifier):
    """Calculates the base damage based on weapon damage and skill modifier.

    Args:
        weapon_dmg: The damage of the weapon.
        skill_modifier: The skill modifier as a percentage.

    Returns:
        The base damage.
    """
    base_dmg = weapon_dmg * skill_modifier / 100
    return round(base_dmg, 2)

def calculate_total_damage(dex, base):
    """Calculates the total damage based on dexterity multiplier and base damage.

    Args:
        dex: The dexterity of the character.
        base: The base damage of the weapon.

    Returns:
        The total damage.
    """
    total_dmg = ((dex * 0.001) * base) + base
    return total_dmg

def calculate_damage(event=None):
    global weapon_dps, skill_modifier, dex

    # Get the user input.
    weapon_dps = int(weapon_dps_entry.get())
    skill_modifier = int(skill_modifier_entry.get())

    # Check the selected character class
    selected_class = character_class_var.get()
    if selected_class == "Rogue":
        dex = int(dex_entry.get())
    else:
        dex = 0

    # Calculate the base damage and total damage.
    base_dmg = calculate_base_damage(weapon_dps, skill_modifier)
    total_dmg = calculate_total_damage(dex, base_dmg)

    # Create a message box to display the output.
    if selected_class == "Rogue":
        messagebox.showinfo(
            "Output",
            "User input:\nCharacter Class - {}\nWeapon DPS - {}\nSkill modifier percentage - {}\nCharacter dexterity - {}\n\n*********************\n\nBase damage = {}\nTotal damage = {}".format(
                selected_class, weapon_dps, skill_modifier, dex, base_dmg, total_dmg
            ),
        )
    else:
        messagebox.showinfo(
            "Output",
            "User input:\nCharacter Class - {}\nWeapon DPS - {}\nSkill modifier percentage - {}\n\n*********************\n\nBase damage = {}\nTotal damage = {}".format(
                selected_class, weapon_dps, skill_modifier, base_dmg, total_dmg
            ),
        )

if __name__ == "__main__":
    main()
