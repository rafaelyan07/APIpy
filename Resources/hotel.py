from flask_restful import Resource, reqparse

hoteis = [
        {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
        }
]
class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel ['hotel_id'] == hotel_id:
                return hotel
        return {'messagem': 'hotel not found.'}, 404 # not found

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
