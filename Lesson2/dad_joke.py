import requests

headers = {
    "Accept" : "application/json",
    "User-Agent": "DadJokeCLI (https://github.com/yourusername/dadjokecli)"
}
def fetch_dad_joke():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("User not found or error occurred.")
        return

    data = response.json()

    return data['joke']


for i in range(10):
    print(fetch_dad_joke())