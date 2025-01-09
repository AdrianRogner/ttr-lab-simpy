Lab report: capacity planning and performance analysis with SimPy
========================================================================

> [!NOTE]
> Write your report in this document. You can write it in English or French

Result table
------------

This table documents the results of the different simulation scenarios

| Case                                                   | Required service rate | Mean service time  | Response time      |
|--------------------------------------------------------|-----------------------|--------------------|--------------------|
| 1a. Base scenario: $\lambda = 90/s$                    | $\mu = 100 /s$        | $1/\mu$ = 10 ms    | mean: 100 ms       |
| 1b. M/M/1 model for $\lambda = 180/s$                  | $\mu = 190    /s$     | $1/\mu$ = 5  ms    | mean: 100 ms       |
| 2a. Batch arrivals with $\lambda_\text{web} = 90$/s    | $\mu = 126    /s$     | $1/\mu$ = 7     ms | mean: 100 ms       |
| 2b. Batch arrivals with $\lambda_\text{web} = 180$/s   | $\mu = 216    /s$     | $1/\mu$ = 4     ms | mean: 100 ms       |
| 3a. Batch arrivals with $\lambda_\text{web} = 90$/s    | $\mu = 142    /s$     | $1/\mu$ = 7     ms | 99th perc.: 300 ms |
| 3b. Batch arrivals with $\lambda_\text{web} = 180$/s   | $\mu = 234    /s$     | $1/\mu$ = 4     ms | 99th perc.: 300 ms |



Case 1a: Base scenario
----------------------

Scenario

- M/M/1 model
- $\lambda = 90$ requests per second
- Target response time $E[t] = 100$ ms

Use the analytical model to compute required service rate $\mu$. Report the value in the table on top.



Case 1b: Doubling the arrival rate
----------------------------------

Use the same scenario as in Case 1a, but double the arrival rate $\lambda$.

Use the analytical model to compute the required service rate $\mu$. Report it in the table on top.

**Question**: does the service rate need to double, too? Interpret the result.

No we don't have to double it, we have have to add the difference between the two arrival rates to the service rate. So we have to add 90 to the service rate. The service rate is now 190 requests per second. The response time is still 100 ms.

Case 2a: Batch arrivals
-----------------------

Simulate the model with batch arrivals and an arrival rate of Web pages (not file requests) of $\lambda = 90$ web requests per second.

Which service rate is required to achieve a mean response time of $E[t] = 100$ ms. Report this result in the table on top.

**Question**: interpret this result!

On a M/M/1 model the service rate is 100 requests per seconde because there are now queings, but in a batch arrivals the service rate is 126 requests per second because there are a bit of queueing.

Case 2b: Batch arrivals and double arrival rate
-----------------------------------------------

Determine the service rate \$mu$ that is required if the arrival rate of Web pages doubles and we want to achieve a response time of 100 ms.

Report this result in the table on top. Interpret the result.

Similar case as case 2a, but the service rate is now 216 requests per second because of queuing.

Case 3a: Batch arrivals and 99th percentile
-------------------------------------------

Determine the service rate $\mu$ that is required such that the 99th percentile of the response time is around 300 ms.

Report this result in the table on top. Interpret the result.

We need a server to work at 142 requests per second to have a response time of 300 ms. This is a matter of probability because we included an random factor to determine the number of files requested. So when we have a lot of file requested a long queue will be created. So we need a service rate of 142 requests per second to have a response time of 300 ms for the 99 perc.

Case 3b: Batch arrivals, double arrival rate and 99th percentile
----------------------------------------------------------------

Determine the service rate $\mu$ that is required if the arrival rate of Web pages doubles such that the 99th percentile of the response time is around 300 ms.

Report this result in the table on top.



Visualization
-------------

Use the plot functions defined in the file `visualization/plots.py` to visualize the response time distribution for the case 3b (Batch arrivals, double arrival rate and 99th percentile).

Include each plot in this report and interpret the results.

**Answer**:

![histogram plot](images/histogram.png)

![scatter plot](images/scatter.png)

![percentiles plot](images/percentiles.png)

![heatmap plot](images/heatmap.png)

In the histogram plot we can see the majority of the response time is between 0 and 400 ms. 

In the scatter plot we don't see clearly the distribution of the response time. but we can affirm that there are some plot where the response time is higher than 400 ms.

In the percentile plot the mean and median response time is under 100 ms. We have a precise idea about the 95th percentile, it is around 200 ms and the 99th is between 200 and 600 ms.

In the heatmap plot we can see that during the whole simulation there are not big response time, during the simulation all the plot are in the reasonable range of response time (under 130 ms).

Conclusion
----------

Document your conclusions here. What did you learn from the simulation results?

**Answer**:

In these simulations we saw the effort we have to do to have a good response time. We saw the service rate is affected by the arrival rate and how they come. When it's in batch it's a lot heavier in request so the service rate has to be higher even with the same arrival rate as an M/M/1 model. 

if we want to satisfy the 99th percentile we have to increase even more the service rate. this case can happen in real life and it impacts a lot the experience of the end user. So we are forced to have a good service rate to have a good response time. 