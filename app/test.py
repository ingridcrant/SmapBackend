import requests

rv = requests.post('http://s-map.herokuapp.com/postbuildinginfo', json={
    "buildingname": "MC",
    "wifi": True,
    "ports": False,
    "soundlevel": 2
})
print(rv)
rv2 = requests.post('http://s-map.herokuapp.com/updatebuildinginfo', json={
    "buildingname": "MC",
    "name": "First Last"
})

rv3 = requests.get('http://s-map.herokuapp.com/getbuildinginfo')
print(rv3.json())