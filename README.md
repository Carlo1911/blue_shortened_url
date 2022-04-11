# Project Shortener

## CORE REQUIREMENTS

• We must be able to put a URL into the home page and get back a URL of
the shortest possible length.
• We must be redirected to the full URL when we enter the short URL (ex:
http://localhost:3000/a => https://google.com)

• There should be a page that shows the top 100 most frequently
accessed URLs.

• There must be a background job that crawls the URL being shortened, pulls the <title> from the website and stores it.
• Display the title with the URL on the top 100 board.
• There must be a README that explains how to setup the application and the algorithm used for generating the URL short code.
### NICE TO HAVE:
Write a bot to populate your DB, and include it in the source code
Write Unit or Integration Tests


## Starting 🚀
_Follow this instructions to start building a copy of this project._

### Tech requirements 📋

-   Docker 19.03^
-   Docker Compose 1.25^
***

## Installation 🔧

1. Clone the repository
    ```
    git clone ...
    ```

2. Create a copy of .envs
    ```
    cp -r .envs-example .envs
    ```

3. Create the images
    ```
    make build
    ```
4. Up the containers
    ```
    make up
    ```
5. Migrate
    ```
    make migrate
    ```
6. Create super user
    ```
    make superuser
    ```
***

## Misc
Generate migrations from changes in models
    ```
    make migrations
    ```

Generating short url using a random choices from letters and digits with a length of 15. Other possible option was using uuid.

## Utils 💻
- Api Docs: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)
***

## References 📖
- Project based on the book: Django 3 Web Development Cookbook Fourth Edition ([Enlace al libro](https://www.packtpub.com/product/django-3-web-development-cookbook-fourth-edition/9781838987428))

***
⌨️ con ❤️ por Carlo1911 🧑‍💻

---