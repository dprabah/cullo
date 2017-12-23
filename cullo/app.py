from flask import Flask



app = Flask(__name__, static_url_path='')
app.config['DEBUG'] = True
app.secret_key = 'the random code'

@app.route("/")
def main():
    return app.send_static_file('view/index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)