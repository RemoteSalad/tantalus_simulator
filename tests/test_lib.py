from tantalus.lib import try_me, lower_chin, reach_for_fruit, give_up
def test_length_of_tryme():
    assert len(try_me()) != 0

def test_length_of_lowerchin():
    assert len(lower_chin()) != 0

def test_length_of_reachforfruit():
    assert len(reach_for_fruit()) != 0

def test_length_of_giveup():
    assert len(give_up()) != 0
