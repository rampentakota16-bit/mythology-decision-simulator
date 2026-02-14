# ===============================
# Character Definitions
# ===============================

# Positivity groups are conceptual.
# Final assignment is done via positivity ranges.

POSITIVE_CHARACTERS = [
    "Krishna",
    "Vidura",
    "Yudhishthira",
    "Bhima",
    "Sahadeva",
    "Draupadi",
    "Arjuna",
    "Nakula",
    "Pandu",
    "Abhimanyu",
    "Ekalavya"
]

GREY_CHARACTERS = [
    "Bhishma",
    "Drona",
    "Kunti",
    "Balarama",
    "Gandhari",
    "Dhritarashtra"
]

NEGATIVE_CHARACTERS = [
    "Karna",
    "Shalya",
    "Amba",
    "Dushasana",
    "Shakuni",
    "Jayadratha",
    "Duryodhana",
    "Ashwatthama"
]

# Master ordered list (do not change order)
ALL_CHARACTERS = (
    POSITIVE_CHARACTERS +
    GREY_CHARACTERS +
    NEGATIVE_CHARACTERS
)

# Sanity check
assert len(ALL_CHARACTERS) == 25, "Total characters must be exactly 25"
