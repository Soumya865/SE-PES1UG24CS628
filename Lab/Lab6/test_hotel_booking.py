import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade

#Example test cases:
def test_standard_two_nights():
    assert booking_cost("standard", 2, 2, False) == 4000

def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000

#Write the rest of the test cases so that the code is 90- 100% covered.
