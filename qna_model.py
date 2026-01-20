from transformers import pipeline


qa_pipeline = pipeline(
    task="question-answering",
    model="distilbert-base-cased-distilled-squad"
)


CONTEXT = """
Artificial Intelligence (AI) is a branch of computer science that focuses on 
creating systems capable of performing tasks that normally require human 
intelligence. These tasks include learning, reasoning, problem-solving, 
perception, and understanding natural language.
"""

print(" QnA System is ready!")
print("Type 'exit' to stop.\n")


while True:
    question = input("Ask a question: ")

    
    if question.lower() == "exit":
        print("Exiting QnA system. Goodbye!")
        break

   
    result = qa_pipeline(
        question=question,
        context=CONTEXT
    )

   
    print("\nAnswer:", result["answer"])
    print("Confidence Score:", round(result["score"], 3))
    print("-" * 40)
