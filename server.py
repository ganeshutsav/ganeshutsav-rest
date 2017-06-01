import flask

from ganeshutsav_rest.rest.mandal.controller.mandal_controller import mandal_app


class Server(object):
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.app.register_blueprint(mandal_app, url_prefix='/mandals')

    def run(self):
        self.app.run(debug=True, port=21000)


if __name__ == '__main__':
    Server().run()
