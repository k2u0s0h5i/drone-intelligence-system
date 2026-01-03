import pandas as pd

ROI_FILE = "data/processed/use_case_roi.csv"

def calculate_roi(farm_size_acres: int):
    """
    Calculate ROI for agriculture drone usage.
    Uses linear interpolation if exact farm size is not available.
    Returns a human-readable explanation.
    """

    df = pd.read_csv(ROI_FILE).sort_values("farm_size_acres")
    sizes = df["farm_size_acres"].values

    # ---------------- BOUNDS CHECK ----------------
    if farm_size_acres < sizes.min() or farm_size_acres > sizes.max():
        return (
            f"ROI data is available only for farm sizes between "
            f"{int(sizes.min())} and {int(sizes.max())} acres."
        )

    # ---------------- EXACT MATCH ----------------
    if farm_size_acres in sizes:
        row = df[df["farm_size_acres"] == farm_size_acres].iloc[0]

        return (
            f"For a farm size of {farm_size_acres} acres, traditional spraying "
            f"would cost approximately ₹{int(row['traditional_cost_inr'])}. "
            f"Using agriculture drones reduces the cost to about "
            f"₹{int(row['drone_cost_inr'])}, resulting in estimated seasonal "
            f"savings of ₹{int(row['seasonal_savings_inr'])}."
        )

    # ---------------- INTERPOLATION ----------------
    lower = df[df["farm_size_acres"] < farm_size_acres].iloc[-1]
    upper = df[df["farm_size_acres"] > farm_size_acres].iloc[0]

    ratio = (
        (farm_size_acres - lower["farm_size_acres"]) /
        (upper["farm_size_acres"] - lower["farm_size_acres"])
    )

    traditional_cost = round(
        lower["traditional_cost_inr"] +
        ratio * (upper["traditional_cost_inr"] - lower["traditional_cost_inr"])
    )

    drone_cost = round(
        lower["drone_cost_inr"] +
        ratio * (upper["drone_cost_inr"] - lower["drone_cost_inr"])
    )

    seasonal_savings = traditional_cost - drone_cost

    return (
        f"For a farm size of {farm_size_acres} acres, traditional spraying would "
        f"cost approximately ₹{traditional_cost}. Using agriculture drones "
        f"reduces the cost to about ₹{drone_cost}, resulting in estimated "
        f"seasonal savings of ₹{seasonal_savings}."
    )
