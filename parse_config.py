import yaml
import re
import os

def main():
    # 读取配置文件
    with open('marimo-team__marimo-6887/marimo-team__marimo-6887.yml', 'r') as f:
        data = yaml.safe_load(f)
    
    # 提取原始字段
    instance_id = data.get('instance_id', '')
    repo_full = data.get('repo', '')
    base_commit = data.get('base_commit', '')
    pr_url = data.get('pr_url', '')
    
    # 处理 REPO_DIR：从 "owner/repo" 中提取 "repo"
    repo_dir = repo_full.split('/')[-1] if '/' in repo_full else repo_full
    
    # 处理 REPO_URL：将 PR URL 转换为 Git URL
    if pr_url and '/pull/' in pr_url:
        repo_url = re.sub(r'/pull/\d+', '.git', pr_url)
    else:
        repo_url = pr_url
    
    # 写入环境变量
    with open(os.environ['GITHUB_ENV'], 'a') as env_file:
        env_file.write(f"INSTANCE_DIR={instance_id}\n")
        env_file.write(f"REPO_DIR={repo_dir}\n")
        env_file.write(f"base_commit={base_commit}\n")
        env_file.write(f"REPO_URL={repo_url}\n")
    
    # 输出调试信息
    print("环境变量设置完成:")
    print(f"INSTANCE_DIR: {instance_id}")
    print(f"REPO_FULL: {repo_full}")
    print(f"REPO_DIR: {repo_dir}")
    print(f"base_commit: {base_commit}")
    print(f"PR_URL: {pr_url}")
    print(f"REPO_URL: {repo_url}")

if __name__ == "__main__":
    main()