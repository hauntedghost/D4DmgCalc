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

def main():
    global weapon_dps_entry, skill_modifier_entry, dex_entry

    # Create the main window.
    root = tk.Tk()

    # Set the window title
    root.title("Diablo IV Total Damage Calculator")

    # Set the window size
    root.geometry("390x164")

    # Create the labels for the user input.
    weapon_dps_label = tk.Label(root, text="Weapon DPS")
    skill_modifier_label = tk.Label(root, text="Skill modifier percentage")
    dex_label = tk.Label(root, text="Character dexterity")

    # Create the entry boxes for the user input.
    weapon_dps_entry = tk.Entry(root)
    skill_modifier_entry = tk.Entry(root)
    dex_entry = tk.Entry(root)

    # Create the button that will calculate the damage.
    calculate_damage_button = tk.Button(root, text="Calculate damage", command=calculate_damage)

    # Add the labels and entry boxes to the main window.
    weapon_dps_label.grid(row=0, column=0)
    weapon_dps_entry.grid(row=0, column=1)
    skill_modifier_label.grid(row=1, column=0)
    skill_modifier_entry.grid(row=1, column=1)
    dex_label.grid(row=2, column=0)
    dex_entry.grid(row=2, column=1)
    calculate_damage_button.grid(row=3, column=0)

    # Bind the Enter key to the calculate_damage function
    root.bind('<Return>', calculate_damage)

    # Start the main loop.
    root.mainloop()

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

def calculate_damage(event=None):  # Add event=None parameter to handle the event binding
    global weapon_dps, skill_modifier, dex
    # Get the user input.
    weapon_dps = int(weapon_dps_entry.get())
    skill_modifier = int(skill_modifier_entry.get())
    dex = int(dex_entry.get())

    # Calculate the base damage and total damage.
    base_dmg = calculate_base_damage(weapon_dps, skill_modifier)
    total_dmg = calculate_total_damage(dex, base_dmg)

    # Create a message box to display the output.
    tk.messagebox.showinfo("Output", "User input:\nWeapon DPS - {}\nSkill modifier percentage - {}\nCharacter dexterity - {}\n\n*********************\n\nBase damage = {}\nTotal damage = {}".format(weapon_dps, skill_modifier, dex, base_dmg, total_dmg))

if __name__ == "__main__":
    main()
