from tools import Taiwan_AQI

def get_best(dataList) -> list:
    sorted_data_best = sorted(dataList, key = lambda a:a.aqi)
    #for item in sorted_data_best:
    #    print(item)      
    return sorted_data_best[:3]
        

def get_bad(dataList) -> list:
    sorted_data_bad = sorted(dataList, key = lambda a:a.aqi, reverse = True) #reverse = True 則排列順序由大到小, 如果都不設, 默認為False
    return sorted_data_bad[:3]

def print_site_level(dataList) -> None:
    pass


def main():
    try:
        aqi_list = Taiwan_AQI.download_AQI()
    except Exception as err:
        print(err.args)
        #print(str(err))
        return
    
    #get_best(aqi_list)

    print("aqi目前站點最好的3個")
    for i in get_best(aqi_list):
        print(i)
    print("aqi目前站點最差的3個")
    for i in get_bad(aqi_list):
        print(i)
    


if(__name__ == "__main__"):
    main()