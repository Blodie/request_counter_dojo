from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/')
def route_index():
    pass

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )