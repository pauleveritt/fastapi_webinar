# Skip Browser

As part of "smarter", I'm going to show a way of FastAPI development that I find productive.
That is, staying in the IDE and not constantly shifting to the browser, hitting reload and clicking the universe.

This is primarily via [HTTP File](https://www.jetbrains.com/help/pycharm/http-client-in-product-code-editor.html) plus pytest.

The typical FastAPI dev cycle is to switch between the editor and a browser reload, perhaps with Postman.
In this step, we bring tooling into let us stay in the IDE: HTTP Files then over to `pytest`. 

## Demo

- Run the .http file for both endpoints
- Emphasize parameter in POST
  - Rename parameter
  - Search for usages
  - Refactor rename, then undo
  - Autocomplete in `.http`
  - Still some work to do: Not yet on type inference, rename in other places, `.http` up in usages
- *(d02a)* Add a test for status code:
```
> {%
   client.test("Request executed successfully", function() {
      client.assert(response.status === 200, "Response status is not 200");
   });
%}
```
- Show (but **don't demo**) intention actions on an endpoint:
  - Open endpoint in a browser
  - Write to `.http`
- Stop the server
- Install pytest via pyproject.toml dev dependency `^6.2.5` then poetry update and setup in PyCharm
- Make a `tests/conftest.py` file
- Cmd-Shift-T to make tests
- Go into "TDD Mode"
- Add:
  - `client = TestClient(app)`
  - `response = client.get("/")`
  - `assert response.stat` and autocomplete fails
  - Show the type is `Any`
  - Install requests via import then remove the import
  - Finish the assert
  - `assert "Hello World == response.json()["message"]`
- Put tests on autorun with delay
- Move client = to conftest.py
  - Select the line for `client =` 
  - Refactor -> Move
  - Add `client` to the test
- Write next test
  - Copy the body from the first
- Show the Endpoints tab
  - Shows putting structure to work for DX
  - Only shows when endpoints are detected
  - Works when using `APIRouter` also
  - Navigate to declaration when browsing endpoints
  - Shows type info
  - Add docstring and see reflection
  - Show HTTP Client tab
    - .http and testing response values
- Commit

- (SR) response_model and mypy

## Discussion



## `test_main.py`

```{literalinclude} test_main.py
```


## `conftest.py`

```{literalinclude} conftest.py
```
