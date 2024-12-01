import requests
import tasks.zad_1 as zad_1
import tasks.zad_2 as zad_2
import tasks.zad_3 as zad_3
import tasks.zad_4 as zad_4
import tasks.zad_5 as zad_5
import tasks.zad_6 as zad_6
import tasks.zad_7 as zad_7


def run_tasks():
    #zad 1
    name = 'Mark'
    surname = 'Oak'
    
    print(zad_1.full_name(name=name, surname=surname))

    #zad 2
    zad_2.multiplication(2,3)

    #zad 3
    if (zad_3.is_even(23)):
        print('Liczba jest parzysta')
    else:
        print('Liczba jest nieparzysta')

    #zad 4
    zad_4.comparision(1,2,3)

    #zad 5
    print(zad_5.list_contains([1, 2, 3, 8], 7))

    #zad 6
    zad_6.join_lists([1, 2, 3, 8], [9, 9, 9, 9])

    #zad 7
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url, params={'per_page': 20})
    breweries_data = response.json()    

    breweries = []  

    for data in breweries_data:
        brewery = zad_7.Brewery(
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
