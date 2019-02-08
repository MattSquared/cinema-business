from flask import Flask, request
from flask_restplus import Api, Resource
from business import cinema_service, errors


business_service = Flask(__name__)
api = Api(business_service)


''' Resource Nearby is mapped to URI "/nearby" '''
@api.route("/nearby")
class Nearby(Resource):
    def get(self):
        ''' GET method for retrieve Nearby resource
            Headers:
                - position: string representing the geographic coordinates in "float(x);float(y)" format
                - datetime: string representing the device datetime in ISO format
            Parameters: 
                - n (optional): integer representing the maximum number of cinemas to fetch
            Returns: JSON object containing the dataset if response is OK
        '''
        n = request.args.get("n")
        position = request.headers.get("position")
        datetime = request.headers.get("datetime")
        if not (position and datetime):
            return errors.missing_headers("position, datetime")
        nearby = cinema_service.findNearby(position, datetime, n)
        return nearby if nearby else errors.not_found("nearby")


''' Resource Cinema is mapped to URI "/cinema" '''
@api.route("/cinema")
class Cinema(Resource):
    def get(self):
        ''' GET method for retrieve Cinema resource
            Headers:
                - position: string representing the geographic coordinates in "float(x);float(y)" format
            Parameters:
                - cinema_id: string representing the cinema ID
            Returns: JSON object containing the dataset if response is OK
        '''
        cinemaId = request.args.get("cinema_id")
        position = request.headers.get("position")
        if not position:
            return errors.missing_headers("position")
        if not cinemaId:
            return errors.missing_args("cinema_id")
        cinema = cinema_service.findCinema(position, cinemaId)
        return cinema if cinema else errors.not_found("cinema_id=" + cinemaId)


''' Resource DetailedShowings is mapped to URI "/detailedShowings" '''
@api.route("/detailedShowings")
class DetailedShowings(Resource):
    def get(self):
        ''' GET method for retrieve DetailedShowtimes resource
            Headers:
                - position: string representing the geographic coordinates in "float(x);float(y)" format
                - datetime: string representing the device datetime in ISO format
            Parameters:
                - cinema_id: string representing the cinema ID
                - date: string representing the date in "YYYY-MM-DD" format
            Returns: JSON object containing the dataset if response is OK
        '''
        cinemaId = request.args.get("cinema_id")
        date = request.args.get("date")
        position = request.headers.get("position")
        datetime = request.headers.get("datetime")
        if not (position and datetime):
            return errors.missing_headers("position, datetime")
        if not (cinemaId and date):
            return errors.missing_args("cinema_id, date")
        showings = cinema_service.findDetailedShowings(position, datetime, cinemaId, date)
        return showings if showings else errors.not_found("cinema_id={}, date={}".format(cinemaId, date))


''' Resource Showings is mapped to URI "/showings" '''
@api.route("/showings")
class Showings(Resource):
    def get(self):
        ''' GET method for retrieve Showtimes resource
            Headers:
                - position: string representing the geographic coordinates in "float(x);float(y)" format
                - datetime: string representing the device datetime in ISO format
            Parameters:
                - cinema_id: string representing the cinema ID
                - date: string representing the date in "YYYY-MM-DD" format
            Returns: JSON object containing the dataset if response is OK
        '''
        cinemaId = request.args.get("cinema_id")
        date = request.args.get("date")
        position = request.headers.get("position")
        datetime = request.headers.get("datetime")
        if not (position and datetime):
            return errors.missing_headers("position, datetime")
        if not (cinemaId and date):
            return errors.missing_args("cinema_id, date")
        showings = cinema_service.findShowings(position, datetime, cinemaId, date)
        return showings if showings else errors.not_found("cinema_id={}, date={}".format(cinemaId, date))


''' Resource Showtimes is mapped to URI "/showtimes" '''
@api.route("/showtimes")
class Showtimes(Resource):
    def get(self):
        ''' GET method for retrieve Showtimes resource
            Parameters:
                - cinema_id: string representing the cinema ID
                - film_id: string representing the film ID
            Returns: JSON object containing the dataset if response is OK
        '''
        cinemaId = request.args.get("cinema_id")
        filmId = request.args.get("film_id")
        if not (cinemaId and filmId):
            return errors.missing_args("cinema_id, film_id")
        showtimes = cinema_service.findShowtimes(cinemaId, filmId)
        return showtimes if showtimes else errors.not_found("cinema_id={}, film_id={}".format(cinemaId, filmId))



@business_service.teardown_appcontext
def cleanup(error=None):
    cinema_service.cleanCache()



if __name__ == "__main__":
    business_service.run()

