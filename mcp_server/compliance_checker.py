def check_compliance(drone_weight_kg: float, zone: str):
    """
    Check DGCA compliance and return human-readable explanation.
    """

    # ---- Drone classification ----
    if drone_weight_kg <= 0.25:
        classification = "Nano"
    elif drone_weight_kg <= 2:
        classification = "Micro"
    elif drone_weight_kg <= 25:
        classification = "Small"
    else:
        classification = "Medium"

    # ---- Zone permissions ----
    zone = zone.lower()

    if zone == "green":
        permission = "No prior permission is required to operate in the green zone."
    elif zone == "yellow":
        permission = "Permission from the concerned Air Traffic Control (ATC) authority is mandatory."
    elif zone == "red":
        permission = "Permission from the Central Government is required as this is a no-drone zone."
    else:
        return "Invalid zone selected. Please choose green, yellow, or red."

    # ---- License rule ----
    if classification in ["Nano"]:
        license_rule = "A remote pilot license is not required for nano drones."
    elif classification == "Micro":
        license_rule = "A pilot license is not required for non-commercial micro drone operations."
    else:
        license_rule = "A remote pilot license is mandatory for this drone category."

    # ---- Final explanation ----
    return (
        f"This drone falls under the **{classification}** category as per DGCA weight classification. "
        f"It is planned to operate in a **{zone.capitalize()} Zone**. {permission} "
        f"{license_rule}"
    )
