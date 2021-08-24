from flask import Flask, json,jsonify,request
app = Flask(__name__)
tasks  = [
    {
        "id":1,
        "Name":u" Raju",
        "contact":u"9875757964",
        "done": False
    },
    {
         "id":2,
        "Name":u" Rahul",
        "contact":u"9874685964",
        "done": False
         
    }
] 
@app.route("/add-data",methods = ["POST"])
def addTasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the data",

        },400)
    task = {
        "id":tasks[-1]["id"]+1,
        "Name":request.json["Name"],
        "contact":request.json.get("contact",""),
        "done": False
    }
    tasks.append(task)

    return jsonify({
        "status":"success",
        "message":"Task added successfully",
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks,

    })
    
if(__name__ == "__main__"):
    app.run(debug = True)