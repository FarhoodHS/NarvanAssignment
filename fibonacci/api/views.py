from datetime import datetime

from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView

from fibonacci.api.serializers import FibonacciSerializer
from fibonacci.utils import fibonacci_func


class FibonacciAPI(APIView):

    serializer_class = FibonacciSerializer
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        return Response({'detail': 'Enter a number'})

    def post(self, request):
        n = request.data['n']
        try:
            n = int(n)
            start_time = datetime.now()
            res = fibonacci_func(n)
            runtime = datetime.now() - start_time
        except ValueError:
            return Response({'detail': 'Input must be an integer.'}, status=HTTP_400_BAD_REQUEST)
       
        return Response({'n': n, 'result': res, 'runtime': runtime})