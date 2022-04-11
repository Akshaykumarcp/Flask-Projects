## Application requirements
- Registration of a user API
- Each user gets 6 tokens
- Detect text similarity API for 1 token
- Refill tokens API
- When 6 tokens are vanished, show status code 303
- Status code meaning:
    - 200: OK
    - 301: Invalid username 
    - 302: Invalid password
    - 303: Out of tokens
    - 304: Invalid admin password

## Tech stack
- Python
- Flask
- Spacy
- MongoDB
- Docker

## How to run the application ?

- Build the project using docker

    ```PS J:\VSCODE_WORKSPACE\flask\similarity of text> docker-compose build
    Building web
    [+] Building 4.4s (11/11) FINISHED
    => [internal] load build definition from Dockerfile      0.0s
    => => transferring dockerfile: 32B   0.0s 
    => [internal] load .dockerignore     0.0s 
    => => transferring context: 2B       0.0s 
    => [internal] load metadata for docker.io/library/python:3 1.1s 
    => [1/6] FROM docker.io/library/python:3@sha256:db428075304d53783f6c7bdf075a47597464b79fac81622c58b92daf170c4af3  0.0s
    => [internal] load build context    0.0s 
    => => transferring context: 5.00kB   0.0s 
    => CACHED [2/6] WORKDIR /usr/src/app    0.0s 
    => CACHED [3/6] COPY requirements.txt ./   0.0s 
    => CACHED [4/6] RUN pip install --no-cache-dir -r requirements.txt   0.0s 
    => [5/6] COPY . .   0.1s 
    => [6/6] RUN pip install ./en_core_web_sm-3.2.0.tar.gz  3.0s
    => exporting to image   0.2s
    => => exporting layers   0.2s 
    => => writing image sha256:a3405439c1e1f8e392a644dba034619e68cbd69c969a0ff7240c34fa499425da  0.0s 
    => => naming to docker.io/library/similarityoftext_web  0.0s 

    Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
    ```

- Start the docker image

    ```
    PS J:\VSCODE_WORKSPACE\flask\similarity of text> docker-compose up   
    Starting similarityoftext_db_1 ... done
    Recreating similarityoftext_web_1 ... done
    Attaching to similarityoftext_db_1, similarityoftext_web_1
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten] MongoDB starting : pid=1 port=27017 dbpath=/data/db 64-bit host=9d0aabdb9540
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten] db version v3.6.4
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten] git version: d0181a711f7e7f39e60b5aeb1dc7097bf6ae5856
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.1t  3 May 2016
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten] allocator: tcmalloc
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten] modules: none
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten] build environment:
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten]     distmod: debian81
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten]     distarch: x86_64
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten]     target_arch: x86_64
    db_1   | 2022-04-11T04:22:26.439+0000 I CONTROL  [initandlisten] options: { net: { bindIpAll: true } }
    db_1   | 2022-04-11T04:22:26.439+0000 I -        [initandlisten] Detected data files in /data/db created by the 'wiredTiger' storage engine, so setting the active storage engine to 'wiredTiger'.
    db_1   | 2022-04-11T04:22:26.439+0000 I STORAGE  [initandlisten]
    db_1   | 2022-04-11T04:22:26.439+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
    db_1   | 2022-04-11T04:22:26.439+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
    db_1   | 2022-04-11T04:22:26.439+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=1434M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),cache_cursors=false,log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
    db_1   | 2022-04-11T04:22:27.024+0000 I STORAGE  [initandlisten] WiredTiger message [1649650947:24495][1:0x7f9ad6418a00], txn-recover: Main recovery loop: starting at 2/5888
    db_1   | 2022-04-11T04:22:27.107+0000 I STORAGE  [initandlisten] WiredTiger message [1649650947:107212][1:0x7f9ad6418a00], txn-recover: Recovering log 2 through 3
    db_1   | 2022-04-11T04:22:27.157+0000 I STORAGE  [initandlisten] WiredTiger message [1649650947:157532][1:0x7f9ad6418a00], txn-recover: Recovering log 3 through 3
    db_1   | 2022-04-11T04:22:27.211+0000 I STORAGE  [initandlisten] WiredTiger message [1649650947:211428][1:0x7f9ad6418a00], txn-recover: Set global recovery timestamp: 0
    db_1   | 2022-04-11T04:22:27.228+0000 I CONTROL  [initandlisten]
    db_1   | 2022-04-11T04:22:27.228+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
    db_1   | 2022-04-11T04:22:27.228+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
    db_1   | 2022-04-11T04:22:27.228+0000 I CONTROL  [initandlisten]
    db_1   | 2022-04-11T04:22:27.228+0000 I CONTROL  [initandlisten]
    db_1   | 2022-04-11T04:22:27.228+0000 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
    db_1   | 2022-04-11T04:22:27.228+0000 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
    db_1   | 2022-04-11T04:22:27.228+0000 I CONTROL  [initandlisten]
    db_1   | 2022-04-11T04:22:27.233+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
    db_1   | 2022-04-11T04:22:27.233+0000 I NETWORK  [initandlisten] waiting for connections on port 27017
    web_1  |  * Serving Flask app 'app' (lazy loading)
    web_1  |  * Environment: production
    web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
    web_1  |    Use a production WSGI server instead.
    web_1  |  * Debug mode: off
    db_1   | 2022-04-11T04:22:28.366+0000 I NETWORK  [listener] connection accepted from 172.21.0.3:43284 #1 (1 connection now open)
    web_1  |  * Running on all addresses (0.0.0.0)
    web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
    web_1  |  * Running on http://127.0.0.1:5000
    web_1  |  * Running on http://172.21.0.3:5000 (Press CTRL+C to quit)
    db_1   | 2022-04-11T04:22:28.367+0000 I NETWORK  [conn1] received client metadata from 172.21.0.3:43284 conn1: { driver: { name: "PyMongo", version: "4.1.0" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "5.10.16.3-microsoft-standard-WSL2" }, platform: "CPython 3.10.4.final.0" }
    ```

## Spacy model download

- spacy model: https://github.com/explosion/spacy-models/releases?q=en_core&expanded=true

![spacy-model](https://github.com/Akshaykumarcp/Flask/blob/master/similarity%20of%20text/screenshots/spacy-model.png)

## Test APIs 
(All APIs are POST requests)

- http://127.0.0.1:5000/register

    ```
    # API request body
    {
        "username":"akshai",
        "password": "1234"
    }
    ```

    ```
    # API response
    {
        "msg": "You successfully signed up for the API",
        "status": 200
    }
    ```

    ![register](https://github.com/Akshaykumarcp/Flask/blob/master/similarity%20of%20text/screenshots/register.png)

- http://127.0.0.1:5000/register (when same user trys to register again)

    ```
    # API request body
    {
        "username":"akshai",
        "password": "1234"
    }
    ```

    ```
    # API response
    {
        "msg": "Invalid username",
        "status": 301
    }
    ```

    ![register-error](https://github.com/Akshaykumarcp/Flask/blob/master/similarity%20of%20text/screenshots/register-error.png)

- http://127.0.0.1:5000/detect

    ```
    # API request body
    {
    "username":"akshai",
        "password": "1234",
        "text1": "Data science is fantastic",
        "text2": "Data science is awesome"
    }
    ```

    ```
    # API response
    {
        "msg": "Similarity score calculated successfully",
        "ratio": 0.9217326869692786,
        "status": 200
    }
    ```

    ![detect](https://github.com/Akshaykumarcp/Flask/blob/master/similarity%20of%20text/screenshots/detect.png)

- http://127.0.0.1:5000/detect

    ```
    # API request body
    {
    "username":"akshai",
        "password": "1234",
        "text1": "Data science is fantastic",
        "text2": "Data science is awesome"
    }
    ```

    ```
    # API response
    {
        "msg": "You are out of tokens, please refill!",
        "status": 303
    }
    ```

    ![detect out of tokens](https://github.com/Akshaykumarcp/Flask/blob/master/similarity%20of%20text/screenshots/detect-out-of-tokens.png)

- http://127.0.0.1:5000/refill

    ```
    # API request body
    {
        "username":"akshai",
        "admin_pw": "1234",
        "refill":4
    }
    ```

    ```
    # API response
    {
        "msg": "Invalid Admin Password",
        "status": 304
    }
    ```

- http://127.0.0.1:5000/refill

    ```
    # API request body
    {
        "username":"akshai",
        "admin_pw": "abc123",
        "refill":4
    }
    ```

    ```
    # API response
    {
        "msg": "Refilled successfully",
        "status": 200
    }
    ```

    ![refill](https://github.com/Akshaykumarcp/Flask/blob/master/similarity%20of%20text/screenshots/refill.png)
