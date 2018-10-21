from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Lunching & learning...'


    @app.route('/git')
    def git():
        return 'From git...'


    @app.route('/great')
    def great():
        return '...to great'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80)