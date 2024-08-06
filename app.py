from flask import Flask, render_template, request
from roman_converter import RomanConverter

app = Flask(__name__)
converter = RomanConverter()

@app.route('/', methods=['GET', 'POST'])
def index():
  result = None
  if request.method == 'POST':
    conversion_type = request.form.get('conversion_type')
    input_value = request.form.get('input_value')

    if conversion_type == 'int_to_roman':
      try:
        number = int(input_value)
        if number <= 0:
          result = 'Número deve ser maior que 0'
        else:
          roman_numeral = converter.int_to_roman(number)
          result = f'O número romano é: {roman_numeral}'
      except ValueError:
        result = 'Número inválido'
    elif conversion_type == 'roman_to_int':
      try:
        roman_numeral = input_value.upper()
        number = converter.roman_to_int(roman_numeral)
        result = f'O número inteiro é: {number}'
      except KeyError:
        result = 'Número romano inválido'

  return render_template('index.html', result=result)

if __name__ == '__main__':
  app.run(debug=True)
