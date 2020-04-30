from app import app
from flask import render_template


@app.route('/')
def index():
    template = render_template(
        'index.html',
        title="Faculdade Impacta de Técnologia",
        h1="Hi there this is an H1 tag",
        lista=['a', 'b', 'c']
    )

    return template


app.run(debug=True)
