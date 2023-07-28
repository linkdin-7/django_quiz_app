# django_quiz_app

## Setup and Installation

1. Clone the project.
    ```
    git clone https://github.com/linkdin-7/django_quiz_app.git
    ```

2. Run virtual environment in the root folder
    ```
    python -m venv test
    test\Scripts\activate
    ```

3. Install required packages using requirement.txt in the movieCollection folder.

    ```
    pip install -r requirement.txt
    ```

4. Run Migrate Command
    ```
    python manag.py makemigrations
    python manage.py migrate
    ```

5. Run the Django Server
    ```
    python manage.py runserver
    ```


   ## API Reference
|   API  | Parameter     | Description                |
| :-------- | :------- | :------------------------- |
| `POST http://localhost:8000/api/user/create` | -` | **Required** for registration |
| `GET http://localhost:8000/api/user/login` | `-` |User Login |
| `GET http://localhost:8000/api/quiz/create` | `-` |Create a Quiz (Admin) |
| `POST http://localhost:8000/api/quiz/list` | `-` | List of quiz with section and topic |
| `PUT http://localhost:8000/quiz/<int:pk>/` | `Quiz Id` |Giving Quiz |



## Register the app
![signup](https://github.com/linkdin-7/django_quiz_app/assets/56730903/ce51dbc6-8712-4a5c-b47f-b286f21ac709)

## Login 
![login_new](https://github.com/linkdin-7/django_quiz_app/assets/56730903/4894b4a2-5eac-4e1c-bcbe-7c9cd56553c3)


## Accesing admin by student(Denied Permission Handle)
![studen_permiss_denied](https://github.com/linkdin-7/django_quiz_app/assets/56730903/769b70be-6274-44ce-824c-8a2bd2ef0435)

## Creating Quiz By admin
![quiz_create_new](https://github.com/linkdin-7/django_quiz_app/assets/56730903/875c826b-68f3-4902-8b17-b098e75d6503)

## Quiz List with Section and Topic
![exam_section_topic_list_new](https://github.com/linkdin-7/django_quiz_app/assets/56730903/01acdca2-e86e-48f8-859c-ca792986ec38)






