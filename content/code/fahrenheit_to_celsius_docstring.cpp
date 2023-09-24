// @brief: Converts a temperature in Fahrenheit to Celsius
//
// @param: temp_f: Temperature in Fahrenheit
//
// @return: Temperature in Celsius
double fahrenheit_to_celsius(double temp_f) {
    auto temp_c = (temp_f - 32.0) * (5.0 / 9.0);
    return temp_c;
}
