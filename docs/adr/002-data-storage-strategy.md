# ADR-002: Data Storage Strategy

## Status
Accepted

## Context
The ai-codemap project requires a robust data storage strategy to handle user data, codemaps, and AI model outputs. We need to balance data consistency, availability, and performance. Our tech stack includes Python, FastAPI, PostgreSQL, Redis, and Docker.

## Decision
We decided to use a combination of PostgreSQL for relational data and Redis for caching and real-time data storage. PostgreSQL will store user information, codemap metadata, and other relational data, while Redis will store frequently accessed data, such as codemap contents and AI model outputs.

## Alternatives Considered
* **Relational database only**: Using only PostgreSQL would provide strong data consistency but may lead to performance issues with frequent reads and writes. 
* **NoSQL database**: Using a NoSQL database like MongoDB could provide flexibility and scalability but may require significant changes to our existing tech stack and introduce data consistency issues.

## Consequences
The chosen approach offers a balance between data consistency and performance. Positive consequences include improved data retrieval performance and reduced load on the relational database. Negative consequences include increased complexity due to the use of multiple storage systems and potential caching inconsistencies.