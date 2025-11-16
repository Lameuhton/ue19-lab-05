import requests

def main():
    url = "https://v2.jokeapi.dev/joke/Any"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get("type") == "single":
            print("Blague: ",data.get("joke"))
        else:
            print("Blague: ",data.get("setup"))
            print("Réponse: ",data.get("delivery"))
    
    else:
        print("Erreur lors de la requête:", response.status_code)
    

if __name__ == "__main__":
    main()