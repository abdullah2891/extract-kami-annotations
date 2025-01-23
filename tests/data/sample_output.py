sample_output = [
"what's difference betwenn ECS launch type vs far gate?|• Amazon Elastic Container Service (Amazon ECS) • Amazon’ s own container platform
• Amazon Elastic Kubernetes Service (Amazon EKS) • Amazon’ s managed Kubernetes
(open source) • AWS Far gate • Amazon’ s own Serverless container platform • Wor ks
with ECS and with EKS • Amazon ECR: • Store container images",
"how does ec2 instance launch type pulls ecs|EC2 Launch Type: you must provision & maintain the infrastructure (the
EC2 instances  
Each EC2 Instance must run the ECS Agent to register in the ECS Cluste",

"How can data volume work with ecs |EC2 Instance Profile (EC2 Launch Type only): • Used by the ECS agent •Makes API calls to ECS service • Send container logs to CloudW atch Logs • Pull Docker
image from ECR • Reference sensitive data in Secrets Manager or SSM Parameter Stor |
can you run different roles for each ecs far gate task?|Allows each task to have a specific role",

"Type of ecs scaling schemes|Ta r g e t Tr a c k i n g – scale based on tar get value for a specific Cloudwatch metric • Step Scaling – scale based on a specified CloudW atch Alarm •
Scheduled Scaling – scale based on a specified date/time (predictable changes)",

"Types of autoscaling scheme for ecs|Auto Scaling Group Scaling • Scale your ASG based on CPU Utilization •Add EC2 instances over time • ECS Cluster Capacity Provider • Used to automatically
provision and scale the infrastructure for your ECS Tasks • Capacity Provider paired
with an Auto Scaling Group • Add EC2 Instances when you’re missing capacity (CPU,
RAM...)"
]
