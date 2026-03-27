## Training

### Pre-Training
During pre-training (which is really just the first part of training), we are building base-layer of intelligence: an understanding of language. This is the "predicts the next word" part people refer to, this is the method it uses to understand language. The data it uses is much of the internet, everything from silly reddit posts to medical journals. Trillions of pieces of text. To learn, it takes a sentence like "Einstein's fist name is...", covers up the answer, makes a prediction, compares the prediction to the answer, and finally adjusts its neurons in a way that's expected to increase accuracy the next time round, much like how learn by doing corrections in school.

### Post-Training
Again, a misnomer, just means the second phase of training.
Reinforcement learning: do this all the time with training a dog, teaching a baby, encouraging a child. the language changes but the method is the same: reward what behaviour we want.
People often say “ChatGPT is just predicting the next word.” But that’s never been quite true. Raw prediction of words from the internet produces outputs that are regularly crazy (as you might expect, given that it’s the internet). Think of the initial large language model (LLM) as containing a foundation of knowledge and concepts. Reinforcement learning is what enables that structure to be turned to a specific end. 
GPT only became truly useful with the addition of reinforcement learning from human feedback (RLHF):
1) The model produces outputs
2) Humans rate those outputs for helpfulness
3) The model's neuron connections are adjusted in a way expected to get a higher rating
A model that’s under RLHF hasn’t been trained only to predict next tokens, it’s been trained to produce whatever output is most helpful to human raters. Whilst this made AI very good at giving answers humans like, the true paradigm shift and leap came from...

### Reasoning
RL on chain of thought. Reward for good and bad reasoning reasoning. Models trained on good reasoning traces. Learn to reason, to plan, to think.
RLVR & LLM-as-a-judge.
inference time scaling