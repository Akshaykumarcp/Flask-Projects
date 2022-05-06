```
PS D:\courses\udemy\Docker Masterclass for Machine Learning and Data Science\Test-App-Docker\Test App Docker> docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED         STATUS         PORTS                    NAMES
53d98310f07b   flaskimage   "/bin/sh -c 'python …"   3 minutes ago   Up 3 minutes   0.0.0.0:5000->5000/tcp   testcontainer
```

```
PS D:\courses\udemy\Docker Masterclass for Machine Learning and Data Science\Test-App-Docker\Test App Docker> docker logs --help

Usage:  docker logs [OPTIONS] CONTAINER

Fetch the logs of a container

Options:
      --details        Show extra details provided to logs
  -f, --follow         Follow log output
      --since string   Show logs since timestamp (e.g.
                       2013-01-02T13:23:37Z) or relative (e.g. 42m for 42
                       minutes)
  -n, --tail string    Number of lines to show from the end of the logs
                       (default "all")
  -t, --timestamps     Show timestamps
      --until string   Show logs before a timestamp (e.g.
                       2013-01-02T13:23:37Z) or relative (e.g. 42m for 42
                       minutes)
```

```
docker login
```

```
PS D:\courses\udemy\Docker Masterclass for Machine Learning and Data Science\Test-App-Docker\Test App Docker> docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
flaskimage   latest    3726ecc47304   12 minutes ago   89.6MB
```

```
PS D:\courses\udemy\Docker Masterclass for Machine Learning and Data Science\Test-App-Docker\Test App Docker> docker pull couchbase
Using default tag: latest
latest: Pulling from library/couchbase
d5fd17ec1767: Pull complete
76937b0923f6: Pull complete
586c5f707c3a: Pull complete
c1a300a82511: Pull complete
ccf9265b3d00: Pull complete
c9647698da40: Pull complete
daeef37ef3ec: Pull complete
b940aaedabcd: Pull complete
a44f857e3b76: Pull complete
0a692084456f: Pull complete
Digest: sha256:1f64978d304983ad56f01633f54b125b578027c78081dba1125ffa3dd4827753
Status: Downloaded newer image for couchbase:latest
docker.io/library/couchbase:latest
```

```
PS D:\courses\udemy\Docker Masterclass for Machine Learning and Data Science\Test-App-Docker\Test App Docker> docker run couchbase:latest
Starting Couchbase Server -- Web UI available at http://<ip>:8091
and logs available in /opt/couchbase/var/lib/couchbase/logs
```