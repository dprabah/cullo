from flask import Flask, request
from model import store_queries


app = Flask(__name__, static_url_path='')
app.config['DEBUG'] = True
app.secret_key = 'the random code'

@app.route('/ask', methods=["POST"])
def forgot_password():
    print(request.get_json()['query'])
    store_queries.store_query(request.get_json()['query'],request.remote_addr)
    return "Im a new born Baby! Still lot to learn to answer your queries!"

@app.route('/fonts/<path:path>')
def send_font(path):
    return app.send_static_file('fonts/'+path)

@app.route('/css/<path:path>')
def send_css(path):
    return app.send_static_file('css/'+path)

@app.route('/js/<path:path>')
def send_js(path):
    return app.send_static_file('js/'+path)

@app.route("/")
def main():
    return app.send_static_file('view/index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)