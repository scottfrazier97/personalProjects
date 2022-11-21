import requests 
import pprint

headers = {
    "Accept": "*/*",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjVlOGU4Y2EzLWRmYjktNDU5Ni04MzVlLTgyOTMyODFiNTlhMCIsImlhdCI6MTY2Njc5NzY0Miwic3ViIjoiZGV2ZWxvcGVyL2JlNDJlMjBlLWU0OTYtMjk5MC04NTMzLWU4OTc2MGZhZjBjNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjQ3LjE4NS4yMDguMTQiXSwidHlwZSI6ImNsaWVudCJ9XX0.hK7C2CkyYH7mkW7gNzEblIAdIdvh8dAHTn-_ArhQrBjWr13guFFdGfdyomI-aF4Tj44G306QXfFV-X38ApChZQ"
}

def get_user():
    #return user profile information
    response = requests.get('https://api.clashofclans.com/v1/players/%23LLY09LLU', headers=headers)
    user_json = response.json()
    print(pprint.pprint(user_json))

get_user()