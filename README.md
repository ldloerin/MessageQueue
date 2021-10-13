# CI / CD test workflow

This repository includes a simple code routine including pytest. It's used to build a CI / CD pipeline. The code itself uses the configuration input from /Main/Input/config.json to build an email address. This repository contains a test routine to asser the created mail address with an expected value.

- use Main/Input/config.json to define first name, last name, name seperator and the domain
- run the code by launching python ./Main/main.py
- the resulst is a print return value of the created mail address
- the code also writes the mail address into a Docker file to echo the result

Use the test routine

- define name and folder of the main test code (which is topic of the unit test here) as an input in Test001/Input/config.json
- define the expected mail address in Test001/Input/config.json
- run Test001/test_001_build_mail_address.py by using pytest as test environment

The CI/CD pipeline will run a lint process with flake8 and execute the pytest routine, on every push of committed code onto GitHub. After merging a pull request into the main branch, the CI/CD process will create a Docker image and list all the Docker images. The process will log onto DockerHub and push the just created image.
