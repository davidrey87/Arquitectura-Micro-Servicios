# Micro servicios
En esta carpeta se definen los micro servicios utilizados en el capítulo 5. La especificación de cada micro servicio se realizó utilizando blueprint de Apiary.
La especificación de cada micro servicio es la siguiente:

+----------------------------------------------------------------------------------------+

## Information Microservice
+----------------------------------------------------------------------------------------+  
FORMAT: 1A  
HOST: https://uaz.cloud.tyk.io/content

# Information API

## Information Microservice [/api/v1/information{?t}]

+ Parameters
    + t - Corresponde al título de la película o serie de Netflix.

### Get Information [GET]

+ Response 200 (application/json)

        { 
            "Title": "Some text",
            "Year": "Some text", 
            "Rated": "Some text",
            "Released": "Some text",
            "Runtime": "Some text",
            "Genre": "Some text",
            "Director": "Some text",
            "Writer": "Some text",
            "Actors": "Some text",
            "Plot": "Some text",
            "Language": "Some text",
            "Country": "Some text",
            "Awards": "Some text.",
            "Poster": "Some text",
            "Metascore": "Some text",
            "imdbRating": "Some text",
            "imdbVotes": "Some text",
            "imdbID": "Some text",
            "Type": "Some text",
            "totalSeasons": "Some text",
            "Response": "Some text"
        }
+----------------------------------------------------------------------------------------+ 