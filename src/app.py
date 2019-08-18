from flask import Flask, render_template, request

app = Flask(__name__)


@app.context_processor
def add_navigation():
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
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
