def create_character(name, strength, intelligence, charisma):
    # Validate name
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # Validate stats are integers
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"

    # Validate minimum value
    if any(stat < 1 for stat in (strength, intelligence, charisma)):
        return "All stats should be no less than 1"

    # Validate maximum value
    if any(stat > 4 for stat in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"

    # Validate total points
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # Build character sheet
    return (
        f"{name}\n"
        f"STR {'●' * strength}{'○' * (10 - strength)}\n"
        f"INT {'●' * intelligence}{'○' * (10 - intelligence)}\n"
        f"CHA {'●' * charisma}{'○' * (10 - charisma)}"
    )