
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
    split_into_digits = (str(num)).split('')
    print(split_into_digits)
   
       
     





def get_roman_numeral(num):
   return roman_numerals[num]



def test_num_equals_roman_numerals_i():
    for i in range(1,11):
        assert get_roman_numeral(i) == roman_numerals[i]

def test_single_digit_equals_1():
    assert get_number_place_value(1) == 1


def test_double_digit_equals_2():
    assert get_number_place_value(30) == [3,0]
    



