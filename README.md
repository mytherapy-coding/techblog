# TechBlog

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

## Microservices

Breaking down the application into several mini parts, mini programs called services. Each service performs a specific business task, creating a modular structure where each service is a separate building block. The failure of one service can occur relatively painlessly for the entire application. Each service has its API that can be accessed to perform a specific task. Services can communicate with each other through HTTP or gRPC requests, known as synchronous communication, where a request is sent, and a response is awaited.

In front of all services, an API Gateway is typically placed. It serves as an intermediary, routing user requests not directly to the services but first through itself, handling the routing.

Another communication option is asynchronous communication, where we don't need to wait for a response from the service. Messages are sent to a message broker like RabbitMQ or Kafka, queued there, and then consumed by a service that reads the queue and performs the necessary actions. The sender, in this case, does not wait for a response and continues working.

However, with benefits come challenges. While some complexities decrease, new ones emerge. Now, each service needs to be raised and configured separately, and connecting them becomes crucial. Architecting with intelligence is necessary, especially paying attention to the consistency of data. Since microservices have specific data in their databases or schemas, performing a join with another table is not straightforward; assembling data in pieces like a puzzle must be done at the application logic level. Moreover, this architecture demands a set of DevOps tools. Containerization is needed for convenient, compact, and independent deployment of microservices. Knowing orchestration becomes crucial for flexible management. Understanding CI/CD pipelines is necessary for smooth deployment. Additionally, setting up logging and monitoring is essential to quickly identify problematic areas in case of issues.

---

## Testing Automation: Programming in QA

Why is automation so important? You can do something manually once, but what about repeating it the third or tenth time? It becomes clear that you need to save your energy, nerves, and time. And testing is one of those areas where automation can be a great help.

Testers check the new functionality of an application to ensure it works as intended. They also test the old functionality to make sure that the new features haven't broken anything. Programs that create programs - that's what automated testing is. It's a process where developers write special programs or scripts, also called automated tests, that tell the computer what actions to perform to check if everything is working properly. When executed, these tests run dozens or even hundreds of different interaction scenarios with the system we are testing and then report which ones passed successfully and which ones didn't.

So, what do these automated tests specifically do?

For instance, you can test the API - write a program that makes requests to your server with different parameters and compares the responses received from the server with what the program expects.

In short, we take tests that were previously done manually, such as going to a specific page, clicking here and there, and seeing what happens. Now, we make a soulless machine do the same without complaints and much faster. This type of testing is called end-to-end, where we simulate the user's path entirely from the user's perspective.

Now, let's take a look at the tools for automated testing. Let's start with Selenium. It's a whole set of tools used for browser automation. We are interested in Selenium WebDriver, a library that allows connecting to the browser and sending commands to make it do something - click a button, fill in a field, and so on. It retrieves some data as a response, which we use as the test result. To achieve this, you need to write code that describes the sequence of browser actions and the expected result. Selenium supports languages like Java, Ruby, JavaScript, and, of course, Python.

Popular alternatives include Puppeteer, Playwright, Cypress, or Appium, which do similar tasks but for mobile phones. These work well with testing frameworks that simplify test management, such as Pytest for Python or JUnit for Java. In a nutshell, these frameworks provide specific functions for your programming language, making it easy to write and run tests in applications.

Another type of testing is performance testing. Its essence is to assess how the system handles load and whether it crashes when it goes into production. For example, sending a huge number of different requests to the server simultaneously, as if they were real users on Black Friday eager to make a purchase. Tools like Apache JMeter and LoadRunner help with this, where we specify which requests to send and with what intensity, then run the test and observe how the server behaves.

Now that we've automated everything, it would be good to add a couple more useful things. Firstly, integrate tests into the CI/CD pipeline so that they run automatically whenever new functionality is added. Secondly, after the check, it would be nice to create a testing report indicating which tests passed, what failed, what needs attention, and so on. Writing these reports manually is not desirable, so we also automate them. There are many tools for this, such as Allure Report. It supports multiple languages and frameworks and can create beautiful graphs and tables based on test results for better visualization.

First, everything needs to be checked manually, ensure that everything works, write test cases and testing scenarios, and only then proceed to automation. Additionally, some things are better

seen by a human. For example, a computer can tell whether a new button on a website is functional but cannot assess how user-friendly it is to interact with.

---

## What is an IP address, and can it reveal anything?

Let's dive into the concept of an IP address. In the IT realm, think of it like addressing an envelope when sending data. If you want to send a request or data, you need to specify the destination (IP address) and the source (your IP address). This is essential for effective communication between devices in a network. For instance, when accessing a website, you send a request to the server's IP, asking for a specific page. The server processes the request and sends back the data to your IP.

Why does an IP address look peculiar?

In the digital world, computers communicate using binary code, represented as zeros and ones. An IP address is essentially a string of 32 zeros in binary. To make it more user-friendly, we convert it to decimal, splitting it into four parts separated by dots. This gives us the familiar IPv4 format with four numbers ranging from 0 to 255. There's also IPv6, using hexadecimal characters and 128 bits, allowing for a vastly increased number of unique addresses.

Differentiating static and dynamic IP addresses:

A static IP remains constant, while a dynamic IP is assigned for a specific period and can change. This is crucial for managing network resources efficiently. Static IPs are useful when devices need a fixed, unchanging address, while dynamic IPs are suitable for temporary connections.

Referring to IP addresses as internal and external:

Given the limited number of IPv4 addresses, Network Address Translation (NAT) comes into play. Port Address Translation (PAT) is a configuration of NAT that allows multiple devices in a local network to share a single external IP address. Each device is identified by a unique port number, adding a layer of security.

Can anything be deduced from an IP address?

Determining specific details from an external IP is challenging because it's shared among numerous devices. Providers, however, can correlate external and internal IPs, maintaining the distinction through unique port assignments. This complexity adds a level of security to the system.
