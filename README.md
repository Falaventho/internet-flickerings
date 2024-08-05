# Internet Flickerings

## Project Description

Internet Flickerings (INTFLX) is a Netflix clone build with Django, PostgreSQL, Nginx, and Docker. This project is both the pathway to and product of my understanding of these technologies and their associated languages.

## Use INTFLX

The current version of INTFLX is pre-deployment, but the project can be self-hosted by following these steps:

1. Clone the repository:

```bash
git clone https://gitlab.com/Falaventho/internet-flickerings.git
cd internet-flickerings
```

2. Ensure you have [Docker](https://docs.docker.com/get-docker/) (Desktop or Engine) installed on your machine.
3. Build and run the Docker containers:

```bash
docker compose up
```

4. Access the application in your web browser at 'http://127.0.0.1'

<br>

❗ Note: The container for nginx binds to port 80. If you have another service bound to port 80, nginx will not bind appropriately and will be inaccessible. To resolve this, either stop all other services bound to port 80 before running the command in step 3 or change the first proxy port in [docker-compose.yml](docker-compose.yml) &nbsp;(the 80 in '- 80:8000') to another free port. If you choose to change the ports, the above link to the web application will require an ammended address with the port number appended in the form 'http://127.0.0.1:\<port>'.

For example, if changing the exposed port from 80 to 5947, (making the docker-compose file read '- 5947:8000' under proxy->ports) the web application would be accessed at 'http://127.0.0.1:5947'

## Project Roadmap

For a detailed developer roadmap and information concerning features, please see the [ROADMAP](ROADMAP.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
