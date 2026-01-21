def run_bridge_detection(img):
    # preprocess as your ML model expects
    # For example:
    # results = model.predict(img)

    # Example outputs (replace with real logic):
    bridge_found = True
    damage_pct = 3.77
    life = "10–15 years"

    if not bridge_found:
        return "No bridge detected", 0, "N/A"

    return "Bridge detected", damage_pct, life
