import requests

keyPierre = "k_w2ky8vcq"
keyMaxime = "k_byr9fs6f"

def get_byId(id):
	url = f"http://www.omdbapi.com/?i={id}&apikey=29dba3b9"
	return requests.get(url).text

def get_byId2(id):
	url = f"https://imdb-api.com/fr/API/Title/{keyMaxime}/{id}/Posters"
	return requests.get(url).text

