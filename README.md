# Cinema Business Service
## Description
This service implements the business logic to manage information fetched from by **MovieGlu**, **MapQuest** and **FourSquare** (through the **CinemaAdapter** service) and to handle requests of accessing to those data from the Process Centric service (Telegram Bot).  
The service is a web application implemented in Python by using **Flask** and its extension called **Flask-RESTplus**.  
The service relies on the **Cinema Adapter** service to retrieve information provided by **MovieGlu**, **MapQuest** and **FourSquare**.

## Modules
- **BusinessService**: implements a Flask application for managing requests from the Process Centric service.
- **CinemaService**: class that implements the business logic in this service. It forwards requests to the CinemaAdapter in order to retrieve the wanted information. Some of the results returned from CinemaAdapter are stored inside a cache service so that they can be provided without performing redundant requests to MovieGlu, MapQuest and FourSquare.
- **Adapter**: class that directly interacts with CinemaAdapter service. It acts as interface and access point for those modules that want to interact with the adapter service.
- **Cache**: class that wraps methods for quering MoviesGlu.

## References
### Flask
- Flask: [http://flask.pocoo.org/](http://flask.pocoo.org/)
- Flask-RESTplus: [https://flask-restplus.readthedocs.io/en/stable/index.html](https://flask-restplus.readthedocs.io/en/stable/index.html)

### MovieGlu
- MovieGlu: [https://www.movieglu.com/](https://www.movieglu.com/)
- MovieGlu APIs: [https://developer.movieglu.com/](https://developer.movieglu.com/)

### FourSquare
- FourSquare: [https://foursquare.com/](https://foursquare.com/)
- FourSquare APIs: [https://developers.foursquare.com/]([https://developers.foursquare.com/])

### MapQuest
- MapQuest: [https://www.mapquest.com](https://www.mapquest.com)
- MapQuest APIs: [https://developer.mapquest.com](https://developer.mapquest.com)

