# Quick reference

-    **Maintained by**:  
     [georchestra.org](https://www.georchestra.org/)

-    **Where to get help**:  
     the [geOrchestra Github repo](https://github.com/georchestra/georchestra), [IRC chat](https://matrix.to/#/#georchestra:osgeo.org), Stack Overflow

# Featured tags

- `latest`

# Quick reference

-	**Where to file issues**:  
     [https://github.com/georchestra/georchestra/issues](https://github.com/georchestra/e2e-tests/issues)

-	**Supported architectures**:   
     [`amd64`](https://hub.docker.com/r/amd64/docker/)

-	**Source of this description**:  
     [docs repo's directory](https://github.com/georchestra/e2e-tests/blob/main/DOCKER_HUB.md)

# What is `georchestra/e2e-tests` ?

This project contains automated tests for the geOrchestra web applications using Playwright and pytest.

A [complete description](https://github.com/georchestra/e2e-tests/blob/main/console/README.md) is available on github .

# How to use base image and run specific tests

Create a folder where you put your specific tests and create a Dockerfile with the following content:

```Dockerfile
FROM georchestra/e2e-tests:latest

COPY mytests /app/tests/mytests
```

## Where is it built

This image is built using Dockerfile in [docs repo's directory](https://github.com/georchestra/e2e-tests/blob/main/Dockerfile)

# License

View [license information](https://www.georchestra.org/software.html) for the software contained in this image.

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

[//]: # (Some additional license information which was able to be auto-detected might be found in [the `repo-info` repository's georchestra/ directory]&#40;&#41;.)

As for any docker image, it is the user's responsibility to ensure that usages of this image comply with any relevant licenses for all software contained within.