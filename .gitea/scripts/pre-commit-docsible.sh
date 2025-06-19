#!/usr/bin/env bash
set -euo pipefail

role_dirs=$(git ls-tree -d --name-only HEAD roles/)

checked_roles=()

for role in $role_dirs; do
  echo "Running docsible on $role"
  docsible --role "$role" --no-backup
  checked_roles+=("$role")
done

echo "Checking for diffs in updated roles..."
git diff --exit-code -- ${checked_roles[@]}
