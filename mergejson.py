import json


def merge_json_files():
    # 读取result.json文件
    with open(r'results.json', 'r', encoding='utf-8') as f:
        result_data = json.load(f)

    # 读取INSTANCE_DIR文件
    with open(r'INSTANCE_DIR.json', 'r', encoding='utf-8') as f:
        pygithub_data = json.load(f)

    # 提取需要的字段
    fail_to_pass = result_data.get('INSTANCE_DIR', {}).get('tests_status', {}).get('FAIL_TO_PASS',{}).get('success',[])
    pass_to_pass = result_data.get('INSTANCE_DIR', {}).get('tests_status', {}).get('PASS_TO_PASS',{}).get('success',[])

    # 将字段追加到PyGithub数据中
    pygithub_data['FAIL_TO_PASS'] = fail_to_pass
    pygithub_data['PASS_TO_PASS'] = pass_to_pass
    pygithub_data['language'] = "Python"
    pygithub_data['content_category'] = ["工具"]

    # 写回文件
    with open(r'INSTANCE_DIR.json', 'w', encoding='utf-8') as f:
        json.dump(pygithub_data, f, indent=4, ensure_ascii=False)

    #print("字段已成功追加到INSTANCE_DIR.json文件中".encode('utf-8').decode('utf-8'))


if __name__ == "__main__":
    merge_json_files()