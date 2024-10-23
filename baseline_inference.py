from unsloth import FastLanguageModel

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/mistral-7b-instruct-v0.2-bnb-4bit",
    "unsloth/gemma-7b-it-bnb-4bit",
] # More models at https://huggingface.co/unsloth

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gemma-2-2b-it-bnb-4bit",
    max_seq_length = 2048,
    load_in_4bit = True,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)


# example
eng_sentence = "How are you?"
# urdu_sentence = train_data.translation[2].get("ur")

prompt = """
<start_of_turn>user
Translate the sentence into urdu and only return the translation:
 
This is a spoon<end_of_turn>
<start_of_turn>model
"""

FastLanguageModel.for_inference(model) # Enable native 2x faster inference

# alpaca_prompt = You MUST copy from above!

inputs = tokenizer(prompt, return_tensors = "pt").to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer)
gen_tokens = model.generate(**inputs, streamer = text_streamer, max_new_tokens = 128)

outs = tokenizer.batch_decode(gen_tokens[:, inputs.input_ids.shape[1]:])[0]
response_only = outs.replace(tokenizer.eos_token, "")
print(response_only)