# ===============================
# Character Mapping Engine
# ===============================

from mythology_simulator.data.characters import ALL_CHARACTERS

# Positivity ranges mapped in fixed order (highest to lowest)
# These ranges are achievable given option values: 100, 80, 50, 30, 5

CHARACTER_RANGES = [
    ("Krishna", 92, 100),
    ("Vidura", 88, 91.99),
    ("Yudhishthira", 84, 87.99),
    ("Bhima", 80, 83.99),
    ("Sahadeva", 76, 79.99),
    ("Draupadi", 72, 75.99),
    ("Arjuna", 68, 71.99),
    ("Nakula", 64, 67.99),
    ("Pandu", 60, 63.99),
    ("Abhimanyu", 56, 59.99),
    ("Ekalavya", 52, 55.99),
    ("Bhishma", 48, 51.99),
    ("Drona", 44, 47.99),
    ("Kunti", 40, 43.99),
    ("Balarama", 36, 39.99),
    ("Gandhari", 32, 35.99),
    ("Dhritarashtra", 28, 31.99),
    ("Karna", 24, 27.99),
    ("Shalya", 20, 23.99),
    ("Amba", 16, 19.99),
    ("Dushasana", 12, 15.99),
    ("Shakuni", 9, 11.99),
    ("Jayadratha", 6, 8.99),
    ("Duryodhana", 5, 5.99),
]

def map_average_to_character(avg_positivity):
    """
    avg_positivity: float
    returns: character name (str)
    """
    for character, low, high in CHARACTER_RANGES:
        if low <= avg_positivity <= high:
            return character

    # Extreme pathological case (very rare)
    return "Ashwatthama"
