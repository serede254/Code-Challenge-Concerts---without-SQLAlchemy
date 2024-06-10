class Band:
    all=[]
    def __init__(self, name, hometown):
        # Ensure hometown is a non-empty string
        if isinstance(hometown, str) and len(hometown):
            self._hometown = hometown
        else:
            raise ValueError("Hometown must be a non-empty string")
        # Ensure name is a non-empty string
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
        Band.all.append(self) 
    
    # Getter and setter for name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    # Getter for hometown property
    @property
    def hometown(self):
        return self._hometown

    # Method to get all concerts of the band
    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.band == self]

    # Method to get all venues where the band has performed
    def venues(self):
        venues = list(set(concert.venue for concert in self.concerts()))
        return venues if venues else None

    # Method to add a concert for the band in a venue
    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        return Concert(date, self, venue)

    # Method to get introductions for all concerts of the band
    def all_introductions(self):
        return [
            concert.introduction() for concert in self.concerts() if concert.introduction()
        ]


class Concert:
    all_concerts = []

    def __init__(self, date, band, venue):
        # Ensure date is a non-empty string
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError("Date must be a non-empty string.")
        # Ensure band is an instance of Band
        if not isinstance(band, Band):
            raise TypeError("Band must be of type Band")
        self._band = band
        # Ensure venue is an instance of Venue
        if isinstance(venue, Venue):
            self._venue = venue
        else:
            raise ValueError("Venue must be an instance of Venue class.")
        Concert.all_concerts.append(self)

    # Getter and setter for date property
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string.")

    # Getter for band property
    @property
    def band(self):
        return self._band

    # Getter for venue property
    @property
    def venue(self):
        return self._venue

    # Method to check if the concert is in the band's hometown
    def hometown_show(self):
        return self.band.hometown == self.venue.city

    # Method to generate introduction for the concert
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all=[]
    def __init__(self, name, city):
        # Ensure name is a non-empty string
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
        # Ensure city is a non-empty string
        if isinstance(city, str) and len(city) > 0:
            self._city = city
        else:
            raise ValueError("City must be a non-empty string.")
        Venue.all.append(self)

    # Getter and setter for name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    # Getter and setter for city property
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string.")

    # Method to get all concerts held in the venue
    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.venue == self]

    # Method to get all bands that have performed in the venue
    def bands(self):
        return list({concert.band for concert in self.concerts()})
    
    # Method to get the concert held in the venue on a specific date
    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None
