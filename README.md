# FastAPI Webinar

In October 2021, I did a [PyCharm webinar](https://blog.jetbrains.com/pycharm/2021/10/webinar-smarter-fastapi-through-tooling-with-sebastian-ramirez/) with [Sebastián Ramírez](https://twitter.com/tiangolo/) the creator of [FastAPI](https://fastapi.tiangolo.com) and [SQLModel](https://sqlmodel.tiangolo.com).
The webinar code is largely based on the demo from the SQLModel tutorial -- along with a healthy dose of structure from the Talk Python Training course [Modern APIs with FastAPI](https://training.talkpython.fm/courses/getting-started-with-fastapi) course.
But it's presented in a way to get the max out of tooling, in this case the IDE -- in this case, PyCharm Professional.

Here's the notes and code, maybe screenshots, hell maybe even videos.

:::{admonition} This repo is temporary!!
Once SQLModel gets live and PyCharm's support gets final, I'll move it to the PyCharm Guide.
:::

## Skip Browser

The typical FastAPI dev cycle is to switch between the editor and a browser reload, perhaps with Postman.
In this step, we bring tooling into let us stay in the IDE: HTTP Files then over to `pytest`. 

- We're going to start refactoring to implement Heroes, but first, write tests
- Run the .http file for both endpoints
- Install pytest via pyproject.toml dev dependency ^ 6.2.5 then poetry update and setup in PyCharm
- Make a tests directory ** and mark it?
- Cmd-Shift-T to make tests
- Emphasize endpoints support in client.get
  - Autocomplete, refactor rename, quick docs
- Emphasize parameter in POST
  - Not yet on type inference
- Move client = to conftest.py
- Write next test
- Put tests on autorun with delay
- Show the Endpoints tab
- Add docstring
- Show HTTP Client tab
- .http and testing response values
- Commit

- (SR) response_model and mypy

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
