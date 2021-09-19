import requests

rv = requests.post('https://s-map.herokuapp.com/postbuildinginfo', json={
    "buildingname": "MC",
    "wifi": True,
    "ports": False,
    "soundlevel": 2
})
print(rv)
rv2 = requests.post('https://s-map.herokuapp.com/updatebuildinginfo', json={
    "buildingname": "MC",
    "name": "First Last"
})
print(rv2)
rv3 = requests.get('https://s-map.herokuapp.com/getbuildinginfo')
print(rv3.json())