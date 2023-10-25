from flask import Flask, render_template
import requests

app = Flask(__name__)

# Define the API URL
API_URL = "https://jsonplaceholder.typicode.com/posts"

@app.route('/')
def index():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return render_template('index.html', data=data)
    return "Failed to fetch data from the API."

if __name__=="__main__":
    app.run(host="0.0.0.0")
