def estimate_flight_time(
    battery_percent: int,
    battery_capacity_ah: float,
    motors: int,
    motor_current_a: float
):
    """
    Estimate drone flight time using engineering formula.
    """

    EFFICIENCY = 0.8

    # Total flight time at 100%
    total_flight_time = (
        battery_capacity_ah
        / (motors * motor_current_a)
        * 60
        * EFFICIENCY
    )

    remaining_time = total_flight_time * (battery_percent / 100)

    return (
        f"With a battery level of {battery_percent}%, battery capacity of "
        f"{battery_capacity_ah}Ah, and {motors} motors drawing approximately "
        f"{motor_current_a}A each, the drone is expected to fly for "
        f"approximately {remaining_time:.1f} minutes. Actual flight time may "
        f"vary based on payload, wind conditions, and maneuvering."
    )
