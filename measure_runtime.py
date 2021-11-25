import time 
import timeit

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
def my_function():
    print("Starting the function...")
    time.sleep(2)
    print("Function finished.")

def measureExecutionTime():
    executionTime = timeit.timeit(stmt=my_function, number=2)
    #executionTime = 325649.2356456
    hours = int(executionTime / SECONDS_PER_HOUR)
    executionTime = executionTime - hours * SECONDS_PER_HOUR
    minutes = int(executionTime / SECONDS_PER_MINUTE)
    executionTime = executionTime - minutes * SECONDS_PER_MINUTE
    seconds = int(executionTime)
    executionTime = executionTime - seconds
    milliseconds = int(executionTime * 1000)
   


    print(f"Execution time is {hours} hours, {minutes} minutes, {seconds} seconds and {milliseconds} milliseconds")
    

measureExecutionTime()