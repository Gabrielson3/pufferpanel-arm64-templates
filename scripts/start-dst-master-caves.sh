#!/usr/bin/env bash
# Experimental DST Master+Caves supervisor for Linux ARM64/Box64.
set -Eeuo pipefail
ROOT=$(cd -- "$(dirname -- "$0")" && pwd -P)
CLUSTER_DIR="$ROOT/DoNotStarveTogether/DontStarveTogetherServer"
BIN_DIR="$ROOT/bin64"
BIN="$BIN_DIR/dontstarve_dedicated_server_nullrenderer_x64"
BOX64=$(command -v box64 || true)

if [[ -z "$BOX64" || ! -x "$BOX64" ]]; then echo "Box64 is not available in PATH" >&2; exit 127; fi
if [[ ! -f "$BIN" ]]; then echo "DST x86_64 dedicated server binary was not found" >&2; exit 127; fi
if [[ ! -s "$CLUSTER_DIR/cluster_token.txt" ]]; then echo "Missing Klei cluster token" >&2; exit 2; fi
if [[ ! -f "$CLUSTER_DIR/cluster.ini" ]]; then echo "Missing cluster.ini" >&2; exit 2; fi

if grep -q '^cluster_key = __AUTO_KEY__$' "$CLUSTER_DIR/cluster.ini"; then
  KEY=$(od -An -N16 -tx1 /dev/urandom | tr -d ' \n')
  sed -i "s/^cluster_key = __AUTO_KEY__$/cluster_key = $KEY/" "$CLUSTER_DIR/cluster.ini"
fi

# DST expects a bin64 working directory for its data/ lookup.
cd "$BIN_DIR"
MASTER_PID=''
CAVES_PID=''
stop_shards() {
  trap - INT TERM EXIT
  [[ -z "$CAVES_PID" ]] || kill -TERM "$CAVES_PID" 2>/dev/null || true
  [[ -z "$MASTER_PID" ]] || kill -TERM "$MASTER_PID" 2>/dev/null || true
  [[ -z "$CAVES_PID" ]] || wait "$CAVES_PID" 2>/dev/null || true
  [[ -z "$MASTER_PID" ]] || wait "$MASTER_PID" 2>/dev/null || true
}
trap stop_shards INT TERM EXIT

"$BOX64" "$BIN" -persistent_storage_root "$ROOT" -console -cluster DontStarveTogetherServer -shard Master &
MASTER_PID=$!
sleep 10
if ! kill -0 "$MASTER_PID" 2>/dev/null; then echo "Master exited before Caves startup" >&2; exit 1; fi

"$BOX64" "$BIN" -persistent_storage_root "$ROOT" -console -cluster DontStarveTogetherServer -shard Caves &
CAVES_PID=$!
set +e
wait -n "$MASTER_PID" "$CAVES_PID"
STATUS=$?
set -e
exit "$STATUS"
