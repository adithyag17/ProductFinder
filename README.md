# Product Finders Solution

## Problem Statement 1

This project is a solution for Problem Statement 1 of the G2 Internship Hackathon. The goal is to create a product finder tool that helps users quickly locate products based on various criteria.

## Technologies Used

- **Python Libraries:** Scrapy, MechanicalSoup
- **Automation:** Jenkins
- **Containerization:** Docker

## Entrepreneurial Aspect

As part of this solution, we have identified the top 3 competitors to G2 in their domain of software. These competitors are:

1. SoftwareAdvice
2. TrustRadius
3. SaaSworthy

## Data Collection and Processing

We have scraped around 25 to 30 thousand product names from each competitor's website using Python libraries like Scrapy and MechanicalSoup. After collecting this data, we cross-referenced it with the G2 API to validate and enhance our results. The final output is dumped into a CSV file for further analysis.

## Solution Overview

While our initial solution may seem brute-force due to the large volume of products being scraped, it offers exceptional accuracy. To make the solution lightweight and scalable, we have dockerized the three scrapers, creating separate lightweight containers for each competitor's data collection process.

## Dockerization

By dockerizing the scrapers and building their images, we ensure portability and easy deployment. Each scraper runs in its own container, maintaining isolation and efficiency.

## Job Scheduling

To tackle the problem of scheduling timely job runs, we have employed Jenkins as an industrially relevant server. Jenkins automates the process of running these scraper solutions at regular intervals, ensuring that our data remains up-to-date and relevant. Jobs are scheduled to run every week for consistent and reliable data collection.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/product-finders.git`
2. Install Docker and Jenkins on your system.
3. Build Docker images for each scraper: `docker build -t scraper1 .`, `docker build -t scraper2 .`, `docker build -t scraper3 .`
4. Run Docker containers for each scraper: `docker run -d scraper1`, `docker run -d scraper2`, `docker run -d scraper3`
5. Configure Jenkins to schedule and run the scraper jobs as needed.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Be sure to follow the project's coding style and guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
