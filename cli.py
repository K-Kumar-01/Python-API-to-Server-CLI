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


def methods(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]


def save_direct(
    path
):
    if path[-2:] != "py":
        raise Exception("the file is not a python file")

    import os
    import importlib
    import inspect
    import sys
    complete_path = os.path.join(os.getcwd(), path)

    head, module_name = os.path.split(complete_path)
    sys.path.append(head)
    module_name = module_name[:-3]
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        raise Exception(f"Couldn't import module:", e)

    count = 0
    class_names = []

    apis_list = []
    for name, obj in inspect.getmembers(module):
        try:
            if isclass(obj):
                apiDict = dict()
                count += 1
                class_names.append(obj.__name__)
                MysteriousClass = getattr(module, obj.__name__)
                classMethods = methods(MysteriousClass)
                for method in classMethods:
                    method_to_Call = getattr(MysteriousClass, method)
                    try:
                        if(hasattr(method_to_Call, 'is_api')):
                            apiDict['http_methods'] = getattr(
                                method_to_Call, 'http_methods')
                            apiDict['route'] = getattr(
                                method_to_Call, '_api_route')
                            apiDict['name'] = method

                            apis_list.append(apiDict)

                    except e:
                        print(e)
                        pass

        except e:
            print(e)
            pass
    try:
        buildPath = os.path.join(os.getcwd(),'build')
        os.mkdir(buildPath)
    except FileExistsError:
        raise Exception("The Build Folder already exists. Delete the previous build and re run the command")

    original_file:str

    with open(f"{module_name}.py", "r") as fh:
        original_file = fh.read()
    
    if(len(original_file)>0):
        try:
            with open(f'./build/{module_name}.py', "x") as f:
                f.write(original_file)
        except FileExistsError:
            raise Exception("The FastAPI file already exists")

    try:
        with open(f'./build/requirements.txt', "x") as f:
            requirements = """fastapi
uvicorn
"""
            f.write(requirements)
    except FileExistsError:
        raise Exception("Requirements file already exists")

    create_fastapi_file(class_name=module_name,
                        module_name=class_names[0], apis_list=apis_list, store_path='./build/main.py')


def cli():
    parser = argparse.ArgumentParser(
        prog='mylibrary', description='Builds a file for deployment to server')

    parser.add_argument('--build', type=str, help='Builds the project')
    parser.add_argument('--deploy', action='store_true')

    args = parser.parse_args()

    if args.build:
        save_direct(f'{args.build}')

    if args.deploy:
        pass


if __name__ == "__main__":
    cli()
