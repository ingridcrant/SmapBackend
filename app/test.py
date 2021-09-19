import requests

rv = requests.post('http://0.0.0.0:80/postbuildinginfo', json={
    "buildingname": "MC",
    "wifi": True,
    "ports": False,
    "soundlevel": 2
})
print(rv)
rv2 = requests.post('http://0.0.0.0:80/updatebuildinginfo', json={
    "buildingname": "MC",
    "name": "First Last"
})

rv3 = requests.get('http://0.0.0.0:80/getbuildinginfo')
print(rv3.json())