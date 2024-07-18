from langgraph.graph import Graph

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()

def send_email(email_obj):
    url = 'http://127.0.0.1:5000/'
    print(json.loads(email_obj))
    x = requests.post(url, json = json.loads(email_obj))
    print(x)
    print(x.text)

os.environ['GROQ_API_KEY'] = os.environ.get('GROQ_API_KEY')
model = ChatGroq(model="mixtral-8x7b-32768")


output_format = {
    "subject":  '<Generate the subject and replace here>',
    "message": '<Generate the message and replace here>',
    "sender": '<Extract from the given query and replace>',
    "recipients": '<Extract from the given query and replace>'
}
def function_1(input_1):
    complete_query = "Your task is to provide only the data in the given json format on the basis of the user query. \
        Nothing more, just the data. Make sure the data is in json format having the keys and values in double quotes and no escape. Following is the user query: " + input_1 + \
        "Output format - " + str(output_format)
    print(str(complete_query))

    response = model.invoke(str(complete_query))

    print(response.content)
    return response.content

def function_2(input_2):
    print('Before sending email with data :: ', input_2)
    return send_email(input_2)

# Define a Langchain graph
workflow = Graph()

#calling node 1 as agent
workflow.add_node("agent", function_1)
workflow.add_node("mail_sender", function_2)

workflow.add_edge('agent', 'mail_sender')

workflow.set_entry_point("agent")
workflow.set_finish_point("mail_sender")

app = workflow.compile()

recipients = app.invoke("Can you generate an email for an offer going of 50% off on all items on Zomato and send this email to jkmarpoo@gmail.com using the relevant subject and sender as info@zomato.com.")
