/// Convert Fahrenheit to Celsius
/// # Arguments
/// * `temp_f` - Temperature in Fahrenheit
///
/// # Returns
/// * `temp_c` - Temperature in Celsius
fn fahrenheit_to_celsius(temp_f: f64) -> f64 {
    let temp_c = (temp_f - 32.0) * 5.0 / 9.0
    temp_c
}
