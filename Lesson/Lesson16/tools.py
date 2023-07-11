class Taiwan_AQI():

    API_KEY = "657f239f-f6e5-49fb-b8e0-966c8f789a5b"

    @classmethod    
    def download_AQI(cls) -> list:
        import requests
        response = requests.get(f"https://data.epa.gov.tw/api/v2/aqx_p_434?api_key={cls.API_KEY}&limit=1000&sort=monitordate desc&format=CSV")
        
        if(response.ok):
            print(response.text)
        else:
            raise Exception("下載失敗", '真的失敗')