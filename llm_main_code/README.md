This file is used to tell you how to use my project.

## Python Version And Packet Dependencies

Python 3.10.12

use `pip3 install -r requirements.txt` to install the dependencies.



## How to use

run `python3 main.py` to start the project.

Fisrt you need to enter a choice in "A" / "B" / "C" / "D".

+ A: Large model dialogue based on these documents
+ B: Provide a summary of a specific document
+ C：Provide the translation of a specific document
+ D: Provide a literature review based on a specified range of documents

Other choice are not allowed.

Then you need to enter the document path or url, enter `done` to stop the files input.

If you enter B or C, you need to enter the index of the document you want to handle.

If you enter D, you need to enter the start index and end index of the document you want to handle. Enter `all` in start or end to use all the files.

Then the result will be stored as "response.txt".