AWS Serverless Quiz Application
Project Overview

This project demonstrates a serverless quiz application built using AWS services. The frontend is hosted on an Amazon EC2 instance running Nginx, while the backend uses API Gateway, AWS Lambda, and DynamoDB to process and store quiz results.

This project was developed as part of a Cloud and DevOps learning exercise to understand how to build a simple full-stack cloud application using a serverless architecture.

Architecture
User Browser → EC2 (Frontend) → API Gateway → Lambda → DynamoDB
AWS Services Used
Amazon EC2

Hosts the quiz frontend application.

OS: RHEL 9

Web Server: Nginx

Serves the index.html quiz interface

Amazon API Gateway

Provides a REST API endpoint that allows the frontend to send quiz results to the backend.

Example endpoint:

POST /submit
AWS Lambda

Processes quiz submissions and stores the results in DynamoDB.

Amazon DynamoDB

Stores quiz results in a NoSQL database including:

Name

Email

Phone

Score

Attempted Questions

Timestamp

Application Workflow

User opens the quiz website hosted on EC2.

User enters details and answers the quiz.

The frontend calculates the score using JavaScript.

A POST request is sent to API Gateway.

API Gateway triggers a Lambda function.

Lambda stores the quiz result in DynamoDB.

Example Data Stored in DynamoDB
email: user@example.com
name: Test User
phone: 9999999999
score: 8
attempted: 10
timestamp: 2026-03-11
Technologies Used
Cloud Services

Amazon EC2

Amazon API Gateway

AWS Lambda

Amazon DynamoDB

AWS IAM

Development

HTML

CSS

JavaScript

Server

Nginx

RHEL Linux
