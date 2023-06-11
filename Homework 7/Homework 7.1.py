def convert_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    time_dict = {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }
    return time_dict


# Вхідні параметри
if __name__ == '__main__':
    input_seconds = int(input("Введіть кількість секунд: "))
    time = convert_time(input_seconds)
    print(time)
