#! /usr/bin/env python3
import os
import requests

# List all .txt files under /data/feedback directory
feedback_files = [file for file in os.listdir("./") if file.endswith(".txt")]

# Create a dictionary to store feedback data
feedback_data = []

# Traverse over each file and extract data
for file in feedback_files:
    with open(f"{file}", "r") as f:
        lines = f.readlines()
        feedback = {
            "title": lines[0].strip(),
            "name": lines[1].strip(),
            "date": lines[2].strip(),
            "feedback": " ".join(lines[3:]).strip()
        }
        feedback_data.append(feedback)

#print(feedback_data)
# POST the dictionary to the company's website
for index, feedback in enumerate(feedback_data):
        # feedback["id"] = index +5
        print(feedback)
        try:
            url = "http://34.135.231.200:80/feedback"  # Replace <corpweb-external-IP> w$
            response = requests.post(url, data=feedback)
            print(response.text)
        except Exception as e:
             print(e)   