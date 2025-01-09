# SimPy simulation of an M/M/1 queueing system.
# The system has a single server and an infinite queue.
# The inter-arrival time is exponentially distributed with a mean of 1.0 time units.
# The service time is exponentially distributed with a mean of 0.5 time units.
# The simulation should run for 1000 time units.
# The output should be an array of the service times for each customer.
# SimPy simulation of an M/M/1 queueing system with batch arrivals.

import simpy
from statistics import mean
import random
import numpy as np

# Parameters for 2a and 3a
#arrival_rate = 18.0 # Arrival rate (lambda) / 5
#service_rate = 126.0 # 2a
#service_rate = 142.0 # 3a
num_requests = 1_000_000

# Parameters for 2b and 3b
arrival_rate = 36 # Arrival rate (lambda) / 5
#service_rate = 216.0 # 2b
service_rate = 234.0 # 3b

# Results
response_times = []

# ---------------------------------------------------------------------------
# SimPy model
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)

def request_generator(env):
    for i in range(num_requests):
        yield env.timeout(random.expovariate(arrival_rate))

        # Simulate a batch of requests
        num_file_requests = random.randint(1, 9)

        for _ in range(num_file_requests):
            env.process(process_request(env))

def process_request(env):
    arrival_time = env.now
    job = server.request()
    # Wait for the server to become available (wait in the queue)
    yield job
    # Process the request
    yield env.timeout(random.expovariate(service_rate))
    departure_time = env.now
    response_times.append(departure_time - arrival_time)
    server.release(job)

env.process(request_generator(env))
env.run()

# ---------------------------------------------------------------------------
# Compute the results
mean_response_time = np.mean(response_times)
print(f'Mean response time: {mean_response_time:.4f} s')
response_time_99 = np.percentile(response_times, 99)
print(f'Response time (99th percentile): {response_time_99:.4f} s')

# ---------------------------------------------------------------------------
# Visualization

from visualization.plots import histogram_plot, scatter_plot, percentile_plot, heatmap_plot

Numpy_array_response_times = np.array(response_times)

# Histogram plot
histogram_plot(Numpy_array_response_times)

# scatter plot
scatter_plot(Numpy_array_response_times)

# Percentile plot
percentile_plot(Numpy_array_response_times)

# Heatmap plot
heatmap_plot(Numpy_array_response_times)