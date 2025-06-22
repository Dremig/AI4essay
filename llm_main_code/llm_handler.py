import os
import openai







# different prompt base on different choice
def choice_to_prompt(choice):
    choice_range = ["A","B","C","D"]
    if choice not in choice_range:
        return "Invalid choice"
    prompt1 = "你是一位专业的文献阅读者，上面我已经传入一段多个文献的内容，不同文献之间已使用'====================='进行分割，请你使用中文给出基于这些文献的大模型对话。"
    prompt2 = "你是一位专业的文献概括者，上面我已经传入一段文献的内容，请你使用中文对该文献文件进行 summary。"
    prompt3 = "你是一位专业的文献翻译者，上面我已经传入一段英文文献内容，请你对该文献文件进行翻译为中文的工作。如果该文献内容是中文，请你仅需要返回'文献已是中文'即可。"
    prompt4 = "你是一位专业的文献综述学者，上面我已经传入一段多个文献的内容，不同文献之间将使用'====================='进行分割，请你使用中文对这些文献进行综述。"
    if choice == "A":
        return prompt1
    elif choice == "B":
        return prompt2
    elif choice == "C":
        return prompt3
    else:
        return prompt4




# Function to process each directory and file
def process(input_file, choice, input_file_list):
    prompt = choice_to_prompt(choice)
    content = ""
    if input_file_list=="no":
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # print(content)

    elif input_file == "no":
        directory = input_file_list
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content += "=====================\n\n"
                    content += f.read()  # 读取文件内容
                    content += "=====================\n\n"

    
    
    message =  content + "\n" + prompt   

    with open("message.txt", "w") as f:
        f.write(message)

    # print(message)

    from openai import OpenAI

    client = OpenAI(api_key="sk-9e687484fa52498a9af6d59d4fee8c5f", base_url="https://api.deepseek.com")
    try:
        # message = "请输出：世界你好！"
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": message},
            ],
            stream=False
        )


        content = response.choices[0].message.content

        print(content)

        if content:
            print("Your answer:")
            final_response = content
            os.system("touch response.txt")
            with open("response.txt", "w") as f:
                f.write(final_response)
        else:
            print("No data received!")
            final_response = "No result found"

    except openai.BadRequestError as e:
        print(f"OpenAI API error: {e}")









