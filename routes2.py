from flask import Flask
from flask import send_file
app = Flask(__name__)
def open_(file):
    fileObject = open(file, "r",encoding='utf-8')
    data = fileObject.read()
    return data

@app.route('/fonts/<path>')
def fonts(path):
    print("fonts REQUEST")
    return send_file(str("./media/"+path))
@app.route('/buying')
def buying():
    print("buying REQUEST")
    return open_('buying.html')
@app.route('/images/<path>')
def images(path):
    print("iamge REQUEST")
    return send_file(str("./images/"+path))
@app.route('/media/<path>')
def media(path):
    print("MEDIA REQUEST")
    return send_file(str("./media/"+path))
@app.route('/css/<path>')
def css(path):
    print("CSS REQUEST")
    return send_file(str("./css/"+path))
@app.route('/js/<path>')
def js(path):
    return send_file(str("./js/"+path))
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path[-4:]==".jpg":
        return send_file(str('./'+path))
    return open_(str('./'+path)) 


if __name__ == '__main__':
    app.run()
