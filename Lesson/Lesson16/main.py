from tools import Taiwan_AQI

def main():
    try:
        Taiwan_AQI.download_AQI()
    except Exception as err:
        print(err.args)
        print(str(err))
        return


if(__name__ == "__main__"):
    main()