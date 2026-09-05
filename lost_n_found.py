def calculate_flight_time(weight_grams):
    """
    Calculate active drone flight time for a given payload weight.

    Parameters:
        weight_grams: Payload weight in grams.

    Returns:
        Flight time in minutes.
    """
    if weight_grams < 0:
        raise ValueError("Payload weight cannot be negative.")

    flight_time = 180 - (0.1 * weight_grams)

    if flight_time < 0:
        return 0

    return flight_time


def flight_time_table(max_weight_grams, step_grams):
    """
    Create a table of payload weights and their corresponding flight times.

    Parameters:
        max_weight_grams: Maximum payload weight in grams.
        step_grams: Amount to increase the payload weight each step.

    Returns:
        A list of (weight, flight_time) pairs.
    """
    table = []

    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))

    return table
print(calculate_flight_time(500))
print(flight_time_table(500, 100))