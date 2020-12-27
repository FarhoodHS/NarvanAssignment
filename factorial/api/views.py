from datetime import datetime

from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView

from factorial.api.serializers import FactorialSerializer
from factorial.utils import factorial_func


class FactorialAPI(APIView):

    serializer_class = FactorialSerializer
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        return Response({'detail': 'Enter a number'})

    def post(self, request):
        n = request.data['n']
        try:
            n = int(n)
            start_time = datetime.now()
            res = factorial_func(n)
            runtime = datetime.now() - start_time
        except ValueError:
            return Response({'detail': 'Input must be an integer.'}, status=HTTP_400_BAD_REQUEST)
        
        return Response({'n': n, 'result': res, 'runtime': runtime})

