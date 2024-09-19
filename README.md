# BookInventory

## Installation


### Prerequisites
Node.js and npm installed on your machine.
Python and pip installed on your machine.


### Setup
1. Navigate to the backend directory:
```sh
cd backend
```
2. Install the required Python packages:
  ```sh
  pip install -r requirements.txt
  ```
3. Apply database migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```
4. Start the Django development server:
```sh
python manage.py runserver
```

### Running the Application
Once the backend server is running, you can access the application in your web browser at http://localhost:8000.

### Challenges Faced
One challenge I faced was having to restrict myself on the design aspect due to having very less time to work on it and making most of it.
If I had more time, I would try to improve the UI and use react to for frontend. In addition, I would try to implement a login/logout functionality
using JWT tokens. Lastly, I would have liked to improve the filtering (write a better matching algorithm) and provide a refresh filtering button so 
that users can simply use that instead of removing all the filters manually. 

