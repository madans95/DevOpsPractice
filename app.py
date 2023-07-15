from flask import Flask

#https://www.markdownguide.org/basic-syntax/
#herovired_devops_classcodes

app = Flask(__name__)

@app.route("/", methods=['GET'])
def helloWorld():
    return "Hello World!!"

@app.route("/aboutus", methods=['GET'])
def aboutUS():
    return "About Us"

if __name__ == "__main__":
    app.run(port=3000, debug=True)