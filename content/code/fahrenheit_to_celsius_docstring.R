#' Convert Fahrenheit to Celsius
#'
#' @param temp_f A numeric vector of temperatures in Fahrenheit.
#' @return A numeric vector of temperatures in Celsius.
fahrenheit_to_celsius <- function(temp_f)
{
  temp_c <- (temp_f - 32.0) * (5.0/9.0)
  temp_c
}
