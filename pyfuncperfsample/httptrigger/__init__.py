import logging
import sys
import azure.functions as func
from math import sqrt
from pyinstrument import Profiler
import random
from memory_profiler import profile

# creating file for memory profiler
fp = open("/home/memory_profiler.log","w+")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # creating random file for each usage of this function
    f= open("/home/"+str(random.randint(1,1100))+".html","w+")
    profiler = Profiler(use_signal=False) 
    profiler.start()

    n = int(req.params.get('n', 15))
        
    if not n:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('n')

    if n:
        output = str(fibnonci_approach(n))

        # stopping profiler and writing it to random file generated earlier
        profiler.stop()
        f.write(profiler.output_html())

        return func.HttpResponse("Fibnonci of " + str(n) + " using regular approach:" + output)
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )

# running memory profiler on this function
@profile(precision=4 ,stream=fp)
def fibnonci_approach(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibnonci_approach(n - 1) + fibnonci_approach(n - 2)
     