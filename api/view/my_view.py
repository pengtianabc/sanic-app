# file: api/view/my_view.py
from sanic import response
from sanic.views import HTTPMethodView
from base import authorized, authorized
# for global views, register after
views = []

class SimpleView(HTTPMethodView):
    decorators  = [authorized()]
    # relative path, ex: /api/view/myview
    __url__ = '/myview'
    async def get(self, request):
        return response.text('I am get method')

    # You can also use async syntax
    async def post(self, request):
        return response.text('I am post method')

    async def put(self, request):
        return response.text('I am put method')

    async def patch(self, request):
        return response.text('I am patch method')

    async def delete(self, request):
        return response.text('I am delete method')
# register to views
views.append(SimpleView)
