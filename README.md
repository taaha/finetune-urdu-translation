# finetune-urdu-translation

[dataset used: ](https://www.kaggle.com/datasets/muhammadanasmahmood/englishurdu-parallel-corpus)

Gemma 2b is finetuned on Urdu (a low resource language)

pretrained models gove a BLEU (average for all test set) score of
en -> ur : 0.015
ur -> en : 0.073

After finetuning
en -> ur : 0.204
ur -> en : 0.251


Finetuned models
[eng_urdu](https://huggingface.co/darthPanda/gemma_2b_en_ur)
[eng_urdu](https://huggingface.co/darthPanda/gemma_2b_ur_en)
