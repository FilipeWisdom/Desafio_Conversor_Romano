class RomanConverter:
  def __init__(self):
    self.value_map = [
      (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
      (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
      (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    self.roman_to_int_map = {roman: arabic for arabic, roman in self.value_map}

  def int_to_roman(self, num):
    result = ''
    for (arabic, roman) in self.value_map:
      while num >= arabic:
        result += roman
        num -= arabic
    return result

  def roman_to_int(self, roman):
    i = 0
    result = 0
    while i < len(roman):
      if i + 1 < len(roman) and roman[i:i+2] in self.roman_to_int_map:
        result += self.roman_to_int_map[roman[i:i+2]]
        i += 2
      else:
        result += self.roman_to_int_map[roman[i]]
        i += 1
    return result

