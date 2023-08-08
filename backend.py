import requests


API_KEY = "67433d4bbefc13d7ef0af417244dba10"

def get_data(place,forecast_days=None,kind=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data =filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data =[dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data=[dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__=="__main__":
    get_data(place="Tokyo",forecast_days=3,kind="Temperature")
