import time 
import timeit

#Time constants
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
MILLIS_PER_SECOND = 1000

# Function to be measured 
def my_function():
    print("Starting the function...")
    time.sleep(2)
    print("Function finished.")

NUMBER_OF_EXECUTIONS = 2

def measureExecutionTime():
    executionTime = timeit.timeit(stmt=my_function, number=NUMBER_OF_EXECUTIONS)
    #executionTime = 325649.2356456
    hours = int(executionTime / SECONDS_PER_HOUR)
    executionTime =- hours * SECONDS_PER_HOUR
    minutes = int(executionTime / SECONDS_PER_MINUTE)
    executionTime =- minutes * SECONDS_PER_MINUTE
    seconds = int(executionTime)
    executionTime =- seconds

    # At this point we only have the decimal part
    # e.g. 05 seconds = 500 milliseconds
    milliseconds = int(executionTime * MILLIS_PER_SECOND)
   


    print(f"Execution time is {hours} hours, {minutes} minutes, {seconds} seconds and {milliseconds} milliseconds")
    

measureExecutionTime()