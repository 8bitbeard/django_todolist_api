from rest_framework import pagination


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size=10
    page_size_query_param = 'size'
    max_page_size=20
    page_query_param = 'page'