class SimpleLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Middleware Initialized")

    def __call__(self, request):
        print("Request path:", request.path)

        response = self.get_response(request)

        print("Response status:", response.status_code)

        return response
    
    
