
roman_numerals = {
        0 : '',
        1 : 'I',
        2 : 'II',
        3 : 'III',
        4 : 'IV',
        5 : 'V',
        6 : 'VI',
        7 : 'VII',
        8 : 'VIII',
        9 : 'IX',
        10 : 'X',
        50 : 'L',
        100 : 'C',
        500 : 'D',
        1000 : 'M'
    }


def get_number_place_value(num):
    return list(str(num))
   
   
       
     





def get_roman_numeral(num):
   if num <= 10:
        return roman_numerals[num]
   else:
        return get_number_place_value(num)



def test_num_equals_roman_numerals_i():
    for i in range(1,11):
        assert get_roman_numeral(i) == roman_numerals[i]


def test_double_digit_equals_30():
    assert get_number_place_value(30) == ['3','0']

def test_triple_digit_equals_400():
     assert get_number_place_value(400) == ['4','0','0']

    



