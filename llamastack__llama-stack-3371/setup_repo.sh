#!/bin/bash
set -e

# 创建 testbed 目录
mkdir -p /testbed

echo ">>> Cloning repository: llamastack/llama-stack..."
# Clone 代码到 /testbed/repo_name
git clone https://github.com/llamastack/llama-stack.git /testbed/llama-stack

echo ">>> Checking out commit: b6cb8178976b941a1fdb3894b00bd13eaca91561..."
cd /testbed/llama-stack
git checkout b6cb8178976b941a1fdb3894b00bd13eaca91561

echo ">>> Repository setup complete."
