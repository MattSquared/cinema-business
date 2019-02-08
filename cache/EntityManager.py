from cache.Configuration import Session, start_db
from cache.models import Cinema, Showtimes


class EntityManager():
    ''' Class for fetch/persist Cinema and Showtime entities from/into the database 
    Exposed methods:
        > existsCinema(): given a cinema ID, it checks if the related Cinema entity is persisted or not
        > existsShowtimes(): given the pair (cinemaId,filmId), it checks if the related Showtimes entity is persisted or not
        > getCinema(): given a cinema ID, it fetches the related Cinema entity from the database
        > getShowtime(): given the pair (cinemaId,filmId), it fetches the related Showtime entity from the database
        > saveCinema(): given an dictionary representation, it persists data as Cinema entity into the database
        > saveShowtimes(): given an dictionary representation, it persists data as Showtimes entity into the database
    '''
    
    def __init__(self):
        ''' Constructor of the class '''
        start_db()
    
    
    def __existsCinema(self, cinemaId):
        ''' Method for check if a cinema entity already exists
            Arguments:
                - cinemaId: cinema identifier corresponding to the related table row
            Returns: True if exists, otherwise False
        '''
        return (Session.query(Cinema.cinema_id).filter(Cinema.cinema_id == cinemaId).scalar() is not None)
    
    
    def __existsShowtimes(self, cinemaId, filmId):
        ''' Method for check if a showtime entity already exists
            Arguments:
                - cinemaId: cinemaId identifier corresponding to the related table row
                - filmId: filmId identifier corresponding to the related table row
            Returns: True if exists, otherwise False
        '''
        return (Session.query(Showtimes.id).filter(Showtimes.cinema_id == cinemaId, Showtimes.film_id == filmId).scalar() is not None)
    
        
    def getCinema(self, cinemaId):
        ''' Method for fetching a Cinema entity from the database
            Arguments:
                - cinemaId: cinema identifier corresponding to the related table row
            Returns: a dictionary representation of the Cinema entity
        '''
        cinema = Session.query(Cinema).filter(Cinema.cinema_id == cinemaId).one_or_none()
        if cinema:
            return cinema.to_dict()
    
    
    def getShowtimes(self, cinemaId, filmId):
        ''' Method for fetching a Showtimes entity from the database
            NOTE: The pair (cinemaId,filmId) is the primary key for Showtime entities
            Arguments:
                - cinemaId: cinema identifier corresponding to the related table row
                - filmId: film identifier corresponding to the related table row
            Returns: a dictionary representation of the Showtimes entity
        '''
        showtimes = Session.query(Showtimes).filter(Showtimes.cinema_id == cinemaId, Showtimes.film_id == filmId).one_or_none()
        if showtimes:
            return showtimes.to_dict()
    
    
    def saveCinema(self, obj):
        ''' Method for pesist a Cinema entity into the database
            Arguments:
                - obj: object representation of the Cinema entity
        '''
        cinema = Cinema(obj)
        if not self.__existsCinema(cinema.cinema_id):
            Session.add(cinema)
            Session.commit()
    
    
    def saveShowtimes(self, obj):
        ''' Method for pesist a Showtime entity into the database
            Arguments:
                - obj: object representation of the Showtime entity
        '''
        showtimes = Showtimes(obj)
        if not self.__existsShowtimes(showtimes.cinema_id, showtimes.film_id):
            Session.add(showtimes)
            Session.commit()
