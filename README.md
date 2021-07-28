Converts Python API to Server

## How to Use
1. Clone the repo `git@github.com:K-Kumar-01/Python-API-to-Server-CLI.git`.
2. Change the directory `cd Python-API-to-Server-CLI`
3. Create a virtual environment `virtualenv -p python3 venv`.
4. Activate the virtual environment source `venv/bin/activate`.
5. Run `python3 setup.py install`

## Commands
`mylibrary --build <fileName.py>`

Builds the file i.e. converts the file to a fastapi code.
Currently single file with no custom imports is only available.

## Structure of file
1. Should not contain custom imports
2. Should contain a class and some functions in it.
3. A decorator which adds the attributes (mentioned in the sample file)  on the used function. 
   These attributes are compulsory. Apart from these any other attribute may be added but 
   they won't be used.

A Sample structure of the file
```python
def api(route, http_methods, *args, **kwargs):
    def decorator(func):
        setattr(func, 'is_api', True)
        setattr(func, "_api_route", route)
        setattr(func, 'http_methods', http_methods)
        return func
    return decorator


class MyService():
    @api(route="/", http_methods=['GET'])
    def predict():
        return {'Hello': 'World'}

    def withoutApi():
        return {'I am': 'without api'}

```

Running the above command will generate a `build` folder in the **current working directory**.

The build can be run locally by doing the following:
1. While in virtual environment, `pip install fastapi` and `pip install uvicorn[standard]`.
2. `cd build`.
3. Run `uvicorn main:app --reload`

The server will be running on `localhost:8000` 