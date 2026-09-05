# Drone Flight Calculator

This project calculates the usable active flight time of a
quadcopter based on its payload weight. 

The flight time is calculated using:

T(w) = 180 - 0.1w

where w is the payload weight in grams and T is the flight time in minutes.

Flight time cannot fall below zero. Negative payload weights raise a ValueError.

## Testing

The project uses pytest to test the flight-time calculation, including zero
payload, typical payloads, heavy payloads, and invalid negative payloads.

## AI-Use Disclosure

Used GitHub Copilot inline suggestions while implementing the flight calculator
and GitHub Copilot chat to generate the initial unit tests 
for calculate_flight_time(). I reviewed and edited the generated tests to ensure
they covered all four which were zero payload, a typical payload, the zero-flight-time boundary,
and negative weight input. I verified the implementation by running
the complete test with pytest and made sure that all 4 tests passed.