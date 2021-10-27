# Skip Browser

As part of "smarter", I'm going to show a way of FastAPI development that I find productive.
That is, staying in the IDE and not constantly shifting to the browser, hitting reload and clicking the universe.

This is primarily via [HTTP File](https://www.jetbrains.com/help/pycharm/http-client-in-product-code-editor.html) plus pytest.

The typical FastAPI dev cycle is to switch between the editor and a browser reload, perhaps with Postman.
In this step, we bring tooling into let us stay in the IDE: HTTP Files then over to `pytest`. 

## Demo

- Run the .http file for both endpoints
- Use intention action to open endpoint in a browser
  - Show but don't demo, write to `.http`
- Install pytest via pyproject.toml dev dependency `^6.2.5` then poetry update and setup in PyCharm
- Make a `tests` directory
- Cmd-Shift-T to make tests
- Emphasize endpoints support in client.get
  - Autocomplete, refactor rename, quick docs
- Emphasize parameter in POST
  - Rename parameter
  - Search for usages
  - Refactor rename, then undo
  - Autocomplete in `.http`
  - Still some work to do: Not yet on type inference, rename in other places, `.http` up in usages
- Move client = to conftest.py
- Put tests on autorun with delay
- Write next test
- Show the Endpoints tab
  - Shows putting structure to work for DX
  - Only shows when endpoints are detected
  - Navigate to declaration when browsing endpoints
  - Shows type info
  - Add docstring and see reflection
  - Show HTTP Client tab
    - .http and testing response values
- Commit

- (SR) response_model and mypy

## Discussion

