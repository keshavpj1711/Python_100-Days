# API Authentication 

## The Need for Auth

Now many a times you might require data that is not so widely accessible or say,
you are using some sort of API Service which requires you to have some kind of subscription,
in that case authenicating yourself to access the data makes sense.

To Authenticate yourself you must need some sort of key i.e. when role of API Key comes.

API Keys are basically a way to tell the API servers that this is you who are trying to access the API Key.

# Environment Variables and Hiding API Keys 

We usually store secret credentials and other application configurations in a file that is not a part of 
the application source code. A popular way to do this is by .env file creation or creating seperate environment variables.

Further read about securing your credentials and creating .env file [here](https://www.baeldung.com/linux/environment-variables-file)