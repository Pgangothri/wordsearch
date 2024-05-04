Word Search using Djanog Rest Framework
This project is a Django-based web application that allows users to manage paragraphs of text and perform interactive searches within them. Users can register, log in, and create/search paragraphs. The application uses Docker for easy deployment and scalability.

Prerequisites
Before you begin, ensure you have met the following requirements:

Docker Engine: Install Docker
Getting Started
To run this project locally using Docker, follow these steps:

Clone the repository:
git clone https://github.com/mrsaikumar-7/text-search.git
cd your-project
Build Docker Images:
docker-compose build
Start the Docker containers:
docker-compose up
The database migrations will automatically done by the docker itself.
Now we have to create superuser:
docker-compose exec web python manage.py createsuperuser
Now it will ask for the username, name and password:
PS E:\codehonk\myproject> docker-compose exec web python manage.py createsuperuser
Email: admin@gmail.com
Name: admin
Password: ******
Password (again):*****
Creating superuser with password: demo@123
Creating admin  with password: demo@123
now we can log in to the admin panel by using the end point http://localhost:8000/admin/:
The application should now be accessible at http://localhost:8000/.:
To stop the containers use:
docker-compose down
# API end points
## User Registration

**Endpoint:** `/register`

**Methods:** 
- `POST`: Register a new user.

**Authentication Required:** No

**Sample Request:**
```json
{
 "email": "john.doe@example.com",
 "name": "John Doe",
 "dob": "1990-01-01",
 "password": "securepassword123"
 
}
Sample Response:

{
  "id": 1,
  "email": "pgangothri@gmail.com",
  "name": "gangothri",
  "dob": "2003-08-13",
  "createdAt": "2024-05-06T16:23:03Z",
  "modifiedAt": "2024-05-06T16:23:03Z",
}
User Login
Endpoint: '/login'

Methods:

POST: Log in with existing credentials.
Authentication Required: No

Sample Request:

{
  "username": "pgangothri@gmail.com",
  "password": "Gangothri"
}
Sample Response:

{
  "token": "your-access-token",

}
Paragraph List and Creation
Endpoint: /paragraphs/

Methods:

POST: Create new paragraphs.
Authentication Required: Yes

authorizaiton : Token 536a2a66ddf451cf36a24278a2f53a6b80e921f9
Sample Request (POST):

{
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam atlectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque.\n\nMaecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id."
}
Sample Response (GET):

[
   {"id":1,"content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam atlectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque."},

   {"id":2,"content":"Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id."}]
Paragraph Retrieve, Update, and Delete
Endpoint: /paragraphs/<int:pk>/ example http://localhost:8000/paragraphs/1

Methods:

GET: Retrieve a specific paragraph.
Authentication Required: Yes

Sample Request (GET): Headers:

authorizaiton : Token 536a2a66ddf451cf36a24278a2f53a6b80e92
Sample Response (GET):

{
  "id": 1,
  "content": "paragraph"
}
Methods:

PUT: Update a specific paragraph.
Authentication Required: Yes

Sample Request (PUT):

{
  "content": "paragraph"
}
Sample Response (PUT):

{
  "id": 1,
  "content": "updated paragraph"
}
Methods:

DELETE: Update a specific paragraph.
Authentication Required: Yes

Sample Request (PUT):

{
  "message": "Paragraph deleted successfully."
}
Search Paragraphs
Endpoint: /search/<str:word>

Methods:

GET: Search for paragraphs containing a specific word.
Authentication Required: Yes

Sample Request (GET): Headers:
                             
authorizaiton : Token 
Sample Request (PUT):

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