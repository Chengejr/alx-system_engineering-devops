Duration: The outage occurred from 12:00 PM to 2:30 PM on May 10, 2024 (UTC).
Impact: The outage affected the login service, rendering it inaccessible to 90% of users. Users experienced login failures and slow response times.
Root Cause: The issue stemmed from a misconfigured firewall rule blocking incoming traffic to the login service.
Timeline:

12:00 PM (UTC): Issue detected through monitoring alerts indicating a spike in failed login attempts.
12:05 PM: Engineering team notified of the issue.
12:15 PM: Investigation begins, focusing on backend services and database connectivity.
12:30 PM: Assumption made that the database server might be experiencing issues due to high load.
12:45 PM: Database team engaged to investigate potential database issues.
1:00 PM: Further investigation reveals no issues with the database server.
1:15 PM: Network team investigates network configuration and firewall rules.
1:30 PM: Misconfigured firewall rule blocking incoming traffic identified as the root cause.
1:45 PM: Incident escalated to network team for immediate resolution.
2:30 PM: Issue resolved by updating firewall rules to allow traffic to the login service.
Root Cause and Resolution:

Root Cause: The misconfigured firewall rule was blocking incoming traffic to the login service, causing login failures and slow response times.
Resolution: The issue was resolved by updating the firewall rules to allow incoming traffic to the login service, restoring normal functionality.
Corrective and Preventative Measures:

Improvements/Fixes:
Regular audits of firewall rules to identify and rectify misconfigurations.
Implementing automated testing for firewall rule changes to prevent similar issues in the future.
Tasks to Address the Issue:
Conduct a thorough review of all firewall rules to ensure they align with security policies.
Implement automated monitoring for firewall rule changes to detect misconfigurations promptly.
Provide additional training to team members on firewall management best practices.
By addressing these corrective and preventative measures, we aim to minimize the risk of similar outages occurring in the future and ensure the continued reliability of our services.
