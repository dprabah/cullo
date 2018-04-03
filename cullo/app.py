from flask import Flask, request
from cullo.services.conversation.response import send_message
from cullo.services.language import Interpreter

app = Flask(__name__, static_url_path='')
app.config['DEBUG'] = True
app.secret_key = 'the random code'


@app.route('/ask', methods=["POST"])
def ask():
    user_query = request.get_json()['query']
    print(user_query)
    state = request.get_json()['state']
    pending = request.get_json()['pending']
    if pending is not None:
        pending = tuple(pending)
    print(pending)
    # store_queries.store_query(user_query,request.remote_addr)
    d = send_message(int(state), pending, user_query)
    # state, pending, bot_response = start([user_query])
    return d


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
    Interpreter.preprocess()
    app.run(debug=True, use_reloader=False)

