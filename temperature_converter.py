import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

st.title("Temperature Converter")

temperature = st.number_input("Enter temperature:", value=0.0)

input_unit = st.selectbox("Select input unit:", ("Celsius", "Fahrenheit", "Kelvin"))

if input_unit == "Celsius":
    celsius_temp = temperature
elif input_unit == "Fahrenheit":
    celsius_temp = fahrenheit_to_celsius(temperature)
else:
    celsius_temp = kelvin_to_celsius(temperature)

output_unit = st.selectbox("Select output unit:", ("Celsius", "Fahrenheit", "Kelvin"))

if output_unit == "Celsius":
    result = celsius_temp
elif output_unit == "Fahrenheit":
    result = celsius_to_fahrenheit(celsius_temp)
else:
    result = celsius_to_kelvin(celsius_temp)

st.write(f"The temperature is: {result} {output_unit}")
