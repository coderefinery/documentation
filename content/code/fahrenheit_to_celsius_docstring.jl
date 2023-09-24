"""
    fahrenheit_to_celsius(temp_f::Float)

Converts temperature in Fahrenheit to Celsius.

# Arguments
- `temp_f::Float`: Temperature in Fahrenheit.

# Returns
- `temp_c::Float`: Temperature in Celsius.
"""
function fahrenheit_to_celsius(temp_f)
    temp_c = (temp_f - 32.0) * (5.0/9.0)
    return temp_c
end
