import tkinter as tk
from tkinter import messagebox
import math

# Declare variables.
weapon_dps = 0
skill_modifier = 0
dex = 0
str_stat = 0
willpower = 0
intelligence = 0
weapon_dps_entry = None
skill_modifier_entry = None
dex_entry = None
str_entry = None
willpower_entry = None
intelligence_entry = None
character_class_var = None
dex_label = None
str_label = None
willpower_label = None
intelligence_label = None


def main():
    global weapon_dps_entry, skill_modifier_entry, dex_entry, str_entry, willpower_entry, intelligence_entry
    global character_class_var, dex_label, str_label, willpower_label, intelligence_label

    # Create the main window.
    root = tk.Tk()

    # Set the window title
    root.title("Diablo IV Total Damage Calculator")

    # Set the window size
    root.geometry("390x250")

    # Create the labels for the user input.
    character_class_label = tk.Label(root, text="Character Class")
    weapon_dps_label = tk.Label(root, text="Weapon DPS")
    skill_modifier_label = tk.Label(root, text="Skill modifier percentage")
    dex_label = tk.Label(root, text="Character dexterity")
    str_label = tk.Label(root, text="Character strength")
    willpower_label = tk.Label(root, text="Character willpower")
    intelligence_label = tk.Label(root, text="Character intelligence")
    dex_label.grid_forget()  # Hide the "Character Dexterity" label initially
    str_label.grid_forget()  # Hide the "Character Strength" label initially
    willpower_label.grid_forget()  # Hide the "Character Willpower" label initially
    intelligence_label.grid_forget()  # Hide the "Character Intelligence" label initially

    # Create the dropdown menu for character class selection.
    character_class_var = tk.StringVar(root)
    character_class_var.set("")  # Set default value as blank
    character_class_menu = tk.OptionMenu(root, character_class_var, "", "Barbarian", "Druid", "Necromancer", "Rogue", "Sorcerer")
    character_class_var.trace("w", on_character_class_change)

    # Create the entry boxes for the user input.
    weapon_dps_entry = tk.Entry(root)
    skill_modifier_entry = tk.Entry(root)
    dex_entry = tk.Entry(root)
    str_entry = tk.Entry(root)
    willpower_entry = tk.Entry(root)
    intelligence_entry = tk.Entry(root)
    dex_entry.grid_forget()  # Hide the "Character Dexterity" entry initially
    str_entry.grid_forget()  # Hide the "Character Strength" entry initially
    willpower_entry.grid_forget()  # Hide the "Character Willpower" entry initially
    intelligence_entry.grid_forget()  # Hide the "Character Intelligence" entry initially

    # Create the button that will calculate the damage.
    calculate_damage_button = tk.Button(root, text="Calculate damage", command=calculate_damage)

    # Add the labels, entry boxes, and dropdown menu to the main window.
    character_class_label.grid(row=0, column=0)
    character_class_menu.grid(row=0, column=1)
    weapon_dps_label.grid(row=1, column=0)
    weapon_dps_entry.grid(row=1, column=1)
    skill_modifier_label.grid(row=2, column=0)
    skill_modifier_entry.grid(row=2, column=1)
    dex_label.grid(row=3, column=0)
    dex_entry.grid(row=3, column=1)
    str_label.grid(row=4, column=0)
    str_entry.grid(row=4, column=1)
    willpower_label.grid(row=5, column=0)
    willpower_entry.grid(row=5, column=1)
    intelligence_label.grid(row=6, column=0)
    intelligence_entry.grid(row=6, column=1)
    calculate_damage_button.grid(row=7, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

    # Bind the Enter key to the calculate_damage function
    root.bind('<Return>', calculate_damage)

    # Start the main loop.
    root.mainloop()


def on_character_class_change(*args):
    selected_class = character_class_var.get()

    dex_label.grid_forget()
    dex_entry.grid_forget()
    str_label.grid_forget()
    str_entry.grid_forget()
    willpower_label.grid_forget()
    willpower_entry.grid_forget()
    intelligence_label.grid_forget()
    intelligence_entry.grid_forget()

    if selected_class == "Rogue":
        dex_label.grid(row=3, column=0)
        dex_entry.grid(row=3, column=1)
    elif selected_class == "Barbarian":
        str_label.grid(row=3, column=0)
        str_entry.grid(row=3, column=1)
    elif selected_class == "Druid":
        willpower_label.grid(row=3, column=0)
        willpower_entry.grid(row=3, column=1)
    elif selected_class == "Necromancer":
        willpower_label.grid(row=3, column=0)
        willpower_entry.grid(row=3, column=1)
    elif selected_class == "Sorcerer":
        intelligence_label.grid(row=3, column=0)
        intelligence_entry.grid(row=3, column=1)


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


def calculate_total_damage(attribute_value, base_damage):
    """Calculates the total damage based on attribute value and base damage.

    Args:
        attribute_value: The value of the corresponding character attribute.
        base_damage: The base damage of the weapon.

    Returns:
        The total damage.
    """
    total_dmg = ((attribute_value * 0.001) * base_damage) + base_damage
    return total_dmg


def calculate_damage(event=None):
    global weapon_dps, skill_modifier, dex, str_stat, willpower, intelligence

    # Get the user input.
    weapon_dps = int(weapon_dps_entry.get())
    skill_modifier = int(skill_modifier_entry.get())

    # Check the selected character class and get the corresponding attribute value.
    selected_class = character_class_var.get()
    if selected_class == "Rogue":
        dex = int(dex_entry.get())
    elif selected_class == "Barbarian":
        str_stat = int(str_entry.get())
    elif selected_class == "Druid":
        willpower = int(willpower_entry.get())
    elif selected_class == "Necromancer":
        willpower = int(willpower_entry.get())
    elif selected_class == "Sorcerer":
        intelligence = int(intelligence_entry.get())

    # Calculate the base damage.
    base_damage = calculate_base_damage(weapon_dps, skill_modifier)

    # Calculate the total damage based on the attribute value and base damage.
    if selected_class == "Rogue":
        total_damage = calculate_total_damage(dex, base_damage)
    elif selected_class == "Barbarian":
        total_damage = calculate_total_damage(str_stat, base_damage)
    elif selected_class == "Druid":
        total_damage = calculate_total_damage(willpower, base_damage)
    elif selected_class == "Necromancer":
        total_damage = calculate_total_damage(willpower, base_damage)
    elif selected_class == "Sorcerer":
        total_damage = calculate_total_damage(intelligence, base_damage)

    # Show the total damage in a message box.
    messagebox.showinfo("Total Damage", f"The total damage is: {total_damage}")


# Run the main function.
if __name__ == "__main__":
    main()
