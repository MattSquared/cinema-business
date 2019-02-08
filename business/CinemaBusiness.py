from adapter import adapter_service
from cache import cache_service, clean_db


class CinemaBusiness:
    ''' This class implements the business logic and interacts directly with the adapter service for retrieve information about cinemas
        Exposed methods:
            > findCinema(): given a GPS position and the cinema ID, it retrieves the related instance from the cache.
            > findDetailedShowings(): given a GPS position, device datetime, cinema ID and a date, it retrieves all the showings of the related cinema in the precise date.
            > findNearby(): given a GPS position, device datetime, it retrieves the nearby cinemas according to the client geolocation. Parameter n is optional and filters the number of items to return 
            > findShowings(): given a GPS position, device datetime, cinema ID and a date, it retrieves all the showings and puts the related showtimes in the cache.
            > findShowtimes(): given a cinema ID and a film ID, it retrieves the related showtimes from the cache.
    '''    
    
    def cleanCache(self):
        ''' Method for clean the cache service database '''
        clean_db()

    
    def findNearby(self, position, datetime, n):
        ''' Method for find nearby cinemas in the given GPS position
            Arguments:
                - position: string containing GPS position
                - datetime: string containing the device datetime in ISO format
                - n (optional): integer representing the maximum number of items to fetch
            Returns: a dictionary object containing the fetched data, otherwise a empty object if there is no result
        '''
        result = adapter_service.getNearby(position, datetime, n)
        if result:
            cinemas = []
            filters = ["cinema_id", "cinema_name"]
            for cinema in result.get("cinemas"):
                response = adapter_service.getCinemaInfo(cinema.get("lat"), cinema.get("lng"), cinema.get("cinema_name"))
                if response:
                    cinema.update(response.get("cinemainfo"))
                cache_service.saveCinema(cinema)
                cinemas.append({k:v for k,v in cinema.items() if k in filters})
            return {"cinemas": cinemas}
    
    
    def findCinema(self, position, cinema):
        ''' Method for retrieve from the cache information about the given cinema and generates URLs for map image and route
            Arguments:
                - position: string containing GPS position
                - cinema: string containing the cinema ID
            Returns: a dictionary object containing the fetched data, otherwise a empty object if there is no result
        '''
        result = cache_service.getCinema(cinema)
        if not result: return
        response = adapter_service.getCinemaRoute(position, result.get("lat"), result.get("lng"))
        if response:
            result.update(response.get("cinemaroute"))
            return result
    
    
    def findDetailedShowings(self, position, datetime, cinema, date):
        ''' Method for find detailed information about showings in the given cinema and date
            Arguments:
                - position: string containing GPS position
                - datetime: string containing the device datetime in ISO format
                - cinema: string containing the cinema ID
                - date: string containing the date in YYYY-MM-DD format
            Returns: a dictionary object containing the fetched data, otherwise a empty object if there is no result
        '''
        return adapter_service.getShowtimes(position, datetime, cinema, date)
    
    
    def findShowings(self, position, datetime, cinema, date):
        ''' Method for find information about showings and to cache the related showtimes
            Arguments:
                - position: string containing GPS position
                - datetime: string containing the device datetime in ISO format
                - cinema: string containing the cinema ID
                - date: string containing the date in YYYY-MM-DD format
            Returns: a dictionary object containing the fetched data, otherwise a empty object if there is no result
        '''
        result = adapter_service.getShowtimes(position, datetime, cinema, date)
        if result:
            films = []
            filters = ["film_id", "imdb_id", "film_name"]
            cacheFilters = ["film_id", "film_name", "showings", "show_dates"]
            for film in result.get("films"):
                showtimes = {"cinema_id": cinema}
                showtimes.update({k:v for k,v in film.items() if k in cacheFilters})
                cache_service.saveShowtimes(showtimes)
                films.append({k:v for k,v in film.items() if k in filters})
            return {"films": films}
    
    
    def findShowtimes(self, cinema, film):
        ''' Method for retrieve from the cache the information about showtimes for a given cinema and film
            Arguments:
                - cinema: string containing the cinema ID
                - film: string containing the film ID
            Returns: a dictionary object containing the fetched data, otherwise a empty object if there is no result
        '''
        result = cache_service.getShowtimes(cinema, film)
        if result:
            return {"showtimes": result}
 
