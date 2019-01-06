from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/')
def homepage():
    with open('data/movies_list.txt') as file:
        movie_lst = file.read().splitlines()
    #print(movie_lst)
    return render_template("main.html", movie_list=movie_lst)

if __name__ == "__main__":
    app.run()
