from flask import Flask, jsonify, request

app = Flask(__name__)

List = [ { 
    'id': 1, 
    'Name': u'Raju', 
    'Contact': u'9987644456', 
    'done': False 
}, 
{   'id': 2, 
    'Name': u'Rahul', 
    'Contact': u'9876543222', 
    'done': False 
} ] and def as def add_task(): 
    if not request.json: 
        return jsonify({ 
            "status":"error", 
            "message": "Please provide the data!" },400) 
        contact = { 'id': tasks[-1]['id'] + 1, 
        'Name': request.json['Name'], 
        'Contact': request.json.get('Contact', ""), 
        'done': False } 
        List.append(contact) 
        return jsonify({ "status":"success", "message": "Contact added succesfully!" })

@app.route("/add-data", methods = ["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        }, 400)

    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "task added successfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data": tasks
    })

if(__name__ == "_main_"):
    app.run(debug = True)

print("Hi")