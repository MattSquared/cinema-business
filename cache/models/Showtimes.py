from sqlalchemy import Column, Integer, String
from cache.Configuration import Base
from json import dumps, loads



''' Model for Showtimes entities '''
class Showtimes(Base):
    ''' Showtimes object mapped to SHOWTIMES table
        Attributes/Columns:
            - id integer primary_key
            - cinema_id varchar(12)
            - film_id varchar(12)
            - film_name varchar(128)
            - showings varchar(1024)
            - show_dates varchar(1024)
    '''
    __tablename__ = "SHOWTIMES"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cinema_id = Column(String(12), nullable=False)
    film_id = Column(String(12), nullable=False)
    film_name = Column(String(128), nullable=False)
    showings = Column(String(1024), nullable=False)
    show_dates = Column(String(1024), nullable=False)
    
    def __init__(self, obj):
        ''' Constructor of the class
            Arguments:
                - obj: map of showtimes attributes
        '''
        self.cinema_id = obj.get("cinema_id")
        self.film_id = obj.get("film_id")
        self.film_name = obj.get("film_name")
        self.showings = dumps(obj.get("showings"))
        self.show_dates = dumps(obj.get("show_dates"))
    
    def to_dict(self):
        return {
            "cinema_id": self.cinema_id,
            "film_id": self.film_id,
            "film_name": self.film_name,
            "showings": loads(self.showings),
            "show_dates": loads(self.show_dates)
        }

