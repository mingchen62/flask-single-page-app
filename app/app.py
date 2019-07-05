import time
import requests
import requests_cache

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

requests_cache.install_cache('my_cache', backend='sqlite', expire_after=180)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # user inputs
        content = request.json
        print(content)

        # api call
        #url = "https://api.github.com/search/users?q=location:{0}+language:{1}".format(first, second)
        #now = time.ctime(int(time.time()))
        #response = requests.get(url)
        #print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
        res={}
        res['summary']="I am so happy"

        # return json
        #return jsonify(response.json())
        return jsonify(res)

    return render_template('index.html')

# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    try:
        _port=int(os.environ["_PORT"])
        app.logger.debug("_port config:"+ _port)  
    except:
        _port=8080
    app.run(port=_port,debug=True)
