import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade

# ---------- Example test cases (from test_hotel_booking.py) ----------
def test_standard_two_nights():
    assert booking_cost("standard", 2, 2, False) == 4000


def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000

# ---------- booking_cost ----------
def test_unknown_room_raises():
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("penthouse", 2, 2, False)


def test_invalid_nights_raises():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)


def test_suite_peak_extra_guests_long_stay():
    # rate 6000 + 1500 = 7500; 7 nights = 52500; +2 extra guests*500*7 = 7000
    # total 59500; 10% long-stay discount = 5950 -> 53550
    assert booking_cost("suite", 7, 4, True) == 53550


# ---------- cancellation_refund ----------
def test_refund_full_when_week_ahead():
    assert cancellation_refund(1000, 10, False) == 1000


def test_refund_half_plus_member_bonus():
    assert cancellation_refund(1000, 3, True) == 750


def test_refund_zero_when_last_minute():
    assert cancellation_refund(1000, 0, False) == 0


# ---------- room_upgrade ----------
def test_no_upgrade_when_no_rooms_free():
    assert room_upgrade("standard", True, 0) == "standard"


def test_standard_member_upgrades_to_deluxe():
    assert room_upgrade("standard", True, 3) == "deluxe"


def test_deluxe_member_upgrades_to_suite():
    assert room_upgrade("deluxe", True, 3) == "suite"


def test_non_member_gets_no_upgrade():
    assert room_upgrade("standard", False, 3) == "standard"
