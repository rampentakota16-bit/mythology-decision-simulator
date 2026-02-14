# ===============================
# Analytical Report Generator
# ===============================

def generate_analytical_report(character, average_positivity):
    """
    character: str (assigned Mahabharata character)
    average_positivity: float
    returns: str (100-word analytical report)
    """

    report = (
        f"Core Character Alignment:\n"
        f"You most closely resemble {character}, based on an overall positivity score "
        f"of {average_positivity}%. This reflects a consistent pattern in how you "
        f"approach responsibility and consequence.\n\n"

        f"Decision Pattern Analysis:\n"
        f"Your choices show a measured balance between ethical intent and practical "
        f"action. You tend to consider long-term outcomes rather than reacting only "
        f"to immediate pressure.\n\n"

        f"Emotional and Social Orientation:\n"
        f"You display controlled emotional responses, preferring restraint over "
        f"impulsive expression. In social contexts, you value stability, fairness, "
        f"and thoughtful judgment.\n\n"

        f"Leadership and Life Perspective:\n"
        f"This profile suggests strength in reflective leadership. You function best "
        f"when allowed time to evaluate situations carefully and act with clarity "
        f"rather than haste."
    )

    return report
