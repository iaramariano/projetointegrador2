#!/bin/sh
# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

until nc -z "$host" 3306; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - running migrations"
# Adicionamos esta linha para rodar a migração
python manage.py migrate

>&2 echo "Migrations complete - starting server"
# O 'exec' passa o controle total para o comando final (gunicorn)
# Isso garante que gunicorn se torne o processo principal que mantém o contêiner vivo.
exec $cmd
