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

# Regarding this project

Ok so I feel like a have a plan on what I can do with this project so at this point of time I think that I will be making a CLI version of all this.

Features I might want to add in that would be: 

- Regarding User
    - Adding a user 
    - Updating details of that user
    - Deleting a user
- Regarding Graphs 
    - Creation and Cofiguring that graph
    - Updating certain parameters of your graph
    - Like Timezone and others
- Regarding Pixels
    - Creation and Deletion of Pixels
- **Miscelaneous** yet useful
    - Having some sort of menu which can be triggered at any point of time(we'll see about time stuff)
    - Actually creating .env and .gitignore file for user
    - Might wanna create a database which kept note of what's happening.
    - Having some sort of navigation functionality accross all my present graphs for the selected user.
    - Also having profile system so that we can see which user is actually doing stuff.

I feel this might be an actual project, which I might be able to put somewhere. And this will be something which has my personel touch
