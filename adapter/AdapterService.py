from json import load
import requests


class AdapterService():
    ''' This class interacts with cinema-adapter service to retrieve resources from MoviesGlu
        Exposed methods:
            > getNearby(): given GPS location, retrieves the list of nearby cinemas
            > getShowtimes(): given a cinema ID and a date, retrieves the shotimes for the wanted date 
    '''
    
    def __init__(self):
        ''' Constructor of the class '''
        configs = load(open("./adapter/config.json", "r"))
        self.__server = configs.get("cinema-adapter")
    
    
    def __get_request(self, request, headers=None, params=None,):
        ''' Method for performing HTTP GET requests
            Arguments:
                - request: string containing the URI of the request
                - headers (optional): map of further headers to include in the request
                - params (optional): map of parameters to provide via GET
            Returns: JSON object if status code is OK, otherwise None (null object)
        '''
        response = requests.get(url=request, headers=headers, params=params)
        if response.status_code == requests.codes.get("ok"):
            return response.json()
        
    
    def getCinemaInfo(self, lat, lng, name):
        ''' Method for retrieve information about a given cinema
            Headers:
                - lat, lng: pair of strings containing the cinema GPS position
            Arguments:
                - name: string containing the venue name
            Returns: JSON object if status code is OK, otherwise None (null object)
        '''
        request = "{}/cinemainfo".format(self.__server)
        headers = {"lat": "{}".format(lat), "lng": "{}".format(lng)}
        params = {"name": name}
        return self.__get_request(request, headers, params)    
    
    
    def getCinemaRoute(self, geolocation, lat, lng):
        ''' Method for retrieve the route from the device location to the cinema location
            Headers:
                - geolocation: string containing the GPS position of the device
            Parameters: 
                - lat, lng: pairs of strings containing the cinema GPS position
            Returns: JSON object if status code is OK, otherwise None (null object)
        '''
        request = "{}/cinemaroute".format(self.__server)
        headers = {"geolocation": geolocation}
        params = {"lat": "{}".format(lat), "lng": "{}".format(lng)}
        return self.__get_request(request, headers, params)
        
    
    def getNearby(self, geolocation, datetime, n=None):
        ''' Method for retrieve a list of nearby cinemas
            Arguments:
                - geolocation: string containing the GPS position of the device
                - datetime: string containing the device datetime in ISO format
                - n (optional): integer representing the maximum number of elements to return
            Return: JSON object if status code is OK, otherwise None (null object)
        '''
        request = "{}/nearby".format(self.__server)
        headers = {"geolocation": geolocation, "datetime": datetime}
        params = {"n": n} if n else None
        return self.__get_request(request, headers, params)
        
    
    def getShowtimes(self, geolocation, datetime, cinema, date):
        ''' Method for retrieve the showtimes in a date for a given cinema
            Arguments:
                - geolocation: string containing the GPS position of the device
                - datetime: string containing the device datetime in ISO format
                - cinema_id: string containing the cinema ID
                - date: string containing the date in YYYY-MM-DD format
            Returns: JSON object if status code is OK, otherwise None (null object)
        '''
        request = "{}/showtimes".format(self.__server)
        headers = {"geolocation": geolocation, "datetime": datetime}
        params = {"cinema_id": cinema, "date": date}
        return self.__get_request(request, headers, params)
        
