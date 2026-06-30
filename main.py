import random

def read_data(file):
    f = open(file)
    return f.readlines() 

# TODO: randomize so not in alphabetical order
def parse_data(data):
    country_dict = {}
    for row in data[1:]:
        split_row = row.split(',')
        country_dict[split_row[2]] = split_row[1]
    return country_dict

def edit_country_dict(country_dict):
    country_dict['Israel'] = 'Jerusalem'
    country_dict['Palestine'] = 'Jerusalem'
    country_dict['Ukraine'] = 'Kyiv'
    country_dict['Bolivia'] = 'Sucre'
    country_dict['Albania'] = 'Tirana'
    country_dict['Myanmar (Burma)'] = 'Naypyidaw'
    country_dict['South Africa'] = 'Pretoria'
    country_dict['Palau'] = 'Ngerulmud'
    country_dict['Kiribati'] = 'Tarawa'
    country_dict['Congo'] = 'Kinshasa'
    del country_dict['"Congo']
    del country_dict[' Sucre (official)"']
    del country_dict[' Bloemfontein']
    return country_dict

def get_country_test_count():
    print("How many countries would you like to test? \n Enter a number between 1 - 195 or 'all' ")
    count = input()
    while not (count == 'all' or (int(count) > 1 and int(count) < 195)):
        print("Invalid input")
        print("How many countries would you like to test? \n Enter a number between 1 - 195 or 'all' ")
        count = input()
    return 195 if count == 'all' else int(count)

def test_country_capitals(country_dict, country_count):
    countries_to_review = {}
    country_list = list(country_dict.keys())
    random.shuffle(country_list)
    for country in country_list[:country_count]:
        print(country)
        capital_guess = input()
        if capital_guess != country_dict[country]:
            print("Incorrect")
            countries_to_review[country] = country_dict[country]
    return countries_to_review


if __name__ == "__main__":
    # must run project from project folder
    data = read_data("all capital cities in the world.csv")
    country_dict = edit_country_dict(parse_data(data))
    print("country count ", len(country_dict))
    country_count = get_country_test_count()
    countries_to_review = test_country_capitals(country_dict, country_count)
    while (len(countries_to_review) != 0):
        print("Let's Review...Country capitals missed: ", len(countries_to_review))
        countries_to_review = test_country_capitals(countries_to_review, len(countries_to_review))
    if country_count == 195:
        print("Congratulations -- you know every country capital!")
    else:
        print("Congratulations -- you know " + str(country_count) + " country capitals!")


# IDEAS FOR CONTINUATION
# take user input for country count, or all (default)
# handle invalid input
# add optional hint functionality - after "Let's Review!" ask user if they would like a letter as a hint
# serve to browser

