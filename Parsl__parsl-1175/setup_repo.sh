#!/bin/bash
# 遇到任何错误则立即退出
set -e

mkdir -p /testbed
git clone https://github.com/Parsl/parsl.git /testbed/parsl
cd /testbed/parsl
git checkout "fe6d47e0774935e82e14f4cb8123c795f24c627f"
cd ..

