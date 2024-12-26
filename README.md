## Tools

- EC2 Instance
  - t4g series ( graviton )
  - m7g metal
  - EIP
  - Security Group
    - allow from security group 

- Autoscaling Group

- LoadBalancers
  - default eks loadbalancer
  - loadbalancer controller 
  - network loadbalancer
  - target group 
  - listeners

- S3 Bucket
- Cloudfront
  
- VPC
  - peering 


- ECR ( Elastic Container Registry )

- EKS ( Elastic Kubernetes Service )
  - Attach efs and create storage class 
  - ebs storage class
  - efs storage class 
  - use s3 in pod 

- Kubernetes 

  - rollout restart 
  - init container
  - readiness/liveness tcp socket
  - security context for root user 
  - install nfs provistioner storage class for nfs server 
  - Affinity 

  - Kubernetes Api Gateway 

  - Istio 
    - Istio Gateway
    - sidecar mode
    - ambiant mode
    - mtls
    - istio gateway 
    - k8s gateway 
    - virtual service
    - destination rule 

- mongo db 

- aws Aurora RDS ( MYSQL )
  - update certificate 
  - instance type 
  - backup plan 

- ElastiCache ( Redis OSS )
  - create cluster using cli
  - cluster mode 

- Adminer
  - connect all kind of db 
  - take db backup 

- MSK ( managed streeming for kafka ) kafka cluster
  - cluster configuration
  - brokers configuration
  - kafka ui 
  - bitnami kafka cluster helm chart with auto create topics 
  - without authantication configuration 

- Lambda

- Architechture Diagram 

- Cost estimation 

- prometheus - grafana - loki
  - grafana agents 
  - promtail agents for logs 

- github 

- HA-Proxy 

- AMI

- EBS

- Jenkins

- Cronjobs 

- Python scripts for daily cost 

- Route 53
  - Types of Records
  - alias record to lb 
  - 

- EFS

- SQS

- SES

- SNS


- what is vpc endpoint indepth
- how to increase site to site vpn speed
- nat gateway indepth
- network loadbalancer in-depth ( network loadbalancer controller )
- karpenter indepth
- how to make changes name of instance in terraform file without recreating instance

# Questions
- Types of Load Balancers provided by AWS: AWS provides three types - Application Load Balancer (ALB), Network Load Balancer (NLB), and Classic Load Balancer (CLB).
- Choosing ALB over NLB or CLB: Choose ALB for HTTP/HTTPS traffic with advanced routing (e.g., path-based or host-based). Use NLB for ultra-low latency and handling TCP/UDP traffic. CLB is generally legacy.
- Path-based routing in ALB: ALB routes requests based on URL paths, allowing different target groups for different parts of the website or application.
- AWS Auto Scaling integration with ELB: Auto Scaling can register/deregister instances with ELB automatically based on scaling policies.
- Target Group in ALB/NLB: A Target Group is a logical grouping of instances or IPs that receive requests routed by the Load Balancer.
- Sticky Session in AWS Load Balancers: Sticky sessions, or session affinity, bind a client’s session to a specific instance to maintain session state.
- Securing your Load Balancer: Use SSL/TLS certificates, enable security groups, configure access control, and use WAF (Web Application Firewall) for added protection.
- Health checks in Elastic Load Balancer: ELB performs health checks on targets to ensure only healthy instances receive traffic. It pings, attempts a TCP connection, or makes HTTP requests to check target health.
- Cross-Zone Load Balancing: Cross-zone load balancing distributes incoming requests evenly across instances in all enabled Availability Zones.
- Monitoring and troubleshooting issues with AWS Load Balancer: Use Amazon CloudWatch for metrics, access logs, and error logs; review target health checks and instance status.
- SSL/TLS termination in AWS ELB: SSL/TLS termination decrypts client traffic at the Load Balancer, reducing the load on backend instances.
- Availability Zone failure with ELB: ELB will route traffic to instances in remaining healthy Availability Zones, if cross-zone load balancing is enabled.
- Configuring ALB for WebSocket traffic: ALB supports WebSocket for bidirectional communication by configuring listener rules to route WebSocket connections.
- Pricing for AWS Load Balancers: Pricing depends on load balancer hours, data processed, and additional features like cross-zone load balancing.
- Listener rules vs. target groups in ALB: Listener rules determine routing behavior for incoming requests, while target groups specify the actual resources to receive the traffic.
- Connection draining in AWS ELB (deregistration delay): Allows in-flight requests to complete before de-registering an instance to ensure a smooth transition during scaling or maintenance.
- NLB low latency: NLB operates at Layer 4 and uses pass-through architecture, providing ultra-low latency for high-performance applications.
- Using AWS Load Balancer with on-premise resources: You can extend ALB/NLB to route traffic to on-premises servers through Direct Connect or VPN for hybrid architecture.
- Role of AWS Global Accelerator with ELB: AWS Global Accelerator provides a static IP and directs traffic to optimal AWS endpoints, reducing latency and improving performance.
- Common error codes in ALB: Common codes include 503 (unavailable), 504 (timeout), and 502 (bad gateway), often due to connectivity or configuration issues.
- Cross-region load balancing in AWS: AWS Global Accelerator can route traffic across AWS regions, providing cross-region load balancing.
- Troubleshooting unhealthy targets in AWS Load Balancer: Check health check settings, target status, security groups, and application logs.
- ELB integration with AWS Lambda: ALB can trigger Lambda functions for HTTP/S requests, enabling serverless applications behind a load balancer.
- Handling multi-tenant applications with ALB: Use host-based or path-based routing to segment traffic to different tenant resources.
- Key metrics to monitor in CloudWatch for ELB: Monitor metrics like RequestCount, Latency, HealthyHostCount, UnHealthyHostCount, and HTTPCode_Target_5XX_Count.
- ELB integration with ECS: ELB integrates with ECS by automatically registering/deregistering containers in target groups as they scale.
- Load Balancer vs. Reverse Proxy: A load balancer distributes traffic across multiple servers, while a reverse proxy forwards requests to a specific server behind it.
- Implementing SSL offloading on AWS Load Balancer: Configure SSL certificates on the load balancer to handle SSL termination, reducing SSL workload on backend instances.
- Role of sticky sessions in multi-instance architecture: Use sticky sessions to maintain session state when needed; avoid if instances need stateless or distributed sessions.
