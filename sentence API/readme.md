## Application requirements
- Registration of a user
- Each user gets 6 tokens
- Store a sentence on mongoDBur database for 1 token
- Retrieve stored sentence from database for 1 token
- When 6 tokens are vanished, show status code 301
- Status code meaning:
    - 200: OK
    - 301: Out of tokens
    - 302: Invalid username and password

## Tech stack
- Python
- Flask
- MongoDB
- Docker

## How to run the application ?

### 1. Build the project using docker

```
PS J:\VSCODE_WORKSPACE\flask\sentence API> docker-compose build
Building web
[+] Building 1.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                          0.0s
 => => transferring dockerfile: 32B                                                                                                                                                                                           0.0s 
 => [internal] load .dockerignore                                                                                                                                                                                             0.0s 
 => => transferring context: 2B                                                                                                                                                                                               0.0s 
 => [internal] load metadata for docker.io/library/python:3                                                                                                                                                                   1.0s 
 => [internal] load build context                                                                                                                                                                                             0.0s
 => => transferring context: 8.49kB                                                                                                                                                                                           0.0s 
 => [1/5] FROM docker.io/library/python:3@sha256:db428075304d53783f6c7bdf075a47597464b79fac81622c58b92daf170c4af3                                                                                                             0.0s 
 => CACHED [2/5] WORKDIR /usr/src/app                                                                                                                                                                                         0.0s 
 => CACHED [3/5] COPY requirements.txt ./                                                                                                                                                                                     0.0s 
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                                           0.0s 
 => [5/5] COPY . .                                                                                                                                                                                                            0.0s 
 => exporting to image                                                                                                                                                                                                        0.1s 
 => => exporting layers                                                                                                                                                                                                       0.0s 
 => => writing image sha256:b89a1a61f4e1f52ca310d4dd12d5118a1b2ffc4692ba05ce5873fff4f7874cfe                                                                                                                                  0.0s 
 => => naming to docker.io/library/sentenceapi_web                                                                                                                                                                            0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```
### 2. Start the docker image

```
PS J:\VSCODE_WORKSPACE\flask\sentence API> docker-compose up   
Starting sentenceapi_db_1 ... done
Recreating sentenceapi_web_1 ... done
Attaching to sentenceapi_db_1, sentenceapi_web_1
db_1   | 2022-04-08T13:01:40.817+0000 I CONTROL  [initandlisten] MongoDB starting : pid=1 port=27017 dbpath=/data/db 64-bit host=27b3bc82b2b4
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten] db version v3.6.4
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten] git version: d0181a711f7e7f39e60b5aeb1dc7097bf6ae5856
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.1t  3 May 2016
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten] allocator: tcmalloc
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten] modules: none
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten] build environment:
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten]     distmod: debian81
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten]     distarch: x86_64
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten]     target_arch: x86_64
db_1   | 2022-04-08T13:01:40.818+0000 I CONTROL  [initandlisten] options: { net: { bindIpAll: true } }
db_1   | 2022-04-08T13:01:40.818+0000 I -        [initandlisten] Detected data files in /data/db created by the 'wiredTiger' storage engine, so setting the active storage engine to 'wiredTiger'.
db_1   | 2022-04-08T13:01:40.818+0000 I STORAGE  [initandlisten]
db_1   | 2022-04-08T13:01:40.818+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
db_1   | 2022-04-08T13:01:40.818+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
db_1   | 2022-04-08T13:01:40.818+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=1434M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),cache_cursors=false,log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
db_1   | 2022-04-08T13:01:41.399+0000 I STORAGE  [initandlisten] WiredTiger message [1649422901:399445][1:0x7fba67831a00], txn-recover: Main recovery loop: starting at 8/6144
db_1   | 2022-04-08T13:01:41.498+0000 I STORAGE  [initandlisten] WiredTiger message [1649422901:498732][1:0x7fba67831a00], txn-recover: Recovering log 8 through 9
db_1   | 2022-04-08T13:01:41.577+0000 I STORAGE  [initandlisten] WiredTiger message [1649422901:577641][1:0x7fba67831a00], txn-recover: Recovering log 9 through 9
db_1   | 2022-04-08T13:01:41.648+0000 I STORAGE  [initandlisten] WiredTiger message [1649422901:648300][1:0x7fba67831a00], txn-recover: Set global recovery timestamp: 0
db_1   | 2022-04-08T13:01:41.669+0000 I CONTROL  [initandlisten]
db_1   | 2022-04-08T13:01:41.669+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
db_1   | 2022-04-08T13:01:41.669+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
db_1   | 2022-04-08T13:01:41.669+0000 I CONTROL  [initandlisten]
db_1   | 2022-04-08T13:01:41.670+0000 I CONTROL  [initandlisten] 
db_1   | 2022-04-08T13:01:41.670+0000 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
db_1   | 2022-04-08T13:01:41.670+0000 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
db_1   | 2022-04-08T13:01:41.670+0000 I CONTROL  [initandlisten]
db_1   | 2022-04-08T13:01:41.679+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
db_1   | 2022-04-08T13:01:41.679+0000 I NETWORK  [initandlisten] waiting for connections on port 27017
db_1   | 2022-04-08T13:01:42.716+0000 I NETWORK  [listener] connection accepted from 172.20.0.3:33962 #1 (1 connection now open)
web_1  |  * Serving Flask app 'app' (lazy loading)
web_1  |  * Environment: production
web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
web_1  |    Use a production WSGI server instead.
db_1   | 2022-04-08T13:01:42.717+0000 I NETWORK  [conn1] received client metadata from 172.20.0.3:33962 conn1: { driver: { name: "PyMongo", version: "4.1.0" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "5.10.16.3-microsoft-standard-WSL2" }, platform: "CPython 3.10.4.final.0" }
web_1  |  * Debug mode: off
web_1  |  * Running on all addresses (0.0.0.0)
web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
web_1  |  * Running on http://127.0.0.1:5000
web_1  |  * Running on http://172.20.0.3:5000 (Press CTRL+C to quit)
```

### 3. Access the URL: http://127.0.0.1:5000/register

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
    "msg": "You succesfully signed up for the API",
    "status": 200
}
```

![register API](https://github.com/Akshaykumarcp/Flask/blob/master/sentence%20API/screenshots/register%20API.png)

### 4. Access the URL: http://127.0.0.1:5000/store

```
# API request body
{
   "username":"akshai",
    "password": "1234",
    "sentence": "Secret message"
}
```

```
# API response
{
    "msg": "Sentence saved succesfully",
    "status": 200
}
```

![store API](https://github.com/Akshaykumarcp/Flask/blob/master/sentence%20API/screenshots/store%20API.png)

### 5. Access the URL: http://127.0.0.1:5000/getSentence

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
    "sentence": "Secret message",
    "status": 200
}
```
![getSentence API](https://github.com/Akshaykumarcp/Flask/blob/master/sentence%20API/screenshots/getSentence%20API.png)
