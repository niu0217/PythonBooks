from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
language_suevey = AnonymousSurvey(question)

# 显示问题并存储答案
language_suevey.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_suevey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
language_suevey.show_results()
