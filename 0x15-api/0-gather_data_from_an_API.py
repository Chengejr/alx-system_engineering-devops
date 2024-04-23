#!/usr/bin/python3

"""
This script fetches information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee.

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
        
        # Filter completed tasks
        completed_tasks = [task for task in todos if task.get('completed')]
        
        # Calculate progress
        total_tasks = len(todos)
        done_tasks = len(completed_tasks)
        
        # Get employee name
        employee_name = todos[0].get('username')
        
        # Display progress
        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task.get('title')}")
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

