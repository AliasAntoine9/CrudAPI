FROM alpine:latest

RUN apk add --no-cache sqlite

WORKDIR /home/sqlite

COPY scripts/sqlite/create_database.sql ./create_database.sql

RUN sqlite3 crud_database.db < create_database.sql

# Expose a volume to be able to access at crud_database.db file from outside the container
VOLUME ["/home/sqlite"]

# Keep container alive after initialization
CMD ["tail", "-f", "/dev/null"]