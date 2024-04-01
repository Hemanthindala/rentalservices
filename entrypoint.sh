#!/bin/ash

echo "Apply migrations"

# Update the working directory
cd /home/application/rentalservices

# Check if manage.py exists
if [ -f "manage.py" ]; then
    # Apply migrations and run the server
    python3 manage.py migrate
    python3 manage.py runserver 0.0.0.0:8000
else
    echo "Error: manage.py file not found in /home/application/rentalservices"
fi

exec "$@"
