# Product Finders Solution

## Problem Statement 1

This project is a solution for Problem Statement 1 of the G2 Internship Hackathon. The goal is to create a tool that helps users quickly scrape software products which are currently not in the g2 space.

## Technologies Used

- **Python Libraries:** Scrapy, MechanicalSoup
- **Automation:** Jenkins
- - **Automation:**Shell Script
- **Containerization:** Docker

## Entrepreneurial Aspect

As part of this solution, we have identified the top 3 competitors to G2 in their domain of software. These competitors are:

1. SoftwareAdvice
2. TrustRadius
3. SaaSworthy

## Data Collection and Processing

We have scraped around 25 to 30 thousand product names from each competitor's website using Python libraries like Scrapy and MechanicalSoup. After collecting this data, we cross-referenced it with the G2 API to validate and enhance our results. The final output is dumped into a CSV file for further analysis.

## Solution Overview

While our initial solution may seem brute-force due to the large volume of products being scraped, it offers exceptional accuracy. To make the solution lightweight and scalable, we have dockerized the three scrapers, creating separate lightweight containers for each competitor's data collection process which will in turn run the scrapers parallely.

## Dockerization

By dockerizing the scrapers and building their images, we ensure portability and easy deployment. Each scraper runs in its own container, maintaining isolation and efficiency.

## Job Scheduling

To tackle the problem of scheduling timely job runs, we have employed Jenkins as an industrially relevant server. Jenkins automates the process of running these scraper solutions at regular intervals, ensuring that our data remains up-to-date and relevant. Jobs are scheduled to run every week for consistent and reliable data collection.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
