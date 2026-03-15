from openai import OpenAI

# 你已经填写好 API Key
client = OpenAI(
    api_key="sk-c81010b47faa4b0eb23adf5fd9b8dd31",
    base_url="https://api.deepseek.com"
)

def chat_with_deepseek(user_input):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(" DeepSeek 聊天机器人已启动，输入 quit 退出")
    while True:
        user_msg = input("你：")
        if user_msg.lower() == "quit":
            print(" 再见！")
            break
        reply = chat_with_deepseek(user_msg)
        print("DeepSeek：" + reply)