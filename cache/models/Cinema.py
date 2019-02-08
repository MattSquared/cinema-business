from sqlalchemy import Column, String
from cache.Configuration import Base
from json import dumps, loads


''' Model for Cinema entities '''
class Cinema(Base):
    ''' Cinema object mapped to CINEMA table
        Attributes/Columns:
            - cinema_id varchar(12) primary_key
            - cinema_name varchar(30)
            - address varchar(30)
            - city varchar(30)
            - lat varchar(12)
            - lng varchar(12)
            - contact varchar(256)
            - url varchar(128)
            - hours varchar(256)
    '''
    __tablename__ = "CINEMAS"
    cinema_id = Column(String(12), primary_key=True)
    cinema_name = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    lat = Column(String(12), nullable=False)
    lng = Column(String(12), nullable=False)
    contact = Column(String(256), nullable=True)
    url = Column(String(128), nullable=True)
    hours = Column(String(256), nullable=True)
    
    def __init__(self, obj):
        ''' Constructor of the class
            Arguments:
                - obj: map of cinema attributes
        '''
        self.cinema_id = obj.get("cinema_id")
        self.cinema_name = obj.get("cinema_name")
        self.address = obj.get("address")
        self.city = obj.get("city")
        self.lat = obj.get("lat")
        self.lng = obj.get("lng")
        self.contact = dumps(obj.get("contact"))
        self.url = dumps(obj.get("url"))
        self.hours = dumps(obj.get("hours"))
    
    def to_dict(self):
        return {
            "cinema_id": self.cinema_id,
            "cinema_name": self.cinema_name,
            "address": self.address,
            "city": self.city,
            "lat": self.lat,
            "lng": self.lng,
            "contact": loads(self.contact),
            "url": loads(self.url),
            "hours": loads(self.hours)
        }

