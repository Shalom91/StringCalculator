import calculator
import pytest

# Testing for each condition in add
def test_add():
    #testing condition 1
    assert calculator.add("") == 0
    assert calculator.add("1") == 1
    assert calculator.add("1,1") == 2

    #testing condition 2
    assert calculator.add("1,2,3,4") == 10
    assert calculator.add("") == 0
    assert calculator.add("1") == 1
    assert calculator.add("1,1") == 2

    # testing condition 3
    assert calculator.add("1\n2,3") == 6

    # testing condition 4
    assert calculator.add("//;\n1;2") == 3
    assert calculator.add("//4\n142") == 3

    # testing condition 5
    with pytest.raises(Exception):
        assert add("-1,-2,3,4") == Exception("ERROR: negatives not allowed -1,-2")
    
    # testing condition 6
    assert calculator.add("//;\n1000,1;2") == 3

    # testing condition 7
    assert calculator.add("//***\n1***2***3") == 6

    # testing condition 8
    assert calculator.add("//[:D][%]\n1:D2%3") == 6
    assert calculator.add("//[***][%%%]\n1***2%%%3") == 6
    assert calculator.add("//[(-_-')][%]\n1(-_-')2%3") == 6
    assert calculator.add("//[abc][777][:(]\n1abc27773:(1") == 7

    # testing condition 9
    """
    MESSAGE POSTED ON SLACK
    Siphiwe  10:31 AM
    @here had a chat with @Johan about the 9th condition for string calculator, 
    it seems to have contradictory instructions so your function does not have 
    to account for it.
    """
    
    


    





