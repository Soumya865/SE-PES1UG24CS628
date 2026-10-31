import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade

# ---------- Example test cases (from test_hotel_booking.py) ----------
def test_standard_two_nights():
    assert booking_cost("standard", 2, 2, False) == 4000


def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000

# ================= booking_cost =================
def test_unknown_room_raises():
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("penthouse", 2, 2, False)


def test_zero_nights_raises():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)


def test_negative_nights_raises():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", -3, 2, False)


def test_valid_room_valid_nights_boundary_one_night():
    # nights == 1 is the smallest valid value (nights < 1 is False)
    assert booking_cost("standard", 1, 1, False) == 2000


def test_peak_season_true():
    # deluxe 3500 + 875 = 4375 per night, 2 nights, 2 guests (no extra)
    assert booking_cost("deluxe", 2, 2, True) == 8750


def test_peak_season_false():
    assert booking_cost("deluxe", 2, 2, False) == 7000


def test_guests_exactly_two_no_surcharge():
    assert booking_cost("standard", 3, 2, False) == 6000


def test_guests_three_surcharge():
    # 6000 + (3-2)*500*3 = 7500
    assert booking_cost("standard", 3, 3, False) == 7500


def test_six_nights_no_long_stay_discount():
    # 12000 + 1*500*6 = 15000, nights < 7 so no discount
    assert booking_cost("standard", 6, 3, False) == 15000


def test_seven_nights_long_stay_discount_boundary():
    # 14000 - 1400 = 12600
    assert booking_cost("standard", 7, 2, False) == 12600


def test_all_conditions_combined():
    # 7500*7=52500 + 7000 = 59500 - 5950 = 53550
    assert booking_cost("suite", 7, 4, True) == 53550


# ================= cancellation_refund =================
def test_refund_exactly_seven_days_full_amount():
    assert cancellation_refund(1000, 7, False) == 1000


def test_refund_full_member_gets_no_extra_bonus():
    # early return: member bonus never applied when >= 7 days
    assert cancellation_refund(1000, 7, True) == 1000


def test_refund_six_days_half_non_member():
    assert cancellation_refund(1000, 6, False) == 500


def test_refund_exactly_two_days_half_boundary():
    assert cancellation_refund(1000, 2, False) == 500


def test_refund_half_member_bonus():
    assert cancellation_refund(1000, 3, True) == 750


def test_refund_one_day_zero_non_member():
    assert cancellation_refund(1000, 1, False) == 0


def test_refund_one_day_member_bonus_only():
    assert cancellation_refund(1000, 1, True) == 250


# ================= room_upgrade =================
def test_no_rooms_free_returns_same_room():
    assert room_upgrade("standard", True, 0) == "standard"


def test_standard_member_to_deluxe():
    assert room_upgrade("standard", True, 5) == "deluxe"


def test_standard_non_member_stays_standard():
    assert room_upgrade("standard", False, 5) == "standard"


def test_deluxe_member_to_suite():
    assert room_upgrade("deluxe", True, 5) == "suite"


def test_deluxe_non_member_stays_deluxe():
    assert room_upgrade("deluxe", False, 5) == "deluxe"


def test_suite_member_stays_suite():
    assert room_upgrade("suite", True, 5) == "suite"
