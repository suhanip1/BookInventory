# BookInventory

#Installation

##Prerequisites
Node.js and npm installed on your machine.
Python and pip installed on your machine.


###BSetup
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
