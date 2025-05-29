import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    songs = os.listdir("static/songs")
    songs = [song for song in songs if song.endswith(".mp3")]
    songs.sort()  # ✅ Sort alphabetically
    selected_index = 0
    return render_template("index.html", songs=songs, selected_index=selected_index)

if __name__ == "__main__":
    app.run(debug=True)
