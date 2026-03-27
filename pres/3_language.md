Here's the state of AI.

First thing’s first: eject the concept of a chatbot from your mind. Eject image generators, deepfakes, and the like. Eject social media algorithms. Eject the algorithm your insurance company uses to assess claims for fraud potential. I am not talking, especially, about any of those things. Instead, I’m talking about LLMs. Simply put, in the coming years, LLMs will be configured in such a way that they can plan, reason, and execute intellectual labor.

Two months ago, mathematicians used the latest versions of ChatGPT, an LLM, to solve frontier maths problems called Erdős problems. The solutions were soon verified by the Messi of Maths, Terrence Tao, establishing the first fully autonomous system to solve an open maths problem. This is truly remarkable, and stories like these extend beyond maths. LLMs are doing research-level STEM.

How did this happen? Do these machines *know* anything at all? You might be inclined to think they must be cheating, that there's some sort of intellectual sleight of hand going on. But when we can dig into this question of what we mean when we say "he or she *knows* x", you'll find this isn't the case. They really do *know* things and they really *are* intelligent.

This is a two part question, one part philosophical, the other part scientific; one theoretical, the other practical. Once we understand the theory of what it is to say we know something to know, the practice how LLMs are developed and what the resulting product is capable of makes far more sense. This will give you the concepts to understand how it's possible that a machine can do real intellectual labour, and hence understand and plan for what's to come.

So, for the first part, what it means to know things, we need to back 100 years to a philosopher called Wittgenstein, and get to grips with that second "L" in LLM: language.

## LLMs, Wittgenstein & Language

### Wittgenstein & Language Games
Wittgenstein wants to know the answer to a simple question: how do we know what words mean?
anyone read a dictionary front to back? I'm only halfway through, no spoilers please.

### Johnny
Imagine a 5 year old called Johnny. Johnny has read a couple of books and he's come across a word he's struggling with: "game". How does he come to know the word?
Well, we don't sit Johnny down and say (sternly), "Johnny, here is the form of the game. Follow this definition only. If anyone tells you otherwise it's propaganda, fake news. Don't listen to 'em."
Of course not, it's silly: there is no universal, essential definition. What does chess have in common with football, darts, the Olympics? If we want to say that "all games are human behaviours governed by rules", we'd have a tough time fitting peekaboo into that definition. it doesn't have any rules, are there offsides? 
Instead of there being some universal definition, Wittgenstein says that words get their meaning through use. If you want to know what a word means, look for how people use it in everyday language. Very practical, very common-sense. So, Johnny learns what a game is through examples, through practice. We show him noughts and crosses, chess, cricket, the Olympics.
And if he says "this thing I'm drinking from, that's a game", we correct him and say "no Johnny, that's a bottle", and point out more examples of games. So, we learn through this iterative process of practice and feedback. That's how we know what words mean, generally speaking, and that's how we verify Johnny knows anything at all: through use.

In other words, we can use language effectively when we learn the patterns of which words go where in everday use: pattern recognition. Over time, our brains build a model of which words and concepts belong where in the surrounding world. To prove this, let's play a simple game: what comes next?
"Fish and..."
"Bob's your..."
"God save the..."
See what happened with that last one?
If our biological brains are big pattern recognition models, then, feasibly, an computational pattern recognition model is functionally the same and can understand language too: a language model. And the bigger the brain, the more patterns it can recognise. Hence, Large.
So there we are, Large Language Model, or LLM. LLMs understand langauge, and we can say "ChatGPT knows x" because it has seen words, used them, and has been given feedback on its errors, just like Johnny.

That's a good starting point, but there's something missing if we want to understand the meaning of words at any given time...

### Context
Our how we come to say "he or she knows x" was  Suppose Johnny joins his friends A and B halfway through a conversation, and friend B responds "wot" (phonetically) to friend A. Johnny has no knowledge of what A said to B. Now, Johnny has come across this sound, this word, before, but can he be sure of its meaning? Well, there are many ways in which the sound (word) "wot" might be an adequate response from B to A.
- friend A mumbles incomprehensibly to B ... B replies, "what?"
- friend A tells B, "I just won the Euro Millions jackpot" ... B replies rhetorically, in shock, "what."
- friend A asks B, "what is the name of the SI unit for power equivalent to one joule per second?" ... B replies "watt".

Wittgenstein also gives the example of "Water!", which can be used as an exclamation, an order, a request, or an answer to a question. The point is the meaning of the word depends on the context in which it is used. In fact, the word "water" has no meaning apart from its use within a particular context, or any word for that matter.

We provide this context so Johnny can properly understand the meaning of the words we use and therefore to understand the world around him. This is what we're doing when we're interacting with LLMs like ChatGPT, often called prompting. This is what we're doing when we upload documents for an LLM to read: providing context.

So, that's how words get their meaning: through how they are used in everyday life and the context in which they are currently being used. Understanding how Johnny learns language gives us an insight into how large language models do the same.

You might object that the machine doesn't *really* understand, it's "just a stochastic parrot". But ask yourself: how do you know anyone really understands? The only test we've ever had is behaviour: can they use the words correctly? By that measure, these models largely pass.

- train to build understanding of world globally
- context to become useful in world locally

So that's the philosophical basis, the theory, for why it's reasonable to say that these models know things. How does this happen practically?