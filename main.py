from flask import Flask, request
from flask_restful import Resource, Api
import pickle
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)


class MakePrediction(Resource):

    def post(self):
        posted_data = request.get_json()
        vehicleType = posted_data['vehicleType']
        gearbox = posted_data['gearbox']
        powerPS = posted_data['powerPS']
        model = posted_data['model']
        kilometer = posted_data['kilometer']
        monthOfRegistration = posted_data['monthOfRegistration']
        fuelType = posted_data['fuelType']
        brand = posted_data['brand']
        estimation = pickle.load(open('finalized_model.pkl', 'rb'))
        prediction = estimation.predict([[vehicleType, gearbox, powerPS, model, kilometer, monthOfRegistration, fuelType, brand]])
        return prediction


api.add_resource(MakePrediction, '/predict')


if __name__ == '__main__':
    app.run(debug=True)