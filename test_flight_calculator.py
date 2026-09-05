import pytest

from flight_calculator import calculate_flight_time


def test_zero_payload():
    assert calculate_flight_time(0) == 180


def test_typical_payload():
    assert calculate_flight_time(500) == 130


def test_heavy_payload():
    assert calculate_flight_time(2000) == 0


def test_negative_payload():
    with pytest.raises(ValueError):
        calculate_flight_time(-100)