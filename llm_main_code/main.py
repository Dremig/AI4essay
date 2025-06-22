from pdf_reader import extract_pdf_content, extract_online_pdf
from llm_handler import process
import os


def main():
    print("============")
    print("Welcome! This is the program for extracting pdf content and using llm to process it.")
    print("First , you input a file path or url, remember to use the correct format(for examle , the url should start with http or https).")
    print("Then , you input your choice. You have 4 choices :")
    print("A: Large model dialogue based on these documents;")
    print("B: Provide a summary of a specific document;")
    print("C: Provide the translation of a specific document;")
    print("D: Provide a literature review based on a specified range of documents.")
    print("If you want to stop entering the file, just type 'done' to stop.")
    print("============")
    os.system("mkdir -p ./files")
    os.system("mkdir -p ./D-choice-list")
    file_list = []
    choice = input("please input choice:")
    while 1:
        file = input("please input pdf file path or url:")
        if file == "done":
            break
        else:
            file_list.append(file)
        
    for i in range(len(file_list)):
        if file_list[i].startswith("http"):
            temp = extract_online_pdf(file_list[i])
            os.system("touch ./files/{}.txt".format(i))
            with open(f'./files/{i}.txt', 'w') as f:
                f.write(temp)
            
        else:
            temp = extract_pdf_content(file_list[i])
            os.system("touch ./files/{}.txt".format(i))
            with open(f'./files/{i}.txt', 'w') as f:
                f.write(temp)


    if choice == "A":
        process('no', choice, "./files")
    elif choice == "B" or choice == "C":
        index = input("please input the index of the document you want to summarize or translate:")
        process(f'./files/{index}.txt', choice, "no")
    elif choice == "D":
        start = input("please input the start index of the documents you want to summarize:")
        end = input("please input the end index of the documents you want to summarize:")
        if "all" in start or "all" in end:
            start = "0"
            end = str(len(file_list) - 1)
        for i in range(int(start), int(end) + 1):
            with open(f'./files/{i}.txt', 'r') as f:
                text = f.read()
            os.system("echo {} > ./D-choice-list/{}.txt".format(text, i))

        process("no", choice, "./D-choice-list")
    

main()


