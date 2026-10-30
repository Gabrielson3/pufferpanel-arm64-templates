#!/usr/bin/env bash
# Valheim launcher for PufferPanel on ARM64 with Box64.
# PufferPanel provides values through environment variables so whitespace and
# quotation marks are passed as arguments, not parsed as shell syntax.
set -Eeuo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

if [[ ! -f ./valheim_server.x86_64 ]]; then
  echo 'Valheim server executable is missing; install the server first.' >&2
  exit 127
fi
if ! command -v box64 >/dev/null 2>&1; then
  echo 'Box64 is not available on PATH.' >&2
  exit 127
fi
: "${VH_NAME:?Missing server name}"
: "${VH_WORLD:?Missing world name}"
: "${VH_PASSWORD:?Missing server password}"
: "${VH_PORT:?Missing UDP port}"
: "${VH_PUBLIC:?Missing public-listing flag}"
: "${VH_PRESET:?Missing world preset}"
: "${VH_RESOURCES:?Missing resource modifier}"
if (( ${#VH_PASSWORD} < 5 )); then
  echo 'Server password must contain at least five characters.' >&2
  exit 2
fi

export LD_LIBRARY_PATH="./linux64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
# Box64 can log all command arguments, including the password. Keep it quiet
# by default; admins may override BOX64_LOG for private troubleshooting.
export BOX64_LOG="${BOX64_LOG:-0}"
args=(
  -nographics -batchmode
  -name "$VH_NAME"
  -port "$VH_PORT"
  -world "$VH_WORLD"
  -password "$VH_PASSWORD"
  -public "$VH_PUBLIC"
  -preset "$VH_PRESET"
)
if [[ "$VH_RESOURCES" != 'default' ]]; then
  args+=(-modifier resources "$VH_RESOURCES")
fi
exec box64 ./valheim_server.x86_64 "${args[@]}"
