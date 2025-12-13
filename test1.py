import requests

# 接口基础地址
BASE_URL = "https://jsonplaceholder.typicode.com"


# 1. 获取所有文章（GET请求）
def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    print("1. 获取所有文章：")
    print(f"状态码：{response.status_code}")
    print(f"前2条数据：{response.json()[:2]}\n")


# 2. 创建新文章（POST请求）
def test_create_post():
    data = {"title": "我的测试文章", "body": "这是接口自动化测试内容", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    print("2. 创建新文章：")
    print(f"状态码：{response.status_code}")
    print(f"创建结果：{response.json()}\n")


# 3. 更新文章（PUT请求）
def test_update_post():
    post_id = 1
    data = {"title": "更新后的标题", "body": "更新后的内容", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    print("3. 更新文章：")
    print(f"状态码：{response.status_code}")
    print(f"更新结果：{response.json()}\n")


# 4. 删除文章（DELETE请求）
def test_delete_post():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    print("4. 删除文章：")
    print(f"状态码：{response.status_code}")
    print(f"删除结果：{response.json()}\n")


# 执行所有测试
if __name__ == "__main__":
    test_get_all_posts()
    test_create_post()
    test_update_post()
    test_delete_post()
