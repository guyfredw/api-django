# Bark Social Application

Bark is a social media application which allows users to write posts on any topics they would like, while also being able to see the posts of others. Within those posts users have the possibility of writing comments on the posts to express their opinions or provide feedback.
The purpose of this app is to try and incorporate the different aspects of a social media application while being able to learn the necessities of a social media app and how to build them.

## Planning Journey

The development of the bark application started on the idea of creating an app that could serve multiple purposes and that people would be able to use to their own liking. Based on that idea, I decided that creating a social media application with the fundamental functionalities would help me build my skills both in the back end and the front end of the app.
It is easy to get lost on deciding what kind of functionalities someone wants to integrate into their application, therefore it was necessary to decide what the key ones were and then to build upon them. The two key functionalities that would be the basis of the application were posts and comments.
To avoid any particular errors that could significantly impact the application I used Github's version control system, and I built the front-end and the back-end in a series of versions.
Whenever an Issue occured I would take that opportunity to learn about the possibilities of how I could resolve by using different resources.
creating and learning about social media applications in order to recreate one.

## Important Links

- [Front-end repository](https://github.com/guyfredw/bark-react)
- [Deployed Client](https://guyfredw.github.io/bark-react/)
- [Deployed API](https://bark-api-project.herokuapp.com)

### Technologies Used

- Python
- Django
- Django rest_framework
- Git
- GitHub

### Future Features or Unsolved Problems

- Styling
- Likes
- Tags
- Follower system
- Notification system

## Entity Relationship Diagram (ERD)

![BarkReachGoals](https://media.git.generalassemb.ly/user/31388/files/4ce29080-4114-11eb-927a-ddf1fdc19f43)


### Catalog of routes

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `sign-up/`             | `users#signup`    |
| POST   | `sign-in/`             | `users#signin`    |
| PATCH  | `change-pw/` | `users#changepw`  |
| DELETE | `sign-out/`        | `users#signout`   |
| GET    | `posts/`            | `posts#index`     |
| GET    | `posts/:pk`        | `posts#show`      |
| POST   | `posts`            | `posts#create`    |
| PATCH  | `posts/:pk`        |  `posts#update`   |
| DELETE | `posts/:pk`        | `posts#delete`    |
| GET   |  `all-posts/` | `posts#index`   |
| GET   |  `show-post/:pk` | `posts#show`  |
| GET    | `comments/`          |  `comments#index`  |
| GET    | `comments/:pk`      | `comments#show`    |
| POST   |  `comments/`         | `comments#create`  |

### Set up instructions

1. Fork and clone this repository
2. When inside the repository run `pipenv shell` to enter your virtual environment
3. Run `pipenv install` to install the dependencies
4. Run `psql -U postgres -f settings.sql` to create a psql database for your project
5. Run `python3 manage.py migrate` to run migration files to migrate changes to db
6. Run `python3 manage.py runserver` to run the server
