import requests


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street=None,
        city=None,
        state=None,
        postal_code=None,
        country=None,
        longitude=None,
        latitude=None,
        phone=None,
        website_url=None
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (
            f"Nazwa: {self.name}\n"
            f"Typ: {self.brewery_type}\n"
            f"Adres: {self.street or 'Brak danych'}, {self.city or 'Brak danych'}, {self.state or 'Brak danych'}, {self.postal_code or 'Brak danych'}, {self.country or 'Brak danych'}\n"
            f"Współrzędne: ({self.latitude or 'Brak danych'}, {self.longitude or 'Brak danych'})\n"
            f"Telefon: {self.phone or 'Brak danych'}\n"
            f"Strona internetowa: {self.website_url or 'Brak danych'}\n"
        )


url = "https://api.openbrewerydb.org/v1/breweries"
response = requests.get(url, params={'per_page': 20})
breweries_data = response.json()

breweries = []

for data in breweries_data:
    brewery = Brewery(
        id=data.get("id"),
        name=data.get("name"),
        brewery_type=data.get("brewery_type"),
        street=data.get("street"),
        city=data.get("city"),
        state=data.get("state"),
        postal_code=data.get("postal_code"),
        country=data.get("country"),
        longitude=data.get("longitude"),
        latitude=data.get("latitude"),
        phone=data.get("phone"),
        website_url=data.get("website_url")
    )

    breweries.append(brewery)

for brewery in breweries:
    print(brewery)
