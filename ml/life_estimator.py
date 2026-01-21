def estimate_life(damage):
    """
    Estimate remaining safe life of the bridge based on damage percentage
    """
    if damage < 10:
        return "10–15 years"
    elif damage < 25:
        return "5–10 years"
    elif damage < 50:
        return "1–5 years"
    elif damage < 75:
        return "3–12 months"
    else:
        return "Immediate repair required"
