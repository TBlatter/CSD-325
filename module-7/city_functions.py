# city_functions.py
#tysonblatter4/20 7.2

def city_country(city, country, population=None, language=None):
    """Returns a string like 'City, Country', optionally with population and language."""
    if population and language:
        return f"{city}, {country} - population {population}, language {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"

# Call with City, Country
print(city_country("Orlando", "USA"))

# Call with City, Country, Population
print(city_country("Paris", "France", 2148327))

# Call with City, Country, Population, Language
print(city_country("Tokyo", "Japan", 13929286, "Japanese"))
