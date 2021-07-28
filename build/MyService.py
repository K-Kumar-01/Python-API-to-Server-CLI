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
