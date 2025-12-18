#!/bin/bash
set -e

# 创建 testbed 目录
mkdir -p /testbed

echo ">>> Cloning repository: llamastack/llama-stack..."
# Clone 代码到 /testbed/repo_name
git clone https://github.com/llamastack/llama-stack.git /testbed/llama-stack

echo ">>> Checking out commit: 167143131053c8de6ea620a83ebdec41c0b24e50..."
cd /testbed/llama-stack
git checkout 167143131053c8de6ea620a83ebdec41c0b24e50

echo ">>> Repository setup complete."
