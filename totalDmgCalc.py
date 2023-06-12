# Diablo IV TotalDmg Calculator

# Ask the user for their weapon DPS
weapon_dps = input("What is your weapon DPS? ")

# Ask the user for their skill modifier percentage
skill_modifier = input("What is your skill modifier percentage? ")

# Ask the user for their dexterity stat
dexterity = input("What is your dexterity stat? ")

# Convert the user input to numbers
weapon_dps = int(weapon_dps)
skill_modifier = float(skill_modifier) / 100
dexterity = int(dexterity)

# Calculate the base damage
base_damage = weapon_dps * skill_modifier

# Calculate the dexterity damage modifier
dex_damage_modifier = (dexterity * 0.1)

# Calculate the total damage
total_damage = base_damage + dex_damage_modifier

# Print the results
print("Base Damage:", base_damage)
print("Dex Damage Modifier:", dex_damage_modifier)
print("Total Damage:", total_damage)
