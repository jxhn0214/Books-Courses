from city_country_module import structure_city_country

def test_city_country():
    """do addresses like San Francisco, United States Of America work"""

    formatted_address = structure_city_country('san francisco', 'united states of america')
    assert formatted_address == "San Francisco, United States Of America"
