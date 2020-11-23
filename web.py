"""A simple web page."""


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    ascii_art_robot = """<pre>
 __________________________________
< Hi, I'm a simple discord bot! :) >
 ----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\/
                ||----w |
               _||    _||

</pre>
"""
    return f"{ascii_art_robot}\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0")