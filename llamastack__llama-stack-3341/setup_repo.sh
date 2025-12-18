#!/bin/bash
set -e

# 创建 testbed 目录
mkdir -p /testbed

echo ">>> Cloning repository: llamastack/llama-stack..."
# Clone 代码到 /testbed/repo_name
git clone https://github.com/llamastack/llama-stack.git /testbed/llama-stack

echo ">>> Checking out commit: 426cac078b75e6f52dff2c16240989fd924a1f11..."
cd /testbed/llama-stack
git checkout 426cac078b75e6f52dff2c16240989fd924a1f11

echo ">>> Repository setup complete."
