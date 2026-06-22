from circuit import calc_voltage

def test_positive_values():
    assert calc_voltage(2,5) == 10

def test_negative_values():
    assert calc_voltage(-3,4) == -12

def test_zero_values():
    assert calc_voltage(0,100) == 0