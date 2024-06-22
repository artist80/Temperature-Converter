from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    temperature = float(request.form['temperature'])
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    converted_temp = convert_temperature(temperature, from_unit, to_unit)
    return render_template('index.html', temperature=temperature, from_unit=from_unit, to_unit=to_unit, converted_temp=converted_temp)

def convert_temperature(temp, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return temp * 9/5 + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (temp - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return temp + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return temp - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (temp - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (temp - 273.15) * 9/5 + 32
    else:
        return temp  # If from_unit == to_unit, return the same temperature

if __name__ == '__main__':
    app.run(debug=True)
