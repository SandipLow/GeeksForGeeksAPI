from flask import Flask, render_template
from flask_restful import Api, Resource
from modules.scrap import scrap

app = Flask(__name__)
api = Api(app)

class geeksforgeeksAPI(Resource):
    def get(self, username):
        scrapper = scrap(username)
        return scrapper.fetchResponse() 


api.add_resource(geeksforgeeksAPI, "/userdata/<string:username>")

@app.route('/stats/<string:username>')
def stats(username):
    scrapper = scrap(username)
    userdata = scrapper.fetchResponse()

    return render_template('stats.html', userdata=userdata)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)