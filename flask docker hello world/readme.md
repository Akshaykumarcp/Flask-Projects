### 1. Build docker image

```
PS D:\courses\udemy\Docker Masterclass for Machine Learning and Data Science\Test-App-Docker\Test App Docker> docker build -t flaskimage .
[+] Building 12.0s (9/9) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                              0.1s
 => => transferring dockerfile: 303B                                                                                                                                              0.0s 
 => [internal] load .dockerignore                                                                                                                                                 0.0s 
 => => transferring context: 2B                                                                                                                                                   0.0s 
 => [internal] load metadata for docker.io/library/python:alpine3.8                                                                                                               3.5s 
 => [internal] load build context                                                                                                                                                 0.0s
 => => transferring context: 6.95kB                                                                                                                                               0.0s 
 => [1/4] FROM docker.io/library/python:alpine3.8@sha256:3491d1abd29b3f87ca5cb1afd34bc696855a2403df1ff854da55cb6754af1ff8                                                         3.6s 
 => => resolve docker.io/library/python:alpine3.8@sha256:3491d1abd29b3f87ca5cb1afd34bc696855a2403df1ff854da55cb6754af1ff8                                                         0.0s
 => => sha256:f11f279751de52541dee36f349656c40cd4ed60faf8baeb9cd56c88e47dbf74f 6.13kB / 6.13kB                                                                                    0.0s 
 => => sha256:c87736221ed0bcaa60b8e92a19bec2284899ef89226f2a07968677cf59e637a4 2.21MB / 2.21MB                                                                                    0.5s 
 => => sha256:c3f51b0d0765f7359fcc1b8d67887b1461c51dfb04b68ad54676a592af48cfdc 309.13kB / 309.13kB                                                                                0.6s 
 => => sha256:a65abebf548020f86dedbaeebd52cabe9c517767097a538b2501f9b7e8b185f5 24.67MB / 24.67MB                                                                                  2.0s 
 => => sha256:3491d1abd29b3f87ca5cb1afd34bc696855a2403df1ff854da55cb6754af1ff8 1.42kB / 1.42kB                                                                                    0.0s
 => => sha256:11bdf108946825111860110128a739374143e9d9937300d47155ae541f291a0d 1.37kB / 1.37kB                                                                                    0.0s 
 => => extracting sha256:c87736221ed0bcaa60b8e92a19bec2284899ef89226f2a07968677cf59e637a4                                                                                         0.2s 
 => => sha256:6628a73c2c8584cad0284cc99cd31d3643520557539f03f360912436cd59ab33 231B / 231B                                                                                        1.1s 
 => => sha256:b49d22f17d2f47ff079f657c80e3249f956dfa0ada4d88806dac1d23b82ebcb0 1.82MB / 1.82MB                                                                                    1.3s 
 => => extracting sha256:c3f51b0d0765f7359fcc1b8d67887b1461c51dfb04b68ad54676a592af48cfdc                                                                                         0.1s 
 => => extracting sha256:a65abebf548020f86dedbaeebd52cabe9c517767097a538b2501f9b7e8b185f5                                                                                         1.2s 
 => => extracting sha256:6628a73c2c8584cad0284cc99cd31d3643520557539f03f360912436cd59ab33                                                                                         0.0s 
 => => extracting sha256:b49d22f17d2f47ff079f657c80e3249f956dfa0ada4d88806dac1d23b82ebcb0                                                                                         0.2s 
 => [2/4] COPY . /app                                                                                                                                                             0.3s 
 => [3/4] WORKDIR /app                                                                                                                                                            0.0s 
 => [4/4] RUN pip install -r requirements.txt                                                                                                                                     4.4s 
 => exporting to image                                                                                                                                                            0.1s 
 => => exporting layers                                                                                                                                                           0.1s 
 => => writing image sha256:8ef8b539a03667f051707950898529bc5f5f8efd0a5be87a45ffcfc1c0fee74d                                                                                      0.0s 
 => => naming to docker.io/library/flaskimage                                                                                                                                     0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```

### 2. list images

```
PS D:\courses\udemy\Docker Masterclass for Machine Learning and Data Science\Test-App-Docker\Test App Docker> docker images --all
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
flaskimage   latest    8ef8b539a036   About a minute ago   89.5MB
```

### 3. Run image as container

```
PS D:\courses\udemy\Docker Masterclass for Machine Learning and Data Science\Test-App-Docker\Test App Docker> docker run --name testcontainer -p 5000:5000 flaskimage
 * Serving Flask app 'index' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 625-793-942
```

### 4. Access http://localhost:5000/