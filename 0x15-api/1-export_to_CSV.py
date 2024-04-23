#!/usr/bin/python3

"""
This script fetches information about an employee's TODO list progress
using a REST API and exports it to a CSV file.
"""

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches TODO list progress for a given employee and exports it to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # API endpoint URL
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Make a GET request to fetch TODO data
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        todos = response.json()
        
        # Create CSV file name
        csv_filename = f"{employee_id}.csv"
        
        # Open CSV file for writing
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # Write CSV header
            writer.writeheader()
            
            # Write task information to CSV file
            for task in todos:
                writer.writerow({
                    'USER_ID': employee_id,
                    'USERNAME': task.get('username'),
                    'TASK_COMPLETED_STATUS': task.get('completed'),
                    'TASK_TITLE': task.get('title')
                })
        
        print(f"Task information exported to {csv_filename}")
    else:
        print("Failed to fetch data from the API.")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    # Extract employee ID from command line argument
    employee_id = sys.argv[1]
    
    # Call the function with the provided employee ID
    get_employee_todo_progress(employee_id)
