from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if(request.method == 'POST'):






        return "hi"
    else:
        return "bye"

if(__name__ == '__main__'):
    app.run(debug=True)