#!/usr/bin/env bash

# собираем импорты из кода
imports=$(grep -rhoP '^import \K\w+|^from \K\w+' src | sort -u)

# читаем зависимости
reqs=$(cut -d= -f1 requirements.txt | sort -u)

echo "== Missing dependencies =="
for imp in $imports; do
    if ! echo "$reqs" | grep -qx "$imp"; then
        echo "$imp"
    fi
done

echo "== Unused dependencies =="
for req in $reqs; do
    if ! echo "$imports" | grep -qx "$req"; then
        echo "$req"
    fi
done