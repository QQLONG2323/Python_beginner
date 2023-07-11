from tools import Taiwan_AQI

def main():
    try:
        Taiwan_AQI.download_AQI()
    except Exception as err:
        print(err.args)
        return


if(__name__ == "__main__"):
    main()