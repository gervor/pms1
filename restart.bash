#!/bin/bash

# Define your module name and database
MODULE_NAME="pms1"
DB_NAME="odoo"

# Restart the Odoo Docker container
echo "Restarting Odoo container..."
docker restart odoo_zadego17-web-1

# Wait for a few seconds to ensure Odoo is up
echo "Waiting for Odoo to start..."
sleep 5

# Run Odoo shell commands
echo "Upgrading module: $MODULE_NAME"
docker exec odoo_zadego17-web-1 odoo shell -d $DB_NAME -c /etc/odoo/odoo.conf --no-http -i $MODULE_NAME --stop-after-init

# Follow the logs of the container
echo "Following the logs of the container..."
docker logs -f odoo_zadego17-web-1
