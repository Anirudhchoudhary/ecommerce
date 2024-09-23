from django.conf import settings

class CustomValueMiddleware:
    """
    Middleware to add a custom value to each request.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add custom value to the request
        request.WHATSAPPURL = settings.WHATSAPP_URL
        # Call the next middleware or the view
        response = self.get_response(request)
        
        return response