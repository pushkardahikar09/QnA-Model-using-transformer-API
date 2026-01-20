# QnA Model Using Hugging Face Transformer API

📖 Project Overview

This project implements a Question Answering (QnA) system using a Hugging Face pre-trained Transformer model.
The system is designed so that a fixed context is embedded in the code, while users can ask multiple questions at runtime through a continuous interaction loop.

The model extracts precise answers from the given context using deep learning-based natural language understanding.

# Key Features

✅ Uses Hugging Face pre-trained DistilBERT model

✅ Continuous QnA loop (ask unlimited questions)

✅ Runtime user interaction

✅ Clean and optimized output formatting

✅ Simple and interview-ready implementation

# Model Used

Model Name: distilbert-base-cased-distilled-squad

Type: Pre-trained Transformer

Fine-tuned On: Stanford Question Answering Dataset (SQuAD)

Source: Hugging Face Model Hub

# Usage

The context is predefined inside the code.

The user can ask questions continuously at runtime.

Type exit to stop the program.

# How It Works

Loads a Hugging Face pre-trained transformer model using the pipeline API.

Stores a fixed contextual paragraph in the application.

Accepts user questions dynamically.

Extracts the most relevant answer span from the context.

Displays the answer with a confidence score.

# Challenges Addressed

Integrating a pre-trained transformer pipeline

Handling runtime user queries

Optimizing output formatting

Ensuring efficient inference in a continuous loop

<img width="877" height="414" alt="image" src="https://github.com/user-attachments/assets/569e2646-1232-46a9-8d29-9fd8b6336f13" />

