from datetime import datetime

from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from rest_framework.views import APIView

from ackermann.api.serializers import AckermannSerializer
from ackermann.utils import ackermann_func


class AckermannAPI(APIView):

    serializer_class = AckermannSerializer
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        return Response({'detail': 'Enter desired numbers'})

    def post(self, request):
        m = request.data['m']
        n = request.data['n']
        try:
            m, n = int(m), int(n)
            start_time = datetime.now()
            res = ackermann_func(m, n)
            runtime = datetime.now() - start_time
        except RecursionError:
            return Response({'error': 'Sorry, this calculation is beyond limitations!'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError:
            return Response({'detail': 'Inputs must be integers.'}, status=HTTP_400_BAD_REQUEST)


        return Response({'m': m, 'n': n, 'result': res, 'runtime': runtime})