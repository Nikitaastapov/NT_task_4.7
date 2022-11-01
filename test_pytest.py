import pytest
from main import check_balance

class TestFuncion:
    test_param =[
        ('(((([{}]))))', 'Balanced'),
        ('[([])((([[[]]])))]{()}', 'Balanced'),
        ('{{[()]}}', 'Balanced'),
        ('}{}', 'Unbalanced'),
        ('{{[(])]}}', 'Unbalanced'),
        ('[[{())}]', 'Unbalanced'),
        ('[]()','Unbalanced')]
    @pytest.mark.parametrize('check_list, result', test_param)      
    def test_check_balance(self, check_list, result):
        res = check_balance(check_list)
        assert result == res
        
    
    
if __name__ == "__main__":
    pytest.main()