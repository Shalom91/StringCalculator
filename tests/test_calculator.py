from string_calculator.calculator import add
import pytest

def test_add():
    #testing condition 1
    assert calculator.add("") == 0
    assert calculator.add("1") == 1
    assert calculator.add("1,1") == 2

    assert calculator.add("1,2,3,4") == 6 
    assert calculator.add("") == 0
    assert calculator.add("1") == 1
    assert calculator.add("1,1") == 2

    assert calculator.add("1\n2,3") == 6

    assert calculator.add("//;\n1;2") == 3
    assert calculator.add("//4\n142") == 3

    with pytest.raises(Exception):
        assert add("-1,-2,3,4") == Exception("ERROR: negatives not allowed -1,-2")
    
    assert calculator.add("//;\n1000,1;2") == 3

    assert calculator.add("//***\n1***2***3") == 6

    assert calculator.add("//[:D][%]\n1:D2%3") == 6
    assert calculator.add("//[***][%%%]\n1***2%%%3") == 6
    assert calculator.add("//[(-_-')][%]\n1(-_-')2%3") == 6
    assert calculator.add("//[abc][777][:(]\n1abc27773:(1") == 7


    
    


    





