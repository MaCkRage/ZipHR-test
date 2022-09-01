# Test Ticket of ZipHR
## Project: ZipAirlines

### Plan to deployment of the development environment on docker-compose
1. : Install all you need 
    * [Docker](https://hub.docker.com/search?q=&type=edition&offering=community)  
    * [Git](https://git-scm.com/downloads)
2. : Download the project
   ```
   git clone https://github.com/MaCkRage/ZipHR-test.git
   ```
#### 3. Go to `ZipHR-test` folder in your terminal
#### 4. **_If you are very lazy_**, just run ```bash run.sh``` with parameter: 
   1. `test` if you want django globally on your machine
   2. `prod` if you want django run in container
   
   **_Or you can deploy project manually_**:
   1. edit and copy environments
      ```
      cp example.env .env
      ```
   2. create virtual env and install requirements
      ```
      virtualenv -p python3.7 venv
      source venv/bin activate
      python -m pip install --upgrade pip
      pip install -r requirements.txt
      ```
   3. run databases:
      ```
      docker-compose up -d
      ```
   4. run django
      ```
      python backend/manage.py migrate
      python backend/manage.py runserver
      ```
#### 5. If you want to fill database with default data, just run:
   ```
   python backend/manage.py fill_db
   ```
   This will create 10 base airplanes and superuser.
   His name and his password are `mac`.
   This command will run automatically if you have used run.sh

#### 6. For tests ypu can run runtests.py
### 7.  If you are reading this, you have been able to start this project.
For optimal testing this project's api, you can open 
```
http://localhost:8000/api/swagger/
```

You never used `Swagger`? Sad, but not bad. This is a [perfect toolset](https://swagger.io/) for showing api and sending test requests.Just try 
it, and you will fall in love with it, I'm sure!

For sending request from task just click on blue button with get request like this
`/plane/{id}/fuel_consumption/`, than click on `Try it out` in the right part of the opened modal window,
insert your values in Parameters form (read description to understand what is what) and click on big
blue button "Execute". 

See the response lower.

### Enjoy!

## PS: 
1) No admin panel
2) No validation
3) No coverage 

 Hope you don't get offended. I didn't have much time