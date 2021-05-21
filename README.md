# Github API challenge named API!

## Overview

This is a simple web app written in Python 3.7+, and uses Flask framework (Python web framework).

### Features:

- Listens for organization events to know when a repository has been created.
- When a repository is created under the organization, triggers an automated process to protect the master branch of the repository using a minimum number of pull reviews.
- Then notify your Github user account with an @mention using Github issue within the repository, highlights the details of what protection was added to the branch.

### Requirements

- [Download](https://git-scm.com/) and install Git 2.x on your machine
- Python 3.7+ installed in your machine
- A code editor, for example [Atom](https://atom.io)
- [A Github account](https://github.com)
- An Github Organisation. _you can create one from your free Github account_
- [A free Ngrok account](https://ngrok.com/)

### Getting started

It's super simple web application, doesn't use docker or anything like that, the idea is you can host this Flask app anywhere with not a specific virtualization platform.

### Setup

1. Fork and clone this repository to your local machine.
2. Open the terminal and start ngrok server, _this will be used to create a tunnel between your local machine and a webhook from Github._

```bash
./ngrok http 8080
```

1. Once you have your ngrok tunnel working you will need to start up the **server.py**, which is the main component here.

On your terminal window, type the following command.

```bash
export FLASK_APP=server.py
pyton3 -m flask run
```

### Configuration

TBD

### Contributing

Long-term discussion and bug reports are limited only during the interview with Github. Code reviews are possible, as long are done via Github Pull requests.

#### License

This project is licensed under the Apache 2.0 License.
