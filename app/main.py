from flask import Flask, jsonify, request
import os
  
app = Flask(__name__)

# building has properties wifi (color change), num_people (change color if full), ports,
# sound level: silent, low, medium, high

# format = { "building":
#   { "num_people": "number",
#     "names": ["name1"],
#     "wifi": "boolean",
#     "soundlevel": "0, 1, 2, or 3",
#     "ports": "boolean"}
# }
building_to_info = {}

@app.route('/getbuildinginfo', methods=['GET'])
def get_building_info():
    return jsonify(building_to_info)

@app.route('/postbuildinginfo', methods=['POST'])
def post_building_info():
    info = request.get_json()

    building_to_info[info['buildingname']] = {"num_people": 0,
                                       "names": [],
                                       "wifi": bool(info['wifi']),
                                       "soundlevel": int(info['soundlevel']),
                                       "ports": bool(info['ports'])
                                    }
    
    return jsonify({"success": True}), 200

@app.route('/updatebuildinginfo', methods=['POST'])
def updatebuildinginfo():
    info = request.get_json()

    data = building_to_info[info['buildingname']]
    data["num_people"] = data["num_people"] + 1
    data["names"] = data["names"] + [info['name']]
    
    return jsonify({"success": True}), 200

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)