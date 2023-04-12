from tools import Taiwan_AQI

def get_best(dataList) -> list:
    sorted_data_best = sorted(dataList, key = lambda a:a.aqi)      
    return sorted_data_best[:3]
        

def get_bad(dataList) -> list:
    sorted_data_bad = sorted(dataList, key = lambda a:a.aqi, reverse = True)
    return sorted_data_bad[:3]

def print_site_level(dataList) -> None:
    pass


def main():
    try:
        aqi_list = Taiwan_AQI.download_AQI()
    except Exception as err:
        print(err.args)
        return
    
    
    print("aqi目前站點最好的3個")
    for i in get_best(aqi_list):
        print(i)
    print("aqi目前站點最差的3個")
    for i in get_bad(aqi_list):
        print(i)
    


if(__name__ == "__main__"):
    main()