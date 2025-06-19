#!/usr/bin/env bash
set -euo pipefail

role_dirs=$(git ls-tree -d --name-only HEAD roles/)

for role in $role_dirs; do
  echo "Checking docsible in: $role"
  docsible --role "$role" --no-backup
done

git diff --exit-code
