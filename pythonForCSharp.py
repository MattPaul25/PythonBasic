#running basic basic python program

import random

#public IEnumerable<string> GetDays(){}
def get_days():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days

def get_random_weather_report():
    weather = ['sunny', 'rainy', 'hot', 'lovely']
    day = weather[random.randint(0, len(weather) - 1)]
    return day

def main():
    days = get_days()
    for d in days:
        r = get_random_weather_report()
        print("Weather on {0} is {1}. ".format(d, r))

if __name__ == "__main__":
    main()
