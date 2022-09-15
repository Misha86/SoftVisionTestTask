import os
from decouple import config


def main():
    os.system(
        f"PGPASSWORD='{config('POSTGRES_PASSWORD')}' pg_dump -h localhost "
        f"-U {config('POSTGRES_USER')} -d {config('POSTGRES_DB')} > {config('POSTGRES_DB')}_db.sql"
    )


if __name__ == "__main__":
    main()
