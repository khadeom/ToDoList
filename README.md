# ToDoList API
This is a brief description of what this app does and how these apis work <br/>
As specified, this is a ToDoList REST API<br/>

To start the project, one needs to run the server first using the specified virtual environment.<br/>
On Linux,<br/>
Enter following commands once you are in this directory<br/>
<pre>
    source venv/bin/activate 
    pip install -r requirements.txt

    in "/TODO/env/lib/python3.8/site-packages/taggit_serializer/serializers.py"
    change line 6 to from "django.utils.translation import gettext_lazy as _"

    python manage.py runserver
    python manage.py createsuperuser
</pre>
Now the application server has started,<br/><br/>

<h3>Every Functionality implemented in the code could have been implemented using various other methods. I have used methods which I felt would be appropriate</h3>
To access anything in the api , one needs to be logged in otherwise it will raise Authentication errors.<br/><br/>

<h4>To register using the API: - </h4><br/>

ENDPOINT - <a href="http://localhost:8000/api/auth/register/">http://localhost:8000/api/auth/register/</a>
<pre>
data = {
    "username": "",
    "password": "",
}
</pre><br/><br/>
<h4>To login and authenticate into the API :</h4><br/>

ENDPOINT - <a href="http://localhost:8000/api/auth/login/">http://localhost:8000/api/auth/login/</a><br/>
<pre>
data = {
    "username": "",
    "password": "",
}
</pre><br/>
<b>After logging in you can use below ENDPOINTS </b>
<br/><br/>
Make a Get Request To
<h4>View all Todo's</h4><br/>
ENDPOINT - <a href="http://localhost:8000/api/main/">http://localhost:8000/api/main/</a><br/>
<br/><br/>
Make a POST request to the ENDPOINT <br/>
<b>To add task </b><br/>
ENDPOINT - <a href="http://localhost:8000/api/main/create/}">http://localhost:8000/api/data/create/</a><br/>
it has been taken care that due date is greater than time stamp

<br/><br/>
<b>To edit a task </b><br/>
ENDPOINT - <a href="http://localhost:8000/api/main/create/{id}/">http://localhost:8000/api/main/create/{id}/</a><br/>
<br/>
Replace {id} with respective task to edit<br/>
<br/><br/>
<h4>To Delete a Task</h4>
ENDPOINT - <a href="http://localhost:8000/api/main/delete/{id}">http://localhost:8000/api/main/delete/{id}</a><br/>

Replace {id} with respective id of task to delete.<br/>

