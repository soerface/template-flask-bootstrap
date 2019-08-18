from flask_frozen import Freezer
from app import app


def main():
    app.config['FREEZER_DESTINATION'] = '../build'
    freezer = Freezer(app)
    freezer.freeze()


if __name__ == '__main__':
    main()
