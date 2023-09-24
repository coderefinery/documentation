!> @brief Convert Fahrenheit to Celsius
!! @param temp_f Temperature in Fahrenheit
!! @return Temperature in Celsius
function fahrenheit_to_celsius(temp_f) result(temp_c)
    implicit none
    real temp_f
    real temp_c
    temp_c = (temp_f - 32.0) * (5.0/9.0)
end function
