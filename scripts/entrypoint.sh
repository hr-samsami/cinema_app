#!bin/sh

echo "========================================================================="
echo "DATABASE MIGRATION"
echo "========================================================================="

alembic upgrade head

export PORT=${PORT:-8000}
export HOST=${WORKERS:-2}

echo "========================================================================="
echo "R U N N I N G  A P P  . . ."
echo "========================================================================="

uvicorn app.main:app \
    --host 0.0.0.0 \
    --port ${PORT} \
    --workers ${WORKERS} \
    --header server:zws \
    --header "Strict-Transport-Security:max-age=15552000; includeSubDomains; preload" \
    --forwarded-allow-ips='*' \
    --proxy-headers
