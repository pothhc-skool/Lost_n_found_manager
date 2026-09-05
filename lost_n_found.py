def calculate_flight_time(weight_grams):
    """
    Calculates active flight time based on payload weight.

    Parameters:
        weight_grams: Payload weight in grams.

    Returns:
        Active flight time in minutes.
    """

    if weight_grams < 0:
        raise ValueError("Payload weight cannot be negative.")

    # Copilot suggestion accepted: calculate flight time using the given formula.
    flight_time = 180 - (0.1 * weight_grams)

    # Copilot suggestion edited to ensure flight time cannot go below zero.
    if flight_time < 0:
        return 0

    return flight_time


def flight_time_table(max_weight_grams, step_grams):
    """
    Creates a table of payload weights and corresponding flight times.

    Parameters:
        max_weight_grams: Maximum payload weight in grams.
        step_grams: Payload weight increment in grams.

    Returns:
        A list of (weight, flight_time) pairs.
    """

    table = []

    # Copilot suggestion rejected because it tried to recalculate the
    # formula instead of calling calculate_flight_time().
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))

    return table
