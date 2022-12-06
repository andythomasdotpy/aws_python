import boto3
import json
from pprint import pprint
from decimal import Decimal


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movie')


with open('movie_data.json') as file:
    movies = json.load(file, parse_float=Decimal)

for movie in movies:
    title = movie['title']
    year = int(movie['year'])
    print(title, year)
    response = table.put_item(Item=movie)

# import boto3
# import json
# from decimal import Decimal
# from pprint import pprint
#
#
#
# def load_movie(movies, dynamodb=None):
#     if not dynamodb:
#         dynamodb = boto3.resource('dynamodb')
#
#     table = dynamodb.Table('Movies')
#
#     for movie in movies:
#         year = int(movie['year'])
#         title = movie['title']
#         print("Adding movie : ", year, title)
#         x = input(movie)
#         # table.put_item(Item=movie)
#
#
#
#
# if __name__=="__main__":
#     with open('movie_data.json') as json_file:
#         movie_list = json.load(json_file, parse_float=Decimal)
#
#         pprint(movie_list)
#
#
#     load_movie(movie_list)