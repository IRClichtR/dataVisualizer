#!/bin/bash

db_path=$DB_PATH

if [ -e "$db_path" ]; then
  echo "db already copied"
else
  echo "Initializing database..."
  python3 init_data.py 
fi 

# Set server to poduction mode

echo "Launching production server... "
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:8000 dataVisualizer:app

