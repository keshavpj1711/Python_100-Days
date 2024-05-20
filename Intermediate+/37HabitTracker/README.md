# HTTP Requests

Uptill now we have only used GET HTTP Requests. 
But other than this we have some requests as well:

- GET - requests.get()
    - getting some data from external service
- POST - requests.post()
    - posting some stuff on external service eg: sheets, twitter
- PUT - requests.put()
    - updating some existing piece of data on above mentioned servies 
- DELETE - requests.delete()
    - does as the name suggests

Huh! well the syntax didn't change that much 

# Authentication using HTTP Header

Did this part in the code and it's more secure than using your key.
Reason when directly passing the key someone who is monitoring your
network connection might steal your key. 
So in order to protect your key we use this method.
