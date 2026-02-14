# ===============================
# Scoring Logic
# ===============================

def calculate_average_positivity(responses):
    """
    responses: list of positivity values (length = number of questions)
    returns: average positivity (float)
    """
    if not responses:
        raise ValueError("No responses provided")

    total = sum(responses)
    average = total / len(responses)
    return round(average, 2)
