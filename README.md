# MovieHub Test Task

## Installation

1. Clone the repository:

```sh
git clone https://github.com/Kleishmidt/test_MovieHub.git
```

2. Make a copy of the `.env.example`,`.env.db.example`  and rename it to `.env`, `.env.db` accordingly.
   Modify the values in the files according to your specific environment and requirements.

3. Build the docker containers:

```sh
   docker-compose up --build --remove-orphans
```

or

```sh
   make build_containers
```


## Swagger Endpoint

```sh
http://localhost:8000/swagger/
```