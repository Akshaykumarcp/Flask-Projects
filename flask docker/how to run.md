### 1. Build the project

```
J:\VSCODE_WORKSPACE\flask docker>docker-compose build
Building web
[+] Building 42.5s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                       0.0s
 => => transferring dockerfile: 32B                                                        0.0s
 => [internal] load .dockerignore                                                          0.0s
 => => transferring context: 2B                                                            0.0s
 => [internal] load metadata for docker.io/library/python:3                                1.1s
 => [internal] load build context                                                          0.0s
 => => transferring context: 123B                                                          0.0s
 => [1/5] FROM docker.io/library/python:3@sha256:db428075304d53783f6c7bdf075a47597464b79  26.1s
 => => resolve docker.io/library/python:3@sha256:db428075304d53783f6c7bdf075a47597464b79f  0.0s 
 => => sha256:dff8c1e4c3a609e87c05f1e08399332cf2dfb2b41d9bc91e142eb5c2bee 2.22kB / 2.22kB  0.0s 
 => => sha256:4dd615d90c9da26a8137ab95596c80093e7a36e92f2303af96236a5503f 8.56kB / 8.56kB  0.0s 
 => => sha256:9baf437a1badb6aad2dae5f2cd4a7b53a6c7ab6c14cba1ed1ecb42b4822 5.16MB / 5.16MB  1.5s 
 => => sha256:db428075304d53783f6c7bdf075a47597464b79fac81622c58b92daf170 2.14kB / 2.14kB  0.0s 
 => => sha256:dbba69284b2786013fe94fefe0c2e66a7d3cecbb20f6d691d71dac891 54.94MB / 54.94MB  5.9s 
 => => sha256:6ade5c59e324bd7cf369c72ad781c23d37e8fb48c9bbb4abbecafafd9 10.87MB / 10.87MB  1.7s 
 => => sha256:b19a994f6d4cdbb620339bd2e4ad47b229f14276b542060622ae44764 54.58MB / 54.58MB  7.7s 
 => => sha256:8fc2294f89de5e20d0ae12149d6136444bcb8c775ea745f06f2eb7 196.55MB / 196.55MB  14.7s 
 => => sha256:9dc715194c21dec8f4d20ea4faa9929b2297b24c123fc8459709266f43e 6.29MB / 6.29MB  7.4s 
 => => extracting sha256:dbba69284b2786013fe94fefe0c2e66a7d3cecbb20f6d691d71dac891ee37be5  3.1s 
 => => sha256:59dc3c5729cd1d72b2fd0913953484d4ecc453f833e0ab53d074bcd6c 19.73MB / 19.73MB  9.7s 
 => => sha256:1312c81b74cee9b25d012de8a666c914ed1862c141098f70728d2e9edc18864 236B / 236B  8.0s 
 => => sha256:2050bfe553ed386581e99bb5724e3565b1dc444ce5d5ce7fb355876e66e 2.87MB / 2.87MB  8.7s 
 => => extracting sha256:9baf437a1badb6aad2dae5f2cd4a7b53a6c7ab6c14cba1ed1ecb42b4822b0e87  0.3s 
 => => extracting sha256:6ade5c59e324bd7cf369c72ad781c23d37e8fb48c9bbb4abbecafafd9be4cc35  0.4s 
 => => extracting sha256:b19a994f6d4cdbb620339bd2e4ad47b229f14276b542060622ae447649294e5d  3.5s 
 => => extracting sha256:8fc2294f89de5e20d0ae12149d6136444bcb8c775ea745f06f2eb775ab4504cd  7.8s 
 => => extracting sha256:9dc715194c21dec8f4d20ea4faa9929b2297b24c123fc8459709266f43e83449  0.3s 
 => => extracting sha256:59dc3c5729cd1d72b2fd0913953484d4ecc453f833e0ab53d074bcd6c0746d27  0.7s 
 => => extracting sha256:1312c81b74cee9b25d012de8a666c914ed1862c141098f70728d2e9edc188644  0.0s 
 => => extracting sha256:2050bfe553ed386581e99bb5724e3565b1dc444ce5d5ce7fb355876e66e655e8  0.2s 
 => [2/5] WORKDIR /usr/src/app                                                             1.1s 
 => [3/5] COPY requirements.txt .                                                          0.2s 
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                              10.7s 
 => exporting to image                                                                     3.0s
 => => exporting layers                                                                    1.9s
 => => writing image sha256:5dd7147604d0d55612e6a7959df7cbb4f23543ede58459a1566f3d959a21c  0.2s
 => => naming to docker.io/library/flaskdocker_web                                         0.1s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```

### 2. Start the docker image
```
docker-compose up    
Recreating flaskdocker_web_1 ... done
Attaching to flaskdocker_web_1
web_1  |  * Serving Flask app 'app' (lazy loading)
web_1  |  * Environment: production
web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
web_1  |    Use a production WSGI server instead.
web_1  |  * Debug mode: on
web_1  |  * Running on all addresses (0.0.0.0)
web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
web_1  |  * Running on http://127.0.0.1:5000
web_1  |  * Running on http://172.18.0.2:5000 (Press CTRL+C to quit)
web_1  |  * Restarting with stat
web_1  |  * Debugger is active!
web_1  |  * Debugger PIN: 381-223-269
```

### 3. Visit the URL: http://127.0.0.1:5000/

```
{
"message": "hello world"
}
```

### 4. Visit the URL: http://127.0.0.1:5000/square/6

```
{
"square": 36
}
```