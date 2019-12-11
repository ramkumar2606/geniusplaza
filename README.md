# geniusplaza
## Technologies Used

 1. Django REST Framework
 2. SQLITE
 
 ### Endpoints
 #### GET ALL RECIPES
GET  /recipes
 

    [{"id":1,"name":"tea","user_id":1},{"id":3,"name":"coffe","user_id":2},{"id":4,"name":"cookies","user_id":2}]

##### GET ALL RECIPES BY USER
GET /recipes?user_id=2

    {"id":3,"name":"coffe","user_id":2},{"id":4,"name":"cookies","user_id":2}]
#### CREATE NEW RECIPE
POST /recipes
REQUEST:

    {
            "name": "cake",
            "user_id": 2
     }
RESPONSE:

    {"id":5,"name":"cake","user_id":2}


#### EDIT RECIPE
PUT /recipes/5
REQUEST:

    {
            "name": "pizza",
            "user_id": 2
     }
RESPONSE:

    {"id":5}
#### DELETE RECIPE
DELETE /recipes/5

RESPONSE:

    {"id":5}

### FUTURE ENHANCEMENTS

 1. CRUD operations for ingredients and steps
 2. Include ingredients and steps in JSON response of Recipes list
