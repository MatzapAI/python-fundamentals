print("---TEMPERATURE RECORD---")

temperature_record = [24, 26, 27, 26, 26, 27, 24]

print(f"Day one: {temperature_record[0]}°C")
print(f"Day three: {temperature_record[2]}°C")
print(f"Day seven: {temperature_record[6]}°C")

average = sum(temperature_record) / len(temperature_record)

print(f"average temperature: {average:.2f}°C")

print(f"Highest temperature of the day: {max(temperature_record)}°C")
print(f"Lowest temperature of the day: {min(temperature_record)}°C")