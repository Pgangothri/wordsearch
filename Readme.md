# Word Search using Djanog Rest Framework

This project is a Django-based web application that allows users to manage paragraphs of text and perform interactive searches within them. Users can register, log in, and create/search paragraphs. The application uses Docker for easy deployment and scalability.


## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker Engine: [Install Docker](https://docs.docker.com/get-docker/)

## Getting Started

To run this project locally using Docker, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Pgangothri/wordsearch.git
   cd your-project
2. Build Docker Images:
   ```bash
   docker-compose build
3. Start the Docker container
   ```bash
   docker-compose up
5. The database migrations will automatically done by the docker itself.
6. Now we have to create superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
7. Now it will ask for the username, name and password:
   ```bash
   PS C:\projects\django\textsearch> docker-compose exec web python manage.py createsuperuser
   Email: admin@gmail.com
   Name: admin
   Password: ******
   Password (again):*****
]
8. now we can log in to the admin panel by using the end point  [http://localhost:8000/admin/](url):
9. The application should now be accessible at http://localhost:8000/.:
10. To stop the containers use:
   ```bash
   docker-compose down
# API end points
## User Registration

**Endpoint:** `/register/`

**Methods:** 
- `POST`: Register a new user.

**Authentication Required:** No

**Sample Request:**
  ```json
  {
    
    "email": "pgangothriroyal@gmail.com",
    "name": "Gangothri",
    "dob": "2003-08-13",
    "password": "Gangothri"
  }
 ```
**Sample Response:** 
   ```json
  {
  "id": 1,
  "email": "pgangothri@gmail.com",
  "name": "gangothri",
  "dob": "2003-08-13",
  "created_at": "2024-05-04T20:00:56.239289",
  "modified_at": "2024-05-04T20:00:56.239289"
}
   ```

## User Login

**Endpoint:** `login/`

**Methods:** 
- `POST`: Log in with existing credentials.

**Authentication Required:** No

**Sample Request:**
```json
{
  "username": "pgangothri@gmail.com",
  "password": "Gangothri"
}
```
**Sample Response:**
```json
{
  "token": "your-access-token",
}
```

## Paragraph List and Creation

**Endpoint:** `/paragraphs/`

**Methods:** 
- `POST`: Create new paragraphs.

**Authentication Required:** Yes
```headers
authorizaiton : Token 536a2a66ddf451cf36a24278a2f53a6b80e921f9
```

**Sample Request (POST):**
```json
{
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam atlectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque.\n\nMaecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id."
}
```
**Sample Response (GET):**
```json
[
   {"id":1,"content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam atlectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque."},

   {"id":2,"content":"Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id."}]
```

## Paragraph Retrieve, Update, and Delete

**Endpoint:** `/paragraphs/<int:pk>/`
example `http://localhost:8000/paragraphs/1`

**Methods:** 
- `GET`: Retrieve a specific paragraph.

**Authentication Required:** Yes

**Sample Request (GET):**
*Headers:* 

```headers
authorizaiton : Token 536a2a66ddf451cf36a24278a2f53a6b80e921f9
```

**Sample Response (GET):**
```json
{
  "id": 1,
  "content": "paragraph"
}
```
**Methods:** 
- `PUT`: Update a specific paragraph.

**Authentication Required:** Yes

**Sample Request (PUT):**
```json
{
  "content": "paragraph"
}
```
**Sample Response (PUT):**
```json
{
  "id": 1,
  "content": "updated paragraph"
}
```
**Methods:** 
- `DELETE`: Update a specific paragraph.

**Authentication Required:** Yes

**Sample Request (PUT):**
```json
{
  "message": "Paragraph deleted successfully."
}
```

## Search Paragraphs

**Endpoint:** `/search/<str:word>`

**Methods:** 
- `GET`: Search for paragraphs containing a specific word.

**Authentication Required:** Yes

**Sample Request (GET):**
*Headers:* 
```headers
authorizaiton : Token 536a2a66ddf451cf36a24278a2f53a6b80e921f9
```
**Sample Request (PUT):**
```json
{
  "results": [
    {
      "id": 1,
      "content": "Highlighted paragraph with <strong>word</strong>."
    },
    {
      "id": 2,
      "content": "Another paragraph containing the <strong>word</strong>."
    }
    // Additional paragraphs may be included in the response
  ]
}
```



### Reporting Issues

If you encounter any issues or have suggestions for improvements, please create an issue in the [issue tracker](https://github.com/mrsaikumar-7/text-search/issues).

# Happy Coding 😊















   
