<div id='main'>

# Movie Maintenance (API Guide) 
A simple server-side application that accesses movies and actors data through the Movie Maintenance Web API.
Explore awesome web client created with Angular, [Here](https://github.com/Rohan3011/movie-maintenance).

</div>


## Getting Started
Backend is completely build with **django** and **django-rest-framework**. As of now,
it's using the default **sqlite3** as database.

### ER Diagram
![Movie_ER_Diagram](https://user-images.githubusercontent.com/76813454/164768169-160b6942-cc90-405d-9562-dfd199c04276.png)


### Prerequisites
As mentioned above django and DRF (virtual environment is recommended).

```sh
    pip install django djangorestframework
```

## Usage
All urls are suffixed to `<BASE URL>/api/` path and 
all routes (mentioned below) are public.

### Movies
 Paths related to `Movies`

| URL        |  Method  | Description  |
| ------------- |:-------------:| -----:       |
|`movies-list/` | **GET /**     |    Returns a list  of all the movies     |
| `movies/<id>` | **GET /**     |   Returns movie with given `id`     |

 Movies can also be *filtered* with respect to `property` using `ordering` query parameter.
example : 

```
<BASE URL>/api/movies-list?ordering=<property>
```


> Here, `property` can be any field of `Movies` model.

Prefix the `property` with `-` for descending order.
example : 
```
<BASE URL>/api/movies-list?ordering=-<property>
```

<br>

### Actors

Use this endpoints to retrieve data about `Actors`.

| URL        |  Method  | Description  |
| ------------- |:-------------:| -----:       |
| `actors-list/`|**GET /**      |      Returns a list  of all the actors.       |
| `actors/<id>` | **GET /**     |    Returns actor with given `id`.         |


<br>

### Casts

Use this endpoints to retrieve data about `Casts`.
Cast refers to the `Actor(s)` involved in a `Movie`.



| URL        |  Method      | Request  | Descripiton|
| ----------       |:--------:    |:-----:   | -------:   |
| `casts/movie/`   |**POST /**   |  {`'movie'` : <movie_id>  }        | Returns the cast of given movie.   |
| `casts/actor/`   | **POST /**        | {`'actor'` : <actor_id>}         | Returns the movies done by given actor. |

<br>


## Contact
Rohan Kamble - rohanopdev@gmail.com

Frontend Project Link: [https://github.com/Rohan3011/movie-maintenance](https://github.com/Rohan3011/movie-maintenance)

<br>

<p align="right">(<a href="#main">back to top</a>)</p>
