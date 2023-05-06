# pyowm weather api
import pyowm
key = pyowm.OWM("050d40d23e3ebd8d89fd1d98443ec984") # Open weather key
check = key.weather_manager().weather_at_place(input("place you want to get the weather from: ")) # place and weather manager

# checking all the data 
check_weather = check.weather
status = check_weather.detailed_status
temp = check_weather.temperature("fahrenheit")
wind = check_weather.wind()
sunrise = check_weather.sunrise_time(timeformat='date')
sunset = check_weather.sunset_time(timeformat='date')

# prints the final result
print(
"\nthe current status is: " + str(status) +
"\nthe current max temperature is " + str(temp['temp_max']) + " and the lowest temperature is " + str(temp['temp_min']) + "(temperature unit is fahrenheit)"
"\nthe current wind speed is " + str(wind['speed']) +
"\nthe current sunrise time is " + str(sunrise) + " and the current sunset time is " + str(sunset)
)

# so the program doesnt end imediately xD
input()
