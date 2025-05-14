import openai

openai.api_key = "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"

def answer_questions(input_text):
    completion = openai.Completion()
    response = completion.create(
        model="text-davinci-002",
        prompt=input_text,
        temperature=0.5,
        max_tokens=100,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    return answer

while True:
    ques = input("Ask a question=>")
    if ques.lower() == 'exit':
        break
    print(answer_questions(ques))
