def calculate(question):
    question = question.replace('What is ', '') \
                       .replace('?', '') \
                       .replace("plus", "+") \
                       .replace("minus", "-") \
                       .replace("multiplied by", "*") \
                       .replace("divided by", "/")
    try:
        return eval(question)
    except SyntaxError:
        raise ValueError("Question systax error")
