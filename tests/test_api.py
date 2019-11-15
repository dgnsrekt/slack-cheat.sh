from slack_cheat.api import remove_puctuation


def test_remove_puctuation():
    """Testing remove_puctuation method"""
    t_before = "What is a String?!@#$%^&*()_.~`{}[]:;<.>.?/|"
    t_after = remove_puctuation(t_before)
    t_expected = "What is a String"
    assert t_after == t_expected
