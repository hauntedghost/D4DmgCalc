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
dmgAdd_bonus_entry = None


def main():
    global weapon_dps_entry, skill_modifier_entry, dex_stat_entry, str_stat_entry, wp_stat_entry, int_stat_entry
    global character_class_var, dex_label, str_label, wp_label, int_label, dmgMulti_bonus_entry, dmgAdd_bonus_entry

    # Create the main window.
    root = tk.Tk()

    # Set the window title
    root.title("Diablo IV Total Damage Calculator")

    # Set the window size
    root.geometry("426x414")

    # Create the labels for the user input.
    character_class_label = tk.Label(root, text="Character Class")
    weapon_dps_label = tk.Label(root, text="Weapon DPS")
    skill_modifier_label = tk.Label(root, text="Skill modifier percentage")
    dex_label = tk.Label(root, text="Character dexterity")
    str_label = tk.Label(root, text="Character strength")
    wp_label = tk.Label(root, text="Character willpower")
    int_label = tk.Label(root, text="Character intelligence")
    dmgMulti_bonus_label = tk.Label(root, text="Add x% skill bonus")
    dmgAdd_bonus_label = tk.Label(root, text="Add +% skill bonus")

    # Hide the stat labels initially
    dex_label.grid_forget()  
    str_label.grid_forget()  
    wp_label.grid_forget()  
    int_label.grid_forget()  

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
    dmgAdd_bonus_entry = tk.Entry(root)

    # Hide the entry boxes for stats initially
    dex_stat_entry.grid_forget()  
    str_stat_entry.grid_forget()  
    wp_stat_entry.grid_forget()  
    int_stat_entry.grid_forget()  

    # Create the button that will calculate the damage.
    calculate_damage_button = tk.Button(root, text="Calculate damage", command=calculate_damage)

    # Position the labels on the grid.
    character_class_label.grid(row=0, column=0, padx=5, pady=10, sticky="w")
    weapon_dps_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    skill_modifier_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    dex_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    str_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    wp_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    int_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    dmgMulti_bonus_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
    dmgAdd_bonus_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    # Position the dropdown menu and entry boxes on the grid.
    character_class_menu.grid(row=0, column=1, padx=5, pady=10, sticky="w")
    weapon_dps_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    skill_modifier_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    dex_stat_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    str_stat_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
    wp_stat_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
    int_stat_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
    dmgMulti_bonus_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")
    dmgAdd_bonus_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")
    
    # Position the calculate button on the grid.
    calculate_damage_button.grid(row=9, column=0, columnspan=2, padx=5, pady=10)

    # Bind the Enter key to the calculate_damage function
    root.bind('<Return>', calculate_damage)

    # Start the main loop.
    root.mainloop()


def on_character_class_change(*args):
    global dex_label, str_label, wp_label, int_label, dex_stat_entry, str_stat_entry, wp_stat_entry, int_stat_entry

    # Retrieve the selected character class.
    character_class = character_class_var.get()

    # Show or hide the corresponding labels and entry boxes based on the selected character class.
    if character_class == "Barbarian":
        dex_label.grid_forget()
        str_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        wp_label.grid_forget()
        int_label.grid_forget()
        dex_stat_entry.grid_forget()
        str_stat_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        wp_stat_entry.grid_forget()
        int_stat_entry.grid_forget()
    elif character_class == "Rogue":
        dex_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        str_label.grid_forget()
        wp_label.grid_forget()
        int_label.grid_forget()
        dex_stat_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        str_stat_entry.grid_forget()
        wp_stat_entry.grid_forget()
        int_stat_entry.grid_forget()
    elif character_class == "Druid":
        dex_label.grid_forget()
        str_label.grid_forget()
        wp_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        int_label.grid_forget()
        dex_stat_entry.grid_forget()
        str_stat_entry.grid_forget()
        wp_stat_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        int_stat_entry.grid_forget()
    elif character_class == "Necromancer":
        dex_label.grid_forget()
        str_label.grid_forget()
        wp_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        int_label.grid_forget()
        dex_stat_entry.grid_forget()
        str_stat_entry.grid_forget()
        wp_stat_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        int_stat_entry.grid_forget()
    elif character_class == "Sorcerer":
        dex_label.grid_forget()
        str_label.grid_forget()
        wp_label.grid_forget()
        int_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        dex_stat_entry.grid_forget()
        str_stat_entry.grid_forget()
        wp_stat_entry.grid_forget()
        int_stat_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")


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
    main_stat_bonus = (1 + (attribute_value * 0.001))
    return main_stat_bonus

def calculate_multi_bonus(dmgMulti_bonus):
    """
    Calculates the multiplicative bonus.

    Args:
        dmgMulti_bonus: The value of the multiplicative bonuses.

    Returns:
        The multiplicative bonus.
    """
    multi_bonus = 1+(dmgMulti_bonus / 100)
    return multi_bonus

def calculate_add_bonus(dmgAdd_bonus):
    """
    Calculates the addative bonus.

    Args:
        dmgAdd_bonus: The value of the addative bonuses.

    Returns:
        The addative bonus.
    """
    add_bonus = 1+(dmgAdd_bonus / 100)
    return add_bonus

def calculate_damage(event=None):
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

    dmgAdd_bonus = 0
    dmgAdd_bonus_value = dmgAdd_bonus_entry.get()
    if dmgAdd_bonus_value:
        try:
            dmgAdd_bonus = int(dmgAdd_bonus_value)
        except ValueError:
            messagebox.showerror("Error", "Please enter an integer value for 'Add +% skill bonus'.")
            return

    # Check the selected character class and get the corresponding attribute value and label.
    selected_class = character_class_var.get()
    attribute_value = None
    attribute_label = None

    if selected_class == "Rogue":
        attribute_value = int(dex_stat_entry.get())
        attribute_label = "Dexterity"
    elif selected_class == "Barbarian":
        attribute_value = int(str_stat_entry.get())
        attribute_label = "Strength"
    elif selected_class == "Druid" or selected_class == "Necromancer":
        attribute_value = int(wp_stat_entry.get())
        attribute_label = "Willpower"
    elif selected_class == "Sorcerer":
        attribute_value = int(int_stat_entry.get())
        attribute_label = "Intelligence"
    else:
        messagebox.showerror("Error", "Please select a character class.")
        return

    base_damage = calculate_base_damage(weapon_dps, skill_modifier)
    main_stat_bonus = calculate_mainStat_bonus(attribute_value)
    multi_bonus = calculate_multi_bonus(dmgMulti_bonus)
    add_bonus = calculate_add_bonus(dmgAdd_bonus)

    skillStat_dmg = main_stat_bonus * 100
    skillMultiBonus_dmg = base_damage * multi_bonus -base_damage
    skillAddBonus_dmg = base_damage * add_bonus - base_damage
    totalDmg = base_damage * main_stat_bonus * multi_bonus * add_bonus

    # Show/Hide multi bonuses or add bonuses depending if their values are blank or not
    result_message = ""  # Initialize result_message with an empty string
    skill_multi_bonus_message = ""
    if dmgMulti_bonus > 1:
        skill_multi_bonus_message += f"x{dmgMulti_bonus}% bonus): {locale.format_string('%0.2f', skillMultiBonus_dmg, grouping=True)}\n"
    
    skill_add_bonus_message = ""
    if dmgAdd_bonus > 1:
        skill_add_bonus_message += f"+{dmgAdd_bonus}% bonus): {locale.format_string('%0.2f', skillAddBonus_dmg, grouping=True)}\n"

    totalDmg_resultMessage = f"Total Damage (w/ all bonuses): {locale.format_string('%0.2f', totalDmg, grouping=True)}"

    # Display the results to the user.
    #result_message = f"User Inputs:\n\nCharacter Class - {selected_class}\nWeapon DPS - {locale.format_string('%d', weapon_dps, grouping=True)}\nSkill Modifier - {locale.format_string('%d', skill_modifier, grouping=True)}\n{attribute_label} - {locale.format_string('%d', attribute_value, grouping=True)}\nAdded x% bonus - {locale.format_string('%d', dmgMulti_bonus, grouping=True)}%\nAdded +% bonus - {locale.format_string('%d', dmgAdd_bonus, grouping=True)}%\n\n********\n\nDamage Calculations:\n\nBase Skill Damage = {locale.format_string('%0.2f', base_damage, grouping=True)}\nSkill Damage (w/ stat multiplier) = {locale.format_string('%0.2f', skillMulti_bonus, grouping=True)}\nSkill Damage (w/ stat multi and x{dmgMulti_bonus}% bonus): {locale.format_string('%0.2f', skillMulti_bonus, grouping=True)}\nSkill Damage (w/ stat multi and +{dmgAdd_bonus}% bonus): {locale.format_string('%0.2f', skillAdd_bonus, grouping=True)}\nTotal Damage (w/ all bonuses): {locale.format_string('%0.2f', totalDmg, grouping=True)}"
    result_message = f"User Inputs:\n\nCharacter Class - {selected_class}\nWeapon DPS - {locale.format_string('%d', weapon_dps, grouping=True)}\nSkill Modifier - {locale.format_string('%d', skill_modifier, grouping=True)}\n{attribute_label} - {locale.format_string('%d', attribute_value, grouping=True)}\nAdded x% bonus - {locale.format_string('%d', dmgMulti_bonus, grouping=True)}%\nAdded +% bonus - {locale.format_string('%d', dmgAdd_bonus, grouping=True)}%\n\n********\n\nDamage Calculations:\n\nBase Skill Damage = {locale.format_string('%0.2f', base_damage, grouping=True)}\n{attribute_label} multiplier bonus = +{locale.format_string('%0.2f', skillStat_dmg, grouping=True)}%\n" + skill_multi_bonus_message + skill_add_bonus_message + totalDmg_resultMessage
    messagebox.showinfo("Results", result_message)

main()
