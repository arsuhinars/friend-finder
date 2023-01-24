# Friend-finder
Service for finding new friends! It has features like: searching and rating
others profiles, chatting with people who liked you too and chat with random
users.

> There will be screenshots of ready UI

## Features description

### Profile creation
During registration in app user gives only their name. After registration and
confirming E-Mail they fill profile. In profile the following data are given:
- Birth date (only for age)
- Search place
- Where to search (only nearby or everywhere)
- Gender
- Who to find (males or females)
- Photos (minimum 1, maximum 4)
- Interests (from given list)
- Brifly description about yourself
- And more detailed description

Further user may look at their profile preview how it will be shown to others.

To start using application it is needed to activate profile. User may delay it,
but main functionality will be unavailable and profile will not be shown in
searching.

If user during some time isn't active their profile will be deactivated.

### Profiles searching
It is first and main tab in app. Here service show other profiles of random
users according with user's profile settings. They may like it or skip. Besides
there is another tab with a list of users who liked profile. It is also possible
to rate them.

### Profiles selection algorithm
Service takes some number of random profiles according to user's profile settings.
Then that profiles are mixed and saved in cache on a certain amount of time.
After it on request profiles are given to client successively.

### Communication
If users liked each other's profiles chat between them will be automatically
opened. If in a day they stop talk with each other service will delete their
chat. Besides it is possible to stop conversation that will also delete chat.

### Random chat
There is a special chat called "Random chat". There user may talk with other 
users anonymously. Users in this chat are selected with profile settings. Time
after what chat will be deleted is shorter than in ordinary chat. After some
time users can share their profile.

## Technology stack  
* __Backend__: Python, FastAPI, Redis, Postgres, Docker
* __Frontend__: Vite, Vue.js, Vuetify, Pinia, Vue Router

## Specification
OpenAPI schema is available [here](api_schema.yaml).

## Installing and running
> TODO
