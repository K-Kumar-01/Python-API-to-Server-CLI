import argparse

from inspect import isclass
from types import FunctionType

template1 = """
from fastapi import FastAPI
from {module_name} import {class_name}
import uvicorn
app = FastAPI()
{func_name}={class_name}
@app.get("/")
def hello_world():
    msg="Welcome to my FastAPI project!"\
        "Please visit the /docs to see the API documentation."
    return msg\n
    """
template2 = """
# WARNING:DO NOT EDIT THE BELOW LINE
app.add_api_route(
        path="{route_path}",
        endpoint={endpoint},
        methods={http_methods},
    )\n
        """
template3 = """
if __name__ == "__main__":
    uvicorn.run(
    app=app,
    host='0.0.0.0',
    port=5000
)"""


def create_fastapi_file(class_name, module_name, apis_list, store_path):
    import os
    func_name = class_name.lower() + "_func"
    complete_template = template1.format(
        module_name=module_name,
        class_name=class_name,
        func_name=func_name
    )

    for api in apis_list:
        complete_template += template2.format(
            route_path=api['route'],
            endpoint=f"{func_name}.{api['name']}",
            http_methods=api['http_methods']
        )

    complete_template += template3.format(
        func_name=func_name
    )

    try:
        with open(store_path, "x") as f:
            f.write(complete_template)
    except FileExistsError:
        raise Exception("The FastAPI file already exists")

def cli():
    parser = argparse.ArgumentParser(
        prog='mylibrary', description='Builds a file for deployment to server')

    parser.add_argument('--build', type=str, help='Builds the project')
    parser.add_argument('--deploy', action='store_true')

    args = parser.parse_args()

    if args.build:
        pass

    if args.deploy:
        pass


if __name__ == "__main__":
    cli()
