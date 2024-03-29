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

---

## HTTP or HTTPS - How It Works and What's the Difference?

HTTP:// stands for Hypertext Transfer Protocol, the protocol for transferring hypertext. Why these prefixes of Greek origin? The term "hypertext" referred to a system of text pages with various footnotes and references to each other. The oldest example of literary hypertext is the Bible. Nowadays, hypertext is associated with the internet, and any web page in it is considered hypertext. Click on an image, and you'll be instantly redirected elsewhere. This is called a hyperlink. So, HTTP transfers hypertext with hyperlinks, representing a path to another file on the internet. It does this by establishing a TCP session on port 80.

Through HTTP, you get a page with video, and the page itself is written in Hypertext Markup Language (HTML). HTTP is a client-server protocol. This means you have a client (you, in this case) that wants to get some data (video), and a server where this data is stored. Seeing a video on YouTube, for example, and clicking on it, you send an HTTP request to the YouTube server and get an HTML page with that video in response. You can also access it by knowing its address or URL (Uniform Resource Locator), which translates to a Uniform Resource Identifier.

HTTP consists of a start line, headers, and a message body. The start line specifies the URL, i.e., where to send it, and the request method. For example, requesting a video, you send a GET request. There are other methods like POST, PUT, HEAD, DELETE, and others. The response start line from the server differs from the request. It includes a three-digit status code indicating the processing status of your request. For example, if everything went well, the server returns the 200 OK code, but if the server couldn't find anything based on your request, you get the famous 404 Not Found code. There are a total of 5 types of codes:

1xx - Informational responses about the process of transferring the request.
2xx - Information about successful transfer.
3xx - Information about redirection.
4xx - Client errors, indicating that either what you're looking for is not found, or you're doing it wrong, or you're not allowed here.
5xx - Server errors, indicating that the server is currently having a hard time.

Moving on. Headers are parameters that define the request or describe the message body. For example, information about the browser being used, language, authorization, and so on. Finally, there's the body - the data you transmit in the request (e.g., text of a comment) or the response you receive from the server (a page with a video).

All this data is transmitted in the open as plain text. This is unsafe. That's why there's an extension to the protocol called HTTPS, where "S" stands for secure.

HTTPS encrypts all data before transmission, making it impossible to read if intercepted. Encryption is provided by SSL and TLS mechanisms. SSL (Secure Socket Layer) works like this: when connecting to a site using SSL, you first ask the site to identify itself. In response, it sends you a copy of the SSL certificate, proving that communication with it is secure. The browser checks it, and if everything is okay, responds to the site that it can be trusted, and encrypted data exchange begins. How does the browser know the certificate is valid? Certificates are issued by certification authorities, and they are not issued to just anyone. They verify the user and their rights to the resource so that the user can be sure the site is genuine. These certification authorities also confirm to the browser that the sent certificate is valid.

The second protocol, TLS (Transport Layer Security), is a newer version of SSL. It also checks the authenticity of the server and encrypts data. Currently, TLS 1.2 and 1.3 are in use.

Search engines lower the ranking of sites without HTTPS in search results, and Google even threatens to stop working with such resources.

---

## DNS Server - What Is It and How Does It Work?

DNS (Domain Name System)

A practical example from real life is the contacts in your smartphone. For instance, behind the name ALENA are the actual numerical digits of a phone number. However, when searching for a contact, we input the name rather than the phone number. This is essentially what a DNS server does - it simplifies our lives.

Initially, your device checks the browser or operating system cache. If you've visited a site before, the information about it remains locally cached, saving time in subsequent searches.

If the site is new, a request is sent to the resolver DNS server. Typically hosted by the provider, it can be changed using, for example, the quad eights (8.8.8.8). If the resolver doesn't find the address, it sends a request to the root server. This server, located at the top of the DNS hierarchy, is not singular but multiple. To streamline the search, it helps to navigate to the right branch.

Next, you need to contact the relevant top-level or TLD (top-level domain) server. Top-level domains are what comes after the dot, such as com, org, net. There are Generic Top Level Domains (gTLD), like .edu, .com, .ai (related to artificial intelligence), and Country Code Top Level Domains (ccTLD) tied to specific countries like .ru, .us, .uk.

The resolver then directs the query to a lower level - the Authoritative Nameserver, which provides the required address.

Finally, the resolver records the address in the cache to avoid repeating the same chain of requests.

---
## Exploring Command-Line Tools for DNS and IP Address Retrieval

This Python script uses the `socket` module to retrieve and print all IP addresses associated with the domain name "google.com." The `get_all_ip_addresses` function attempts to obtain the IP addresses using the `gethostbyname_ex` function and prints the results. If an error occurs, such as the domain not being valid, it prints an error message. The main part of the script sets the domain name and calls the function for demonstration purposes.

```py
import socket

def get_all_ip_addresses(domain_name):
    try:
        _, _, ip_addresses = socket.gethostbyname_ex(domain_name)
        print(f"All IP addresses for {domain_name}: {', '.join(ip_addresses)}")
    except socket.gaierror:
        print(f"Unable to get IP addresses for {domain_name}")


domain_name = "google.com"
get_all_ip_addresses(domain_name)
```

If you want to retrieve IP addresses using the command line or terminal, you can use tools like nslookup or dig. Here's how you can do it:

```bash 
nslookup google.com
```
```bash
dig +short google.com
```
```bash 
host google.com
```
---
## HTTP GET Request
To execute an HTTP GET request to a specified URL and display the response using Python, you can utilize the following code. If you are in a controlled environment and comprehend the associated risks, you have the option to disregard SSL verification. Nevertheless, it is strongly discouraged for production environments due to security considerations.

```py
import urllib.request
import ssl

def send_get_request(url):
    try:
        # Create an SSL context that doesn't verify certificates
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=context) as response:
            print("HTTP Status Code:", response.getcode())
            print("Response:")
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error: {e}")

url = "https://leetcode.com/"
send_get_request(url)
```

If you are seeking an alternative method to access a website without employing Python, you may consider using command-line tools such as curl or wget. These tools are commonly employed for making HTTP requests. Here's an example using curl:
```bash
curl -L <your_url>
```
or 
```bash
wget -qO- "https://example.com/"
```
---
## TCP and UDP

A protocol refers to a set of rules or conventions that define how data is transmitted and received between devices on a network. 

Examples of network protocols include:

-Transmission Control Protocol (TCP): Ensures reliable and ordered delivery of data.

-Internet Protocol (IP): Manages the addressing and routing of data packets in a network.

-Hypertext Transfer Protocol (HTTP): Facilitates communication for web browsing.

-File Transfer Protocol (FTP): Defines rules for transferring files between devices.

-Simple Mail Transfer Protocol (SMTP): Governs the sending of emails over a network.


TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two different transport layer protocols used for communication over the Internet. 

TCP (Transmission Control Protocol):

-Ensures information is sent correctly, like making sure your friend hears every word when you talk on the phone.
-Takes a bit more time but is careful to get everything right.
-Good for things like downloading files or watching videos.

UDP (User Datagram Protocol):

-Sends information quickly, like sending a message without waiting for a response.
-Doesn't worry too much if some details get lost.
-Good for fast activities like playing online games or streaming videos.

In summary, TCP is connection-oriented, reliable, and ensures the ordered delivery of data, while UDP is connectionless, less reliable, and prioritizes low-latency communication. The choice between TCP and UDP depends on the specific requirements of the application.

---

## tcp_server.py and tcp_client.py

When tcp_server.py and tcp_client.py are used together, they create a simple client-server communication system using the TCP (Transmission Control Protocol) network protocol.

Let's break down the interactions between tcp_server.py and tcp_client.py

#### tcp_server.py (Server Script)

```py
import socket

# Choose the port
port = 1235

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('0.0.0.0', port))

print(f"Server is listening on port {port}")

# Start listening for incoming connections
server_socket.listen()

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    try:
        # Receive data from the client
        data_received = client_socket.recv(1024).decode()
        print(f"Received request: {data_received}")

        # Send a response back to the client
        response_message = "I received your message"
        client_socket.sendall(response_message.encode())

    except Exception as e:
        # Print any errors
        print(f"Error: {e}")

    finally:
        # Close the connection with the current client
        client_socket.close()

```
### Initialization:

- The server script creates a TCP socket and binds it to a specified address and port.
- It starts listening for incoming connections.


### Accepting Connections:

- The server enters into a loop, continuously accepting incoming connections.
- For each accepted connection, the server creates a new socket specifically for that client.

### Handling Data:

- After accepting a connection, the server receives data from the connected client.
- In the provided example, it prints the received data to the console and sends a fixed response back to the client.

### Connection Closure:

- The server then closes the connection with the current client.
Repeat:

- The server continues listening for and accepting new connections, repeating the process.


#### tcp_client.py (Client Script)

tcp_client.py script appears to be a basic example of a TCP client in Python. This client script connects to a specified server (IP address and port), sends a greeting message to the server, waits for a response, and then prints the received response. Here's a breakdown of the script:

```py
import socket

# Replace with the server's IP address and port
server_ip = "127.0.0.1"
server_port = 1235

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to {server_ip}:{server_port}")

# Greeting message
message_to_send = "hello server!"

try:
    # Send the message to the server
    client_socket.sendall(message_to_send.encode())

    # Wait for a response from the server
    response_message = client_socket.recv(1024).decode()

    # Print the response
    print(f"I received your message: {response_message}")

except Exception as e:
    # Print any errors
    print(f"Error: {e}")

finally:
    # Close the connection
    client_socket.close()

```
### Initialization:

- The client script creates a TCP socket.

- Connecting to the Server:

- The client connects to the server using the server's IP address and port.

### Sending Data:

- The client sends a message (greeting) to the server.

- Receiving Response:

- The client waits for a response from the server.

### Printing the Response:

- Upon receiving the response, the client prints it to the console.

### Connection Closure:

- The client then closes the connection.

This basic example illustrates a simple one-way communication from the client to the server, with the server responding to each client independently. In more complex scenarios, we might implement bidirectional communication or handle multiple clients concurrently.

Here are the shortened commands to run the server and client scripts:

#### Server (tcp_server.py):

```bash
cd path/to/server-directory
python3 tcp_server.py
```

#### Client (tcp_client.py):

```bash
cd path/to/client-directory
python3 tcp_client.py
```
Ensure that Python 3 is installed on your machine, and you may need to use python instead of python3 based on your Python installation.

---
## tcp_server.py and browser(http)

## Introduction
Frameworks are powerful tools that simplify development by providing pre-built components and structures. However, they're not for everyone. Some developers prefer to work without frameworks, either due to personal preference, project constraints, or philosophical reasons. In this post, we'll explore why it's okay to hate frameworks and how you can thrive as a framework-free developer.

## The Framework Dilemma
Frameworks offer numerous advantages, such as speeding up development, providing standardized solutions, and offering community support. However, they also come with drawbacks. Some developers find frameworks restrictive, bloated, or overly complex. Additionally, reliance on frameworks can lead to a lack of understanding of core concepts and hinder creativity.

## Reasons to Embrace Framework-Free Development
1. Flexibility and Control
Working without frameworks gives you complete control over your code. You're not bound by the limitations or conventions imposed by a framework. This flexibility allows you to tailor your solutions to fit the specific needs of your project without compromise.

2. Deep Understanding
Building applications from scratch forces you to understand the underlying principles and technologies. Without the crutch of a framework, you'll gain a deeper understanding of programming languages, design patterns, and architecture, making you a more versatile developer in the long run.

3. Lightweight Solutions
Frameworks often come with a lot of overhead, including unnecessary features and dependencies. By writing code without frameworks, you can create lightweight, optimized solutions that perform better and are easier to maintain.

4. Innovation and Creativity
Without the constraints of a framework, you're free to experiment with unconventional approaches and innovative solutions. This creative freedom can lead to breakthroughs and unique products that stand out in a crowded market.

## Tips for Framework-Free Development
1. Start Small
Begin by building simple projects without relying on frameworks. This allows you to gradually familiarize yourself with core concepts and techniques before tackling more complex challenges.

2. Leverage Libraries
While you may eschew frameworks, there's no need to reinvent the wheel. Take advantage of libraries and modules that provide specific functionality without imposing a rigid structure on your code.

3. Focus on Best Practices
Even without a framework, it's essential to adhere to best practices in software development. Write clean, maintainable code, follow established design patterns, and prioritize scalability and performance.

4. Embrace Learning
Framework-free development is an ongoing learning process. Stay curious, explore new technologies, and continuously seek to improve your skills. Engage with the developer community, attend workshops, and read relevant articles and books.


Here's an example of a simple Python HTTP server implemented without using any frameworks, along with a corresponding terminal command to demonstrate its usage:

```py
import socket

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request:\n{request}")

    # Extract the requested URL from the request
    try:
        url = request.split()[1]
    except IndexError:
        url = '/'

    # Define response content based on requested URL
    if url == '/':
        # Home page content
        response_content = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html\n\n"
            "<html><body>"
            "<h1>Welcome to the Home Page</h1>"
            "<p>This is the home page.</p>"
            "<p><a href='/about'>About</a></p>"
            "</body></html>"
        )
    elif url == '/about':
        # About page content
        response_content = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html\n\n"
            "<html><body>"
            "<h1>About Us</h1>"
            "<p>This is the about page.</p>"
            "<p><a href='/'>Home</a></p>"
            "</body></html>"
        )
    else:
        # Page not found
        response_content = (
            "HTTP/1.1 404 Not Found\n"
            "Content-Type: text/html\n\n"
            "<html><body>"
            "<h1>404 Not Found</h1>"
            "<p>The requested page was not found.</p>"
            "</body></html>"
        )

    # Send the response
    client_socket.send(response_content.encode('utf-8'))

    # Close the connection with the client
    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1235)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print(f"Server is listening on {server_address}")

    while True:
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    run_server()
```

Save this code to a Python file, for example, http_server.py, and run the python file.

In a terminal window or tab, open Google Chrome using the open command:

```bash
open -a "Google Chrome" http://127.0.0.1:1235
```
This command will open the specified URL http://127.0.0.1:1235 in Google Chrome, allowing you to see the response from the server in your web browser.

You can achieve the same by using curl to make a request to the server after starting it with Python. Here's how you can do it:

First, execute the Python code to start the server:

```bash
python http_server.py
```
This will start the HTTP server listening on 127.0.0.1:1235.

Then, in another terminal window or tab, use curl to make a request to the server:

```bash
curl http://127.0.0.1:1235
```
This curl command sends a GET request to the specified address and port where the server is running (127.0.0.1:1235). You will receive the response from the server directly in the terminal, without needing to open a web browser.


# Conclusion

Hating frameworks doesn't make you a bad developer; it simply means you have a different approach to problem-solving. Framework-free development offers numerous benefits, including flexibility, deep understanding, lightweight solutions, and creative freedom. By embracing this mindset and following best practices, you can thrive as a framework-free developer and build innovative, high-quality software.

Remember, there's no one-size-fits-all solution in software development. Whether you love or hate frameworks, what matters most is delivering value to your users and continuously improving your craft.

