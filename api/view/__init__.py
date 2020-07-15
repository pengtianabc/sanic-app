# file: api/handler/__init__.py
from .my_view import views as my_view
# export for parent
views = []
views.extend(my_view)
