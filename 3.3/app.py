from flask import Flask, render_template
import random

app = Flask(__name__) # list of at images
images = [
    "https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif",
    "https://media.giphy.com/media/xUPGcyi4YxcZp8dWZq/giphy.gif",
    "https://media.giphy.com/media/1iu8uG2cjYFZS6wTxv/giphy.gif",
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/lJNoBCvQYp7nq/giphy.gif" ]

@app.route('/') 
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")