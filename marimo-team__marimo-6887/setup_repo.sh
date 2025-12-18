#!/bin/bash
set -e

# 创建 testbed 目录
mkdir -p /testbed

echo ">>> Cloning repository: marimo-team/marimo..."
# Clone 代码到 /testbed/repo_name
git clone https://github.com/marimo-team/marimo.git /testbed/marimo

echo ">>> Checking out commit: 12b174df72d8731ee62f6c90d108711db5719ebf..."
cd /testbed/marimo
git checkout 12b174df72d8731ee62f6c90d108711db5719ebf

echo ">>> Repository setup complete."
