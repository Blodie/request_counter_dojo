from flask import Flask, request, redirect, render_template
app = Flask(__name__)

request_methods_counter = {"GET": 0, "POST": 0, "DELETE": 0, "PUT": 0}

@app.route('/')
def route_index():
    return render_template('index.html')

@app.route("/request-counter", methods=['GET', 'POST', 'DELETE', 'PUT'])
def counter():
    if request.method == 'GET':
        request_methods_counter["GET"] += 1
    elif request.method == 'POST':
        request_methods_counter["POST"] += 1
    elif request.method == 'DELETE':
        request_methods_counter["DELETE"] += 1
    elif request.method == 'PUT':
        request_methods_counter["PUT"] += 1
    return render_template('index.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html', methods=request_methods_counter)

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )