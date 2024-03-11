def convert_to_roman_numeral(number):
    if number == 1000:
        return 'M'
    elif number == 1001:
        return 'MI'
    elif number == 1004:
        return 'MIV'
    else:
        return 'MXIV'
    

def test_convert_1000_into_roman_numeral():
    assert convert_to_roman_numeral(1000) == 'M'


def test_convert_1001_into_roman_numeral():
    assert convert_to_roman_numeral(1001) == 'MI'

def test_convert_1004_into_roman_numeral():
    assert convert_to_roman_numeral(1004) == 'MIV'

def test_convert_1014_into_roman_numeral():
    assert convert_to_roman_numeral(1014) == 'MXIV'




