#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

python << END
import os
import sys
import time
import psycopg2

suggest_unrecoverable_after = 30
start = time.time()

while True:
    try:
        psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
        )
        break
    except psycopg2.OperationalError as error:
        sys.stderr.write("Waiting for postgres...\n")
        if time.time() - start > suggest_unrecoverable_after:
            sys.stderr.write(
                f"Postgres is taking too long to start up; aborting error: '{error}'\n"
            )
            sys.exit(1)
        time.sleep(3)
END

echo >&2 "Postgres is up - continuing"
exec "$@"
