#!/usr/bin/env bash

expected_path="src/test/resources/samples/measurements.txt.md5sum"
actual_path="measurements.txt.md5sum.tmp"
measurements_path="src/test/resources/samples/measurements.txt"

md5sum "$measurements_path" >"$actual_path"
diff "$expected_path" "$actual_path"
rm "$actual_path"
