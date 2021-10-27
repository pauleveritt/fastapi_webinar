# FastAPI Webinar

In October 2021, I did a [PyCharm webinar](https://blog.jetbrains.com/pycharm/2021/10/webinar-smarter-fastapi-through-tooling-with-sebastian-ramirez/) with [Sebastián Ramírez](https://twitter.com/tiangolo/) the creator of [FastAPI](https://fastapi.tiangolo.com) and [SQLModel](https://sqlmodel.tiangolo.com).
The webinar code is largely based on the demo from the SQLModel tutorial -- along with a healthy dose of structure from the Talk Python Training course [Modern APIs with FastAPI](https://training.talkpython.fm/courses/getting-started-with-fastapi) course.
But it's presented in a way to get the max out of tooling, in this case the IDE -- in this case, PyCharm Professional.

Here's the notes and code, maybe screenshots, hell maybe even videos.

:::{admonition} This repo is temporary!!
Once SQLModel gets live and PyCharm's support gets final, I'll move it to the PyCharm Guide.
:::

## Skip Browser



## Discussion

3. **Heroes**. Let's start implementing the Heroes tutorial from SQLModel, but first, just as Pydantic models.

    - Tests first
      - Fail faster on typing and testing
    - Write model in main.py, will extract later
    - response_model with type hint in test
    - Use debugger first to simulate confused
    - Navigation and usages thanks to type hint on function args
    - Heros -> Heroes
      - Refactor symbol name and type annotations
      - Including in Google Doc String
    - Quick documentation inlay and Endpoints tab for docs

4. **Database**.

    - Refactor -> Move to models
    - DataGrip by double clicking on the .db file
    - Mention you might have to download drivers first
    - Depends() doesn't do typing right
    - Project-level problems view for things like typing
5. 
6. **Frontend**.
    - Now navigation and usages on the endpoints shows:
      - the JS, the .http, maybe later the test
    - `.content` the div.content and make a .css, then show navigation/usage/rename
