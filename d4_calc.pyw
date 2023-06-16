import tkinter as tk
from tkinter import messagebox
import locale

# Set the locale for number formatting
locale.setlocale(locale.LC_ALL, '')

# Declare variables.
weapon_dps = 0
skill_modifier = 0
dex_stat = 0
str_stat = 0
wp_stat = 0
int_stat = 0
weapon_dps_entry = None
skill_modifier_entry = None
dex_stat_entry = None
str_stat_entry = None
wp_stat_entry = None
int_stat_entry = None
character_class_var = None
dex_label = None
str_label = None
wp_label = None
int_label = None
dmgMulti_bonus_entry = None


def main():
    global weapon_dps_entry, skill_modifier_entry, dex_stat_entry, str_stat_entry, wp_stat_entry, int_stat_entry
    global character_class_var, dex_label, str_label, wp_label, int_label, dmgMulti_bonus_entry

    # Create the main window.
    root = tk.Tk()

    # Set the window title
    root.title("Diablo IV Total Damage Calculator")

    # Set the window size
    root.geometry("390x280")

    # Create the labels for the user input.
    character_class_label = tk.Label(root, text="Character Class")
    weapon_dps_label = tk.Label(root, text="Weapon DPS")
    skill_modifier_label = tk.Label(root, text="Skill modifier percentage")
    dex_label = tk.Label(root, text="Character dexterity")
    str_label = tk.Label(root, text="Character strength")
    wp_label = tk.Label(root, text="Character willpower")
    int_label = tk.Label(root, text="Character intelligence")
    dmgMulti_bonus_label = tk.Label(root, text="Add x% skill bonus")
    dex_label.grid_forget()  # Hide the "Character Dexterity" label initially
    str_label.grid_forget()  # Hide the "Character Strength" label initially
    wp_label.grid_forget()  # Hide the "Character Willpower" label initially
    int_label.grid_forget()  # Hide the "Character Intelligence" label initially

    # Create the dropdown menu for character class selection.
    character_class_var = tk.StringVar(root)
    character_class_var.set("")  # Set default value as blank
    character_class_menu = tk.OptionMenu(root, character_class_var, "", "Barbarian", "Druid", "Necromancer", "Rogue", "Sorcerer")
    character_class_var.trace("w", on_character_class_change)

    # Create the entry boxes for the user input.
    weapon_dps_entry = tk.Entry(root)
    skill_modifier_entry = tk.Entry(root)
    dex_stat_entry = tk.Entry(root)
    str_stat_entry = tk.Entry(root)
    wp_stat_entry = tk.Entry(root)
    int_stat_entry = tk.Entry(root)
    dmgMulti_bonus_entry = tk.Entry(root)
    dex_stat_entry.grid_forget()  # Hide the "Character Dexterity" entry initially
    str_stat_entry.grid_forget()  # Hide the "Character Strength" entry initially
    wp_stat_entry.grid_forget()  # Hide the "Character Willpower" entry initially
    int_stat_entry.grid_forget()  # Hide the "Character Intelligence" entry initially

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
    dex_stat_entry.grid(row=3, column=1)
    str_label.grid(row=4, column=0)
    str_stat_entry.grid(row=4, column=1)
    wp_label.grid(row=5, column=0)
    wp_stat_entry.grid(row=5, column=1)
    int_label.grid(row=6, column=0)
    int_stat_entry.grid(row=6, column=1)
    dmgMulti_bonus_label.grid(row=7, column=0)
    dmgMulti_bonus_entry.grid(row=7, column=1)
    calculate_damage_button.grid(row=8, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

    # Bind the Enter key to the calculate_damage function
    root.bind('<Return>', calculate_damage)

    # Start the main loop.
    root.mainloop()


def on_character_class_change(*args):
    selected_class = character_class_var.get()

    dex_label.grid_forget()
    dex_stat_entry.grid_forget()
    str_label.grid_forget()
    str_stat_entry.grid_forget()
    wp_label.grid_forget()
    wp_stat_entry.grid_forget()
    int_label.grid_forget()
    int_stat_entry.grid_forget()

    if selected_class == "Rogue":
        dex_label.grid(row=3, column=0)
        dex_stat_entry.grid(row=3, column=1)
    elif selected_class == "Barbarian":
        str_label.grid(row=3, column=0)
        str_stat_entry.grid(row=3, column=1)
    elif selected_class == "Druid":
        wp_label.grid(row=3, column=0)
        wp_stat_entry.grid(row=3, column=1)
    elif selected_class == "Necromancer":
        wp_label.grid(row=3, column=0)
        wp_stat_entry.grid(row=3, column=1)
    elif selected_class == "Sorcerer":
        int_label.grid(row=3, column=0)
        int_stat_entry.grid(row=3, column=1)


def calculate_base_damage(weapon_dmg, skill_modifier):
    """Calculates the base damage based on weapon damage and skill modifier.

    Args:
        weapon_dmg: The damage of the weapon.
        skill_modifier: The skill modifier as a percentage.

    Returns:
        The base damage.
    """
    base_dmg = weapon_dmg * skill_modifier / 100
    return base_dmg

def calculate_mainStat_bonus(attribute_value):
    """
    Calculates the main stat bonus based on the given attribute value.

    Args:
        attribute_value: The value of the attribute.

    Returns:
        The main stat bonus.
    """
    main_stat_bonus = 1 + (attribute_value * 0.001)
    return main_stat_bonus

def calculate_multi_bonus(dmgMulti_bonus):
    """
    Calculates the multiplicative bonus.

    Args:
        dmgMulti_bonus: The value of the multiplicative bonus.

    Returns:
        The multiplicative bonus.
    """
    multi_bonus = 1+(dmgMulti_bonus / 100)
    return multi_bonus

def calculate_damage(event=None):
    global weapon_dps, skill_modifier, dex_stat, str_stat, wp_stat, int_stat

    # Get the user input.
    weapon_dps = int(weapon_dps_entry.get())
    skill_modifier = int(skill_modifier_entry.get())
    dmgMulti_bonus = 0
    dmgMulti_bonus_value = dmgMulti_bonus_entry.get()
    if dmgMulti_bonus_value:
        try:
            dmgMulti_bonus = int(dmgMulti_bonus_value)
        except ValueError:
            messagebox.showerror("Error", "Please enter an integer value for 'Add x% skill bonus'.")
            return

    # Check the selected character class and get the corresponding attribute value and label.
    selected_class = character_class_var.get()
    attribute_value = None
    attribute_label = None
    if selected_class == "Rogue":
        attribute_value = int(dex_stat_entry.get())
        attribute_label = "Dexterity"
        dexMulti_dmg = calculate_mainStat_bonus(attribute_value) * calculate_base_damage(weapon_dps, skill_modifier)
        skillMulti_bonus = calculate_base_damage(weapon_dps, skill_modifier) * calculate_mainStat_bonus(attribute_value) * calculate_multi_bonus(dmgMulti_bonus)
        messagebox.showinfo("Results", f"User Inputs:\n\nCharacter Class - {selected_class}\nWeapon DPS - {locale.format_string('%d', weapon_dps, grouping=True)}\nSkill Modifier - {locale.format_string('%d', skill_modifier, grouping=True)}\n{attribute_label} - {locale.format_string('%d', attribute_value, grouping=True)}\nAdded x% bonus - {locale.format_string('%d', dmgMulti_bonus, grouping=True)}%\n\n********\n\nDamage Calculations:\n\nBase Skill Damage = {locale.format_string('%0.2f', calculate_base_damage(weapon_dps, skill_modifier), grouping=True)}\nSkill Damage (w/ stat multiplier) = {locale.format_string('%0.2f', dexMulti_dmg, grouping=True)}\nSkill Damage (w/ stat multi and {dmgMulti_bonus}% bonus): {locale.format_string('%0.2f', skillMulti_bonus, grouping=True)}")
    elif selected_class == "Barbarian":
        attribute_value = int(str_stat_entry.get())
        attribute_label = "Strength"
        # Calculate the strMulti_dmg for Barbarian class.
        strMulti_dmg = calculate_mainStat_bonus(attribute_value) * calculate_base_damage(weapon_dps, skill_modifier)
        skillMulti_bonus = calculate_base_damage(weapon_dps, skill_modifier) * calculate_mainStat_bonus(attribute_value) * calculate_multi_bonus(dmgMulti_bonus)
        # Display the total damage and strMulti_dmg to the user, with the associated attribute.
        messagebox.showinfo("Results", f"User Inputs:\n\nCharacter Class - {selected_class}\nWeapon DPS - {locale.format_string('%d', weapon_dps, grouping=True)}\nSkill Modifier - {locale.format_string('%d', skill_modifier, grouping=True)}\n{attribute_label} - {locale.format_string('%d', attribute_value, grouping=True)}\nAdded x% bonus - {locale.format_string('%d', dmgMulti_bonus, grouping=True)}%\n\n********\n\nDamage Calculations:\n\nBase Skill Damage = {locale.format_string('%0.2f', calculate_base_damage(weapon_dps, skill_modifier), grouping=True)}\nSkill Damage (w/ stat multiplier) = {locale.format_string('%0.2f', strMulti_dmg, grouping=True)}\nSkill Damage (w/ stat multi and {dmgMulti_bonus}% bonus): {locale.format_string('%0.2f', skillMulti_bonus, grouping=True)}")

    elif selected_class == "Druid":
        attribute_value = int(wp_stat_entry.get())
        attribute_label = "Willpower"
        # Calculate the wpMulti_dmg for Druid class.
        wpMulti_dmg = calculate_mainStat_bonus(attribute_value) * calculate_base_damage(weapon_dps, skill_modifier)
        skillMulti_bonus = calculate_base_damage(weapon_dps, skill_modifier) * calculate_mainStat_bonus(attribute_value) * calculate_multi_bonus(dmgMulti_bonus)
        # Display the total damage and wpMulti_dmg to the user, with the associated attribute.
        messagebox.showinfo("Results", f"User Inputs:\n\nCharacter Class - {selected_class}\nWeapon DPS - {locale.format_string('%d', weapon_dps, grouping=True)}\nSkill Modifier - {locale.format_string('%d', skill_modifier, grouping=True)}\n{attribute_label} - {locale.format_string('%d', attribute_value, grouping=True)}\nAdded x% bonus - {locale.format_string('%d', dmgMulti_bonus, grouping=True)}%\n\n********\n\nDamage Calculations:\n\nBase Skill Damage = {locale.format_string('%0.2f', calculate_base_damage(weapon_dps, skill_modifier), grouping=True)}\nSkill Damage (w/ stat multiplier) = {locale.format_string('%0.2f', wpMulti_dmg, grouping=True)}\nSkill Damage (w/ stat multi and {dmgMulti_bonus}% bonus): {locale.format_string('%0.2f', skillMulti_bonus, grouping=True)}")
    elif selected_class == "Necromancer":
        attribute_value = int(wp_stat_entry.get())
        attribute_label = "Willpower"
        # Calculate the wpMulti_dmg for Necromancer class.
        wpMulti_dmg = calculate_mainStat_bonus(attribute_value) * calculate_base_damage(weapon_dps, skill_modifier)
        skillMulti_bonus = calculate_base_damage(weapon_dps, skill_modifier) * calculate_mainStat_bonus(attribute_value) * calculate_multi_bonus(dmgMulti_bonus)
        # Display the total damage and wpMulti_dmg to the user, with the associated attribute.
        messagebox.showinfo("Results", f"User Inputs:\n\nCharacter Class - {selected_class}\nWeapon DPS - {locale.format_string('%d', weapon_dps, grouping=True)}\nSkill Modifier - {locale.format_string('%d', skill_modifier, grouping=True)}\n{attribute_label} - {locale.format_string('%d', attribute_value, grouping=True)}\nAdded x% bonus - {locale.format_string('%d', dmgMulti_bonus, grouping=True)}%\n\n********\n\nDamage Calculations:\n\nBase Skill Damage = {locale.format_string('%0.2f', calculate_base_damage(weapon_dps, skill_modifier), grouping=True)}\nSkill Damage (w/ stat multiplier) = {locale.format_string('%0.2f', wpMulti_dmg, grouping=True)}\nSkill Damage (w/ stat multi and {dmgMulti_bonus}% bonus): {locale.format_string('%0.2f', skillMulti_bonus, grouping=True)}")
    elif selected_class == "Sorcerer":
        attribute_value = int(int_stat_entry.get())
        attribute_label = "Intelligence"
        # Calculate the intMulti_dmg for Sorcerer class.
        intMulti_dmg = calculate_mainStat_bonus(attribute_value) * calculate_base_damage(weapon_dps, skill_modifier)
        skillMulti_bonus = calculate_base_damage(weapon_dps, skill_modifier) * calculate_mainStat_bonus(attribute_value) * calculate_multi_bonus(dmgMulti_bonus)
        # Display the total damage and intMulti_dmg to the user, with the associated attribute.
        messagebox.showinfo("Results", f"User Inputs:\n\nCharacter Class - {selected_class}\nWeapon DPS - {locale.format_string('%d', weapon_dps, grouping=True)}\nSkill Modifier - {locale.format_string('%d', skill_modifier, grouping=True)}\n{attribute_label} - {locale.format_string('%d', attribute_value, grouping=True)}\nAdded x% bonus - {locale.format_string('%d', dmgMulti_bonus, grouping=True)}%\n\n********\n\nDamage Calculations:\n\nBase Skill Damage = {locale.format_string('%0.2f', calculate_base_damage(weapon_dps, skill_modifier), grouping=True)}\nSkill Damage (w/ stat multiplier) = {locale.format_string('%0.2f', intMulti_dmg, grouping=True)}\nSkill Damage (w/ stat multi and {dmgMulti_bonus}% bonus): {locale.format_string('%0.2f', skillMulti_bonus, grouping=True)}")
    else:
        messagebox.showerror("Error", "Please select a character class.")

main()
