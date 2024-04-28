from rest_framework_simplejwt.views import TokenViewBase



class GoogleAuthView(TokenViewBase):
    _serializer_class = 'accounts.serializers.GoogleAuthSerializer'


google_auth_view = GoogleAuthView.as_view()