# Shortened URL

## prerequisites
* docker
* docker-compose
* python

## run the project
As we have a Makefile you can run the project with the following command:

Build the project
```bash
make build
```

Run the project
```bash
make up
```

Create migrations (The project has to be running)
```bash
make migrations
```

Apply migrations (The project has to be running)
```bash
make migrate
```