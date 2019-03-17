from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        return {
            'Access-Control-Allow-Origin': '*'
        }
