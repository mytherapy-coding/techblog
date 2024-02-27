## Fun with Infinity

This is how you can define -infinity and +infinity in Python:

```py
float('-inf')
float('+inf')
```
Examples of how infinity works in Python
```py
print(float('-inf'))
print(float('-inf') + float('-inf') )
print(float('+inf') * 10)
print(float('-inf') + float('+inf') )
print(1/float('inf'))
print(max(1000, float('-inf')))
```
Output:
```
-inf
-inf
inf
nan
0.0
1000
```
Note that infinity - infinity is undefined in Math.
Python yields this as `nan`(NaN -- Not a Number):

Here is the example how to use -infinity to compute maximum window:

```py
def find_max_window(nums: list[int], k: int) -> float:
    window_max = float('-inf')
    for i in range(len(nums) - k + 1):
        window_k = nums[i:i + k]
        window_sum = sum(window_k)
        window_max = max(window_sum, window_max)
    return window_max 
```

Note that that is 0(n^2)algorithm. 
But there is nore efficient linear in time algorithm.

---

## Microservices Intro

## Microservices

Breaking down the application into several mini parts, mini programs called services. Each service performs a specific business task, creating a modular structure where each service is a separate building block. The failure of one service can occur relatively painlessly for the entire application. Each service has its API that can be accessed to perform a specific task. Services can communicate with each other through HTTP or gRPC requests, known as synchronous communication, where a request is sent, and a response is awaited.

In front of all services, an API Gateway is typically placed. It serves as an intermediary, routing user requests not directly to the services but first through itself, handling the routing.

Another communication option is asynchronous communication, where we don't need to wait for a response from the service. Messages are sent to a message broker like RabbitMQ or Kafka, queued there, and then consumed by a service that reads the queue and performs the necessary actions. The sender, in this case, does not wait for a response and continues working.

However, with benefits come challenges. While some complexities decrease, new ones emerge. Now, each service needs to be raised and configured separately, and connecting them becomes crucial. Architecting with intelligence is necessary, especially paying attention to the consistency of data. Since microservices have specific data in their databases or schemas, performing a join with another table is not straightforward; assembling data in pieces like a puzzle must be done at the application logic level. Moreover, this architecture demands a set of DevOps tools. Containerization is needed for convenient, compact, and independent deployment of microservices. Knowing orchestration becomes crucial for flexible management. Understanding CI/CD pipelines is necessary for smooth deployment. Additionally, setting up logging and monitoring is essential to quickly identify problematic areas in case of issues.


