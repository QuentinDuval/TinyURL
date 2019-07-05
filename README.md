# Tiny URL

An example of implementation of the Tiny URL service.

## Requirements

The service requires the following services to run beside it:

- Postgres: to store the associations tiny URL to full URL
- Redis: to cache the results of database fetches
- Zookeeper: to handle the distributed allocation of identifiers used to created tiny URL
