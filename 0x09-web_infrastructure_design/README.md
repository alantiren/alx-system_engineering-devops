0x09. Web infrastructure design
DevOps
SysAdmin
web infrastructure
 By: Sylvain Kalache, co-founder at Holberton School
 Weight: 1


 TASK 0
 Sure! Let's design the one-server web infrastructure for www.foobar.com:

1. Server:
   - We have one server that will act as the main hosting machine for all our components.

2. Domain Name (foobar.com):
   - The domain name "foobar.com" serves as the address of our website on the internet. Users can access our website by typing "www.foobar.com" in their web browsers.

3. DNS Record (www):
   - The DNS record for "www.foobar.com" is a CNAME (Canonical Name) record. It points to the domain itself, indicating that the "www" subdomain should resolve to the main domain, foobar.com.

4. Web Server (Nginx):
   - The web server (e.g., Nginx) handles incoming HTTP requests from users. It acts as the front-facing component and serves static content like HTML, CSS, and images directly to the user's browser.

5. Application Server:
   - The application server is responsible for running our application code (e.g., Python Flask, Ruby on Rails, etc.). It handles dynamic requests and generates responses based on the user's actions or inputs.

6. Application Files (Code Base):
   - The application files consist of our website's code base, including scripts, templates, and resources required to run the application. These files are stored on the server and accessed by the application server during runtime.

7. Database (MySQL):
   - The database (e.g., MySQL) stores and manages the website's data, such as user information, posts, comments, etc. The application server communicates with the database to read and write data as needed.

User Accessing the Website:

1. When a user wants to access our website, they will type "www.foobar.com" into their web browser.

2. The DNS resolver on the user's computer will look up the IP address associated with "www.foobar.com" using the DNS system.

3. The DNS record for "www.foobar.com" will resolve to our server's IP address, which is 8.8.8.8.

4. The user's computer will establish a connection to our server (8.8.8.8) through the internet.

5. The web server (Nginx) on our server will receive the incoming HTTP request from the user's computer.

6. If the request is for static content (e.g., HTML, CSS), the web server will serve it directly to the user's computer.

7. If the request requires dynamic content, the web server will forward the request to the application server.

8. The application server will process the request, interact with the database if needed, generate the appropriate response (e.g., dynamically generated HTML), and send it back to the web server.

9. The web server will then send the response back to the user's computer, which will display our website in the user's web browser.

Issues with the Infrastructure:

1. Single Point of Failure (SPOF):
   - Since we have only one server, if it fails or experiences downtime, the entire website will become inaccessible. To mitigate this, we can introduce redundancy by using multiple servers or cloud-based solutions.

2. Downtime During Maintenance:
   - When performing maintenance tasks, such as deploying new code that requires restarting the web server, the website may experience downtime. We can implement strategies like rolling deployments and load balancing to reduce downtime during maintenance.

3. Cannot Scale with High Traffic:
   - With only one server, our infrastructure may struggle to handle high traffic loads. If too much incoming traffic occurs, it can lead to slower response times or crashes. To address this, we can introduce load balancing and scale horizontally by adding more servers to distribute the load effectively. Cloud-based solutions can also provide scalability options.

Overall, this one-server web infrastructure is suitable for small-scale websites or testing purposes. However, to ensure higher availability, better scalability, and reduced downtime, it's essential to consider more advanced infrastructure designs and architecture.

TASK 1
Sure, let's design a three-server web infrastructure for www.foobar.com:

Components:
1. Two Servers (Server A and Server B):
   - We add two servers to introduce redundancy and improve the overall availability of the website. In case one server fails, the other server can handle incoming traffic.

2. Web Server (Nginx):
   - The web server (e.g., Nginx) handles incoming HTTP requests from users. It serves static content like HTML, CSS, and images, and also acts as a reverse proxy to distribute requests to the application servers.

3. Application Server:
   - The application server runs the website's application code (e.g., Python Flask, Ruby on Rails, etc.). It handles dynamic requests and generates responses based on user interactions.

4. Load Balancer (HAProxy):
   - The load balancer (e.g., HAProxy) distributes incoming HTTP requests across multiple application servers (Server A and Server B). It ensures that the load is evenly distributed, optimizing performance and preventing overload on a single server.

5. Set of Application Files (Code Base):
   - The application files consist of the website's code base, including scripts, templates, and resources required to run the application. These files are stored on both Server A and Server B and accessed by the application servers during runtime.

6. Database (MySQL):
   - The database (e.g., MySQL) stores and manages the website's data, such as user information, posts, comments, etc.

Explanation of the Infrastructure:

1. Additional Servers (Server A and Server B):
   - We add two servers to improve redundancy and fault tolerance. If one server goes down, the other can take over, ensuring the website remains accessible.

2. Load Balancer (HAProxy):
   - We introduce a load balancer to distribute incoming requests across multiple application servers. It uses a distribution algorithm (e.g., Round Robin) to evenly distribute the load.

3. Database Primary-Replica (Master-Slave) Cluster:
   - The database is set up in a Primary-Replica configuration. The Primary node handles write operations (e.g., INSERT, UPDATE) and replicates the data to the Replica node(s). The Replica node(s) handle read operations (e.g., SELECT). This setup improves read scalability and provides data redundancy.

4. Security Issues:
   - One notable issue is the lack of a firewall, leaving the infrastructure vulnerable to unauthorized access. To enhance security, a firewall should be implemented to control incoming and outgoing traffic.

   - Additionally, the absence of HTTPS means that data transmitted between the user's browser and the website is not encrypted, potentially exposing sensitive information. Implementing HTTPS is crucial to secure data transmission.

5. Single Points of Failure (SPOF):
   - While we have redundancy in the form of two servers, other components like the load balancer and database might become SPOFs. To mitigate this, we can introduce additional load balancers and set up a High Availability (HA) database cluster.

Load Balancer Configuration:
   - The load balancer is configured with a Round Robin distribution algorithm. It works by sequentially sending each incoming request to the next available server in the pool (Server A, Server B, Server A, Server B, and so on). This ensures that each server receives an equal share of the traffic.

Active-Active vs. Active-Passive Setup:
   - The load balancer enables an Active-Active setup, where both Server A and Server B actively handle incoming traffic simultaneously. In an Active-Passive setup, only one server is active at a time, with the other server serving as a standby backup.

Difference Between Primary and Replica Nodes:
   - In a database Primary-Replica cluster, the Primary node handles write operations and is the authoritative source for data changes. The Replica nodes replicate data from the Primary node and handle read operations. Application servers typically interact with the Primary node for data writes and can perform read operations on both the Primary and Replica nodes.

Issues with the Infrastructure:

   - SPOFs: The load balancer and database can be single points of failure if they experience issues. Additional redundancy measures can help mitigate this.

   - Security Issues: The lack of a firewall and HTTPS implementation can expose the infrastructure to potential security breaches.

   - No Monitoring: Without monitoring, we lack visibility into the infrastructure's performance and health, making it challenging to identify and address potential issues proactively. Implementing monitoring tools is essential for maintaining a healthy web infrastructure.

   TASK 2
   Sure, let's design a three-server web infrastructure for www.foobar.com that is secured, serves encrypted traffic, and is monitored:

Components:
1. Three Servers (Server A, Server B, Server C):
   - We add three servers to provide redundancy and fault tolerance. If one server goes down, the others can handle incoming traffic, ensuring high availability.

2. Web Server (Nginx):
   - The web server (e.g., Nginx) handles incoming HTTP requests from users. It serves static content and also acts as a reverse proxy to distribute requests to the application servers.

3. Application Server:
   - The application server runs the website's application code (e.g., Python Flask, Ruby on Rails, etc.). It handles dynamic requests and generates responses based on user interactions.

4. Database (MySQL):
   - The database (e.g., MySQL) stores and manages the website's data, such as user information, posts, comments, etc.

5. Firewalls:
   - We add three firewalls to enhance security by controlling incoming and outgoing traffic to and from the servers. Firewalls help prevent unauthorized access and protect against various cyber threats.

6. SSL Certificate:
   - We install an SSL certificate on the web server to serve www.foobar.com over HTTPS. HTTPS encrypts the traffic between the users' browsers and the web server, ensuring secure data transmission and protecting sensitive information from interception.

7. Monitoring Clients (Data Collector):
   - We install monitoring clients (e.g., Sumo Logic, Prometheus, etc.) on each server to collect performance metrics, logs, and other data. Monitoring provides real-time insights into the infrastructure's health, performance, and potential issues.

Explanation of the Infrastructure:

1. Firewalls:
   - Firewalls are added to control network traffic and enforce security policies. They act as a barrier between the internet and the servers, filtering incoming and outgoing traffic based on predefined rules. This helps protect the infrastructure from unauthorized access and various cyber threats.

2. SSL Certificate (HTTPS):
   - Serving traffic over HTTPS ensures that data transmitted between the users' browsers and the web server is encrypted and secure. This protects sensitive information, such as login credentials and personal data, from being intercepted by malicious actors.

3. Monitoring:
   - Monitoring is used to keep track of the infrastructure's health, performance, and potential issues. It helps identify and resolve problems proactively, ensuring high availability and optimal performance.

4. Monitoring Data Collection:
   - The monitoring clients collect data from various sources, such as server performance metrics, application logs, and database queries. This data is sent to the monitoring service (e.g., Sumo Logic) where it is analyzed and presented in a dashboard for visualization and alerting.

Monitoring Web Server QPS:
   - To monitor the web server's QPS (Queries Per Second), we can collect the number of incoming HTTP requests per second on the web server. Monitoring tools can provide real-time graphs and alerts when the QPS exceeds predefined thresholds.

Issues with the Infrastructure:

1. Terminating SSL at the Load Balancer Level:
   - Terminating SSL (decrypting HTTPS traffic) at the load balancer level and sending unencrypted traffic to the web servers can expose sensitive data on the internal network. To mitigate this, SSL termination should be performed directly on the web servers.

2. One MySQL Server Capable of Accepting Writes:
   - Having only one MySQL server capable of accepting writes introduces a single point of failure for write operations. If this server goes down, write functionality will be affected. Implementing a Primary-Replica (Master-Slave) cluster can provide data redundancy and improved write scalability.

3. Servers with All the Same Components:
   - Having servers with identical components (database, web server, and application server) may lead to a lack of diversity in the infrastructure. If a critical vulnerability affects one component, it can potentially affect all servers. Introducing some variations in the infrastructure, such as using different web server technologies or databases, can improve resilience.

By addressing these issues, we can create a more robust, secure, and highly available web infrastructure for www.foobar.com.

TASK 3

**Web Server vs. Application Server**

In the context of a web infrastructure, the terms "web server" and "application server" refer to distinct components that serve different purposes in handling incoming requests and generating responses for web applications. Let's explore the specifics of each component:

1. **Web Server**:
   - A web server is responsible for handling incoming HTTP requests from clients (such as web browsers) and serving static content like HTML, CSS, images, and other files. It acts as the front-facing component that interacts directly with users.

   - Web servers are optimized for serving static content efficiently and can handle multiple simultaneous connections with low overhead. They often use protocols like HTTP and HTTPS to communicate with clients.

   - Examples of web servers include Nginx and Apache.

2. **Application Server**:
   - An application server is responsible for running the application code and handling dynamic requests that require processing or access to a database. It processes business logic, performs calculations, and interacts with databases or other backend services to generate dynamic content.

   - Application servers are typically used to execute server-side code and handle application-specific tasks, such as user authentication, data processing, and generating customized responses.

   - Examples of application servers include Gunicorn, uWSGI, and Tomcat.

**Designing the Infrastructure:**

Requirements:
1. **One Server**: We will have one server that hosts all the components.

2. **Load Balancer (HAProxy) as a Cluster**: We will use HAProxy as a load balancer to distribute incoming traffic across multiple instances of the web server and application server. This cluster setup provides high availability and ensures that if one instance fails, traffic can be redirected to others.

3. **Split Components with Their Own Server**: We will split the web server, application server, and database components onto separate servers to improve performance, separation of concerns, and scalability.

Explanation of Additional Elements:

1. **Load Balancer (HAProxy)**:
   - We add a load balancer (HAProxy) to distribute incoming HTTP requests across multiple instances of web and application servers. Load balancing optimizes resource utilization, ensures even distribution of traffic, and improves fault tolerance. It enhances the overall performance and availability of the application.

2. **Split Components to Separate Servers**:
   - By splitting components onto separate servers, we can scale each component independently based on its specific resource requirements. For example, if the application server requires more processing power, we can add more instances of the application server without affecting the web server or database. This flexibility allows us to handle varying workloads effectively.

By combining a load balancer with separate servers for web, application, and database components, we create a scalable, high-performance, and highly available web infrastructure that can handle increased traffic and ensure smooth operations of the application. This design allows us to optimize resource utilization, improve fault tolerance, and achieve better overall performance.