from city_country_module import structure_city_country

def test_city_country():
    """do addresses like San Francisco, United States Of America work"""

    formatted_address = structure_city_country('san francisco', 'united states of america')
    assert formatted_address == "San Francisco, United States Of America"

def test_city_country_pop():
    """do addresses like Tokyo, Japan - population size work?"""

    formatted_address = structure_city_country('tokyo', 'japan', '37,000,000')
    assert formatted_address == "Tokyo, Japan - Population 37,000,000"