#!/usr/bin/env bash
set -euo pipefail

SERVICE_NAME="${SERVICE_NAME:-alphaai}"
PUBLISHED_PORT="${PUBLISHED_PORT:-8087}"
TARGET_NODE="${TARGET_NODE:-alphahs}"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAMP="$(date +%Y%m%d%H%M%S)"

INDEX_CONFIG="alphaai_index_html_${STAMP}"
TIMELINE_CONFIG="alphaai_timeline_json_${STAMP}"
NGINX_CONFIG="alphaai_nginx_conf_${STAMP}"

docker config create "${INDEX_CONFIG}" "${REPO_DIR}/index.html" >/dev/null
docker config create "${TIMELINE_CONFIG}" "${REPO_DIR}/timeline.json" >/dev/null
docker config create "${NGINX_CONFIG}" "${REPO_DIR}/nginx.conf" >/dev/null

if docker service inspect "${SERVICE_NAME}" >/dev/null 2>&1; then
  docker service rm "${SERVICE_NAME}" >/dev/null
  while docker service inspect "${SERVICE_NAME}" >/dev/null 2>&1; do
    sleep 1
  done
fi

docker service create \
  --name "${SERVICE_NAME}" \
  --publish "published=${PUBLISHED_PORT},target=80,protocol=tcp,mode=host" \
  --constraint "node.hostname==${TARGET_NODE}" \
  --config "source=${INDEX_CONFIG},target=/usr/share/nginx/html/index.html" \
  --config "source=${TIMELINE_CONFIG},target=/usr/share/nginx/html/timeline.json" \
  --config "source=${NGINX_CONFIG},target=/etc/nginx/conf.d/default.conf" \
  nginx:alpine >/dev/null

echo "Deployed ${SERVICE_NAME} on port ${PUBLISHED_PORT}"
