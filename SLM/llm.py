from transformers import pipeline

messages = [
    {"role": "user", "content": "who are you"},
]
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
generated_text = pipe(messages, max_length=150, num_return_sequences=1)

# Display only the assistant's response
response = generated_text[0]['generated_text']
print(response)
