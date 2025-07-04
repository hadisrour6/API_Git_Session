import requests

headers1 = {
    "Accept": "application/json",
}

res = requests.get("https://icanhazdadjoke.com/", headers=headers1)
#print("CASE 1:", res.json(),"\n")

#Case 1, we made a get request call to dad joke API using headers accept, saying we want result as JSON.

res = requests.get("https://icanhazdadjoke.com/")
#print("CASE 2:", res.text)


#Case 2, we made a request get call to dad joke API with no headers so it gave us HTML code which we dont want.


payload = {
    "name": "Hadi",
    "job": "Software Dev"
}

reqres_header = {
    "x-api-key" : "reqres-free-v1"

}
res = requests.post(url= "https://reqres.in/api/users", headers=reqres_header, json=payload)

print(res.json())