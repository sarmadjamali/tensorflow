from tokenize_fn import tokenize_sentences,tokenize_sentences1
from add_fn import add
from subtract_fn import subtract
from multiply_fn import multiply
from basicModel import runbasicModel

def run_prompt(prompt):
    if prompt == "1":
        tokenize_sentences()
        # tokenize_sentences1()
    elif prompt == "1.1":
        runbasicModel()
    elif prompt == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)
    elif prompt == "3":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        subtract(a, b)
    elif prompt == "4":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        multiply(a, b)
    else:
        print("Invalid prompt. Use 1–4.")

if __name__ == "__main__":
    runbasicModel()
    print("Choose a prompt:")
    print("1 - Tokenize Sentences")
    print("2 - Addition")
    print("3 - Subtraction")
    print("4 - Multiplication")
    
    user_input = input("Enter prompt number: ")
    run_prompt(user_input)
