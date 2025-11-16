import requests

def main():
    url = "https://v2.jokeapi.dev/joke/Any"

    response = requests.get(url)
    data = response.json()

    if data.get("type") == "single":
        print("Blague: ",data.get("joke"))
    else:
        print("Blague: ",data.get("setup"))
        print("Réponse: ",data.get("delivery"))
    

if __name__ == "__main__":
    main()