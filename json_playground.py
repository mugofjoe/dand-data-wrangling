"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""

#%%

import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"


# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {"simple": {},
              "atr": {"inc": "aliases+tags+ratings"},
              "aliases": {"inc": "aliases"},
              "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    """
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    """
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    """
    After we get our output, we can use this function to format it to be more
    readable.
    """
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


#%%

def main():
    """
    Below is an example investigation to help you get started in your
    exploration. Modify the function calls and indexing below to answer the
    questions on the next quiz.

    HINT: Note how the output we get from the site is a multi-level JSON
    document, so try making print statements to step through the structure one
    level at a time or copy the output to a separate output file. Experimenting
    and iteration will be key to understand the structure of the data!
    """

    # Query for information in the database about bands named Nirvana
    # results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid")
    # # pretty_print(results)

    # # Isolate information from the 4th band returned (index 3)
    # print "\nARTIST:"
    # pretty_print(results["artists"][2])

    # # Query for releases from that band using the artist_id
    # artist_id = results["artists"][2]["id"]
    # artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    # releases = artist_data["releases"]

    # Print information about releases from the selected band
    # print "\nONE RELEASE:"
    # pretty_print(releases[5], indent=2)

    # release_titles = [r["title"] for r in releases]
    # # print("TYPE OF release_titles: {}".format(type(release_titles)))
    # print "\nALL TITLES:"
    # for t in release_titles:
    #     print t

    # atr_data = query_site(ARTIST_URL, query_type["atr"], artist_id)
    # pretty_print(atr_data)

    """
    How many bands named First Aid Kit?
    """
    # Query for information in the database about bands named First Aid Kit
    # results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")

    # name_count = 0
    # for item in results["artists"]:
    #     # pretty_print(item["name"])
    #     if item["name"] == "First Aid Kit":
    #         name_count += 1

    # print("Number of First Aid Kit: {}".format(name_count))
    # Answer: 2

    """
    What is the begin-area name for Queen?
    """

    # # Query for information in the database about bands named Queen
    # results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    # # pretty_print(results)

    # # Isolate information from the 3rd band returned (index 2)
    # print "\nARTIST:"
    # pretty_print(results["artists"][2])

    # # Query for releases from that band using the artist_id
    # artist_id = results["artists"][2]["id"]
    # artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    # print(artist_data["begin_area"]["name"])
    # Answer: London

    """
    What is the Spanish alias for Beatles?
    """

    # # Query for information in the database about bands named Queen
    # results = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
    # # pretty_print(results)

    # # Isolate information from the 3rd band returned (index 2)
    # print "\nARTIST:"
    # pretty_print(results["artists"][7])

    # # # Query for releases from that band using the artist_id
    # artist_id = results["artists"][7]["id"]
    # beatles_data = query_site(ARTIST_URL, query_type["aliases"], artist_id)
    # beatles_aliases = beatles_data["aliases"]
    # alias_id = 0
    # for a in beatles_aliases:
    #     if a["locale"] == "es":
    #         break
    #     else:
    #         alias_id += 1

    # print(beatles_aliases[alias_id]['name'])
    # # Answer: Los Beatles

    """
    Nirvana Disambiguation?
    """

    # Query for information in the database about band named Nirvana
    # results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    # # pretty_print(results)

    # # Isolate information from the 5th band returned (index 4)
    # print "\nARTIST:"
    # pretty_print(results["artists"][4])

    # # Isolate information from the 4th band returned (index 3)
    # print "\nARTIST:"
    # pretty_print(results["artists"][4])

    # # Query for releases from that band using the artist_id
    # artist_id = results["artists"][4]["id"]
    # artist_data = query_site(ARTIST_URL, query_type["simple"], artist_id)
    # disambiguation = artist_data["disambiguation"]

    # # Print information about releases from the selected band
    # print "\nDisambiguation:"
    # print(disambiguation)
    # Answer: 90s US grunge band

    """
    When was One Direction formed?
    """

    # Query for information in the database about band named Nirvana
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    # pretty_print(results)

    # Isolate information from the 1st band returned (index 0)
    print "\nARTIST:"
    pretty_print(results["artists"][0])

    # Query for releases from that band using the artist_id
    artist_id = results["artists"][0]["id"]
    artist_data = query_site(ARTIST_URL, query_type["simple"], artist_id)
    begin_date = artist_data["life-span"]["begin"]
    print("One Direction begin date: {}".format(begin_date))
    # Answer: 2010-07


if __name__ == '__main__':
    main()


# From https://jefflirion.github.io/udacity/Data_Wrangling_with_MongoDB/Lesson1.html

# import pprint
# pp = pprint.PrettyPrinter(indent=2)

# # How many bands are there named "First Aid Kit"?
# results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
# names = [artist['name'] for artist in results['artists'] if artist['name']=='First Aid Kit']
# print '\n***There are', len(names), 'bands named "First Aid Kit"\n'

# # begin-area name for Queen?
# results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
# queen = [artist for artist in results['artists'] if artist['name']=='Queen']
# print '\n***The begin-area name for Queen is', queen[0]['begin-area']['name'],'\n'

# # Spanish alias for the Beatles?
# results = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
# beatles = [artist for artist in results['artists'] if (artist['name']=='Beatles' or artist['name']=='The Beatles')]
# #pp.pprint(beatles)
# #print beatles[0]['aliases']
# pp.pprint([alias['name'] for alias in beatles[0]['aliases']])
# print '\n'

# # Nirvana disambiguation
# results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
# nirvana = [artist for artist in results['artists'] if artist['name']=='Nirvana']
# print '\n***The disambiguation for Nirvana is:',nirvana[0]['disambiguation'],'\n'

# # when was one direction formed?
# results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
# onedirection = [artist for artist in results['artists'] if artist['name']=='One Direction']
# print '\n***One Direction began', onedirection[0]['life-span']['begin']
