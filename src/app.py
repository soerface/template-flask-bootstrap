from flask import Flask, render_template, request

from fizzbuzz import fizzbuzz

app = Flask(__name__)


@app.context_processor
def add_navigation() -> dict:
    endpoints = [
        ('index', 'Home'),
        ('about', 'About')
    ]
    items = [{
        'active': request.endpoint == endpoint,
        'endpoint': endpoint,
        'title': title,
    } for endpoint, title in endpoints]

    return {
        'navigation': items,
    }


@app.route('/')
def index():
    results = [{
        'input': x,
        'output': fizzbuzz(x),
    } for x in range(25, 41)]
    return render_template('index.html', results=results)


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
