**place the groq api and openai api in .env file.

Email Sender Project
This project demonstrates how to send emails based on user prompts using Langraph, FlaskMail, Mailtrap, Groq API, and ChatGPT API. The emails are generated and sent according to the user's instructions, leveraging large language models (LLMs) to create the email content.

Problem Statement
The goal is to send an email with a generated body based on the user's prompt using LLM Agents.

Features
Create an API to send emails:

Fields: subject, body, sender, recipient
Technology: Flask, FlaskMail
LLM Setup:

Example Prompt: "Send an email to manangupta@gmail.com for Leave Approval"

Steps:

Extract the recipient email address from the prompt.
Create the email body and subject based on the context.
Responses:

Extracted recipient email:xxxx@gmail.com
Generated email content (subject and body) for the leave approval request.
Email Sending Workflow:

Format the output in the specified JSON structure.
Use the formatted JSON to call the Flask API and send the email.
API Details
Endpoint: /send-email
Method: POST

Request Parameters:

subject (string): Subject of the email.
body (string): Body of the email.
sender (string): Sender's email address.
recipient (string): Recipient's email address.
