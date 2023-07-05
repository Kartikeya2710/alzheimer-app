<div style="text-align:center ">
    <h1>
        <a href="https://alzheimer-detection.onrender.com/"> Alzheimer Prediction</a> 
    </h1>
</div>

Web application deployment for alzheimer detection from MRI images

## <div align="center">Documentation</div>

1. Build Docker image with `docker-compose`
    ```bash
    docker-compose build --no-cache
    ```

2. Run Docker container with `docker-compose`
    ```bash
    docker-compose -f docker-compose.yml up
    ```

3. [Parallelize](https://fastapi.tiangolo.com/async/#concurrency-parallelism-web-machine-learning) the application
    - Use gunicorn as a process manager with uvicorn workers to take advantage of multi-core CPUs in production for running multiple processes in parallel.
    - This is achieved in `config/gunicorn.py`. More specifically:
        ```bash
        workers = int(os.getenv('WEB_CONCURRENCY', multiprocessing.cpu_count() * 2))
        worker_class = os.getenv('WORKER_CLASS', 'uvicorn.workers.UvicornWorker')
        ```
    - Example showing parallelization for a CPU with 6 cores and 12 logical processors
        ```bash
        [+] Building 0.0s (0/0)                                                                                                          
        [+] Running 2/2
        ✔ Network alzheimer-app_default            Created                                                                         0.1s 
        ✔ Container alzheimer-app-alzheimer-app-1  Created                                                                         0.1s 
        Attaching to alzheimer-app-alzheimer-app-1
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:39 +0000] [1] [INFO] Starting gunicorn 20.1.0
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:39 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:39 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [7] [INFO] Booting worker with pid: 7
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [8] [INFO] Booting worker with pid: 8
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [9] [INFO] Booting worker with pid: 9
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [10] [INFO] Booting worker with pid: 10
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [11] [INFO] Booting worker with pid: 11
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [12] [INFO] Booting worker with pid: 12
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [13] [INFO] Booting worker with pid: 13
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [14] [INFO] Booting worker with pid: 14
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [15] [INFO] Booting worker with pid: 15
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [16] [INFO] Booting worker with pid: 16
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [39] [INFO] Booting worker with pid: 39
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [51] [INFO] Booting worker with pid: 51
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [52] [INFO] Booting worker with pid: 52
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [54] [INFO] Booting worker with pid: 54
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [53] [INFO] Booting worker with pid: 53
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [55] [INFO] Booting worker with pid: 55
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [67] [INFO] Booting worker with pid: 67
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [75] [INFO] Booting worker with pid: 75
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [91] [INFO] Booting worker with pid: 91
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:40 +0000] [92] [INFO] Booting worker with pid: 92
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:41 +0000] [93] [INFO] Booting worker with pid: 93
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:41 +0000] [94] [INFO] Booting worker with pid: 94
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:41 +0000] [95] [INFO] Booting worker with pid: 95
        alzheimer-app-alzheimer-app-1  | [2023-07-05 20:03:41 +0000] [96] [INFO] Booting worker with pid: 96
        ```

4. Shut down and remove running containers with `docker-compose`
    ```bash
    docker-compose -f docker-compose.yml down
    ```