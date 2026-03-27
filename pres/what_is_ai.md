
This note contains a plan and ideas about a presentation introducing LLMs to a non-technical audience. I want this presentation to convince the audience that LLMs are here to stay and that it is imperative they learn to use these systems. To do so, I want to spark awe and wonder in my audience, whilst explaining the fundamentals of LLMs and progress since the release of GPT-3.

Intro

There's this thing people are talking about, not sure if you've heard of it… it's called AI. But AI has been around since the 50s, so why is everyone talking about it now? Well, there's this other thing people are talking about, not sure if you've heard of it… it's called ChatGPT.
ChatGPT is pretty damn smart, and has a clumsy twin called Copilot. They have slightly smarter cousin they’re both very envious of called Gemini, and another cousin trying to save the world called Claude. They all come from the same family called "Large Language Models", or LLM for short.
LLMs have been making progress in the capabilities absurdly fast. We measure this with something called benchmarks, much like (sometimes exactly like) how we measure each other through standardised tests or qualifications like A-Levels.
GPT-3.5 benchmarks.
GPT-5.2 benchmarks.
IMO, IPO, IIO golds in 2025.
In Jan 2026, people prompting GPT5.2 in right way to solve maths problems. Verified by the Messi of Maths, Terrence Tao.
How do these machines know things? You might be inclined to think they must be cheating, that there's some sort of intellectual sleight of hand going on. But when we can dig into this question of how we know someone knows something in everyday life, when we say "he or she knows x", you'll find this isn't the case.
This is a two part question, one part philosophical, one part scientific; one theoretical, the other practical (theory and practice). Once we understand the theory of what it is for something to know, the practice of how to grow these models makes far more sense.
So, for the first part, we need to back 100 years to a philosopher called Wittgenstein, and get to grips with that second "L" in LLM: language.


---

Theory

Wittgenstein & Language Games
Wittgenstein wanted to know how we participate in this thing called "language". as a matter of empirical fact, 5 year olds use language all the time. also, language is simply a collection of words. so, let's break it down. simple question: how do know what words mean? any guesses?
anyone read a dictionary front to back? I'm only halfway through, no spoilers please.

Johnny
Imagine a 5 year old called Johnny. Johnny has read a couple of books and he's come across a word he's struggling with: "game". How does he come to know the word?
Well, we don't sit Johnny down and say (sternly), "Johnny, here is the form of the game. Follow this definition only. If anyone tells you otherwise it's propaganda, fake news. Don't listen to 'em."
Of course not, it's silly: there is no universal, essential definition. What does chess have in common with football, darts, the Olympics? If we want to say that "all games are human behaviours governed by rules", we'd have a tough time fitting peekaboo into that definition. it doesn't have any rules, are there offsides? 
Instead of there being some universal definition, Wittgenstein says that meaning is use. If you want to know what a word means, look for how people use it in everyday language. Very practical, very common-sense. So, Johnny learns what a game is through examples, through practice. We show him noughts and crosses, chess, cricket, the Olympics.
And if he says "this thing I'm drinking from, that's a game", we correct him and say "no Johnny, that's a bottle", and point out more examples of games. So, we learn through this iterative process of practice and feedback. That's how we know what words mean, generally speaking, and that's how we verify Johnny knows anything at all: through use.

In other words, we know things when we learn the patterns of which words go where: pattern recognition. Over time, our brains build a predictive model of which words belong where in the surrounding world. To prove this, let's play a simple game: what comes next?
"Fish and..."
"Bob's your..."
"God save the..."
See what happened with that last one? You practiced and practiced all your life, and now your predictive model no longer fits the world perfectly. You got it wrong.
If our brains are big pattern recognition, predictive models, then, feasibly, an actual pattern recognition predictive model can understand language too: a language model. And the bigger the brain, the more patterns it can recognise. Hence, Large.
So there we are, Large Language Model, or LLM.
But there's something missing essential missing...

Context

Suppose Johnny joins his friends A and B midway through a conversation, and friend B responds "wot" (phonetically) to friend A. Johnny has no knowledge of what friend A said. Now, Johnny has come across this sound, this word, before, but can he be sure of its meaning? No! He can't. There are many ways in which "wot" might be an adequate response from B to A.
- friend A mumbles incomprehensibly to B ... B replies, "what?"
- friend A tells B, "I just won the Euro Millions jackpot" ... B replies rhetorically, in shock, "what."
- friend A asks B, "what is the name of the SI unit for power equivalent to one joule per second?" ... B replies "watt".

Wittgenstein also gives the example of "Water!", which can be used as an exclamation, an order, a request, or an answer to a question. The meaning of the word depends on the context in which it is used. Another way Wittgenstein makes the point is that the word "water" has no meaning apart from its use within a particular context.

Johnny needs context to fully understand language, and hence the world. it is up to us to provide this to Johnny so that he properly understands our picture of the world. We provide the context. This is what we're doing when we're interacting with ChatGPT, often called prompting. this is what we're doing when we upload documents for an LLM to read: providing context. We'll get into this more and best practices in later lectures.

So, that's language, and understanding how Johnny learns language gives us an insight into how large language models do the same.
OpenAI (company behind ChatGPT) released GPT-3 on Nov 2022, and marked the release of ChatGPT to the public. GPT-1 and GPT-2 basically spat out garbled messes, quite useless. The key jump from 2 to 3 was the size of the brain, increasing the number of neurons and connections between them (called scaling, which we'll get into next week). GPT-3 is large and has a model of language. It's a large language model, much like Johnny.


---

Practice

So now that we have the theoretical basis for how models can know things like we do, how do they do this in practice? For us, it's sort of intuitive as we've been doing this our whole lives. With machines, it's less obvious. 
I've really anthropomorphised these machines through this analogy with Johnny. I'm going to continue to doing that. In some ways, AI has a brain much like ours: it has neurons and synapses (nodes and weights), and researchers are increasingly trying to adapt AI brains to mimic human brains. First, we need to understand what form this learning comes in.

Data
You might have heard that AI needs good training data. We can bridge this gap between human and machine learning again by recognising one thing: data is simply recorded information. We learn through information, machines learn through data. For example, I know the names of people in the Manchester office. They're in my head because it's information I've gathered and stored in my brain. However, it's only data until I record it somewhere, like write it down or put it in a spreadsheet. Another example: word documents are data, they are recorded information (it doesn't have to be in Excel to be data). Good training data is simply the correct recorded information. It's no good AI learning from data that's incorrect.
This is why people say, rightly, the AI is coming for entry-level knowledge jobs. The knowledge entry-level employees have is what we call explicit knowledge. Almost all entirely gained through data, recorded information, knowledge that has been explicated that undergrads learn through something like a 3-year degree. Senior workers have more tacit knowledge, knowledge that is difficult to describe with language. What is stakeholder management exactly? We can all use the word, but it's tough to define, tough to write down, to transform into data.

bigger brain = more intelligence. More computational power for training (i.e. ‘training compute’) means you can use more neurons, which lets the models learn more sophisticated and abstract patterns in the data. It also means you can use more data. This is making the hardware better, the computers, the data centres. roughly increasing 4x per year. this process of increasing intelligence with more compute is called scaling. and it's why you should have invested in Nvidia 5 years ago.
2023 - bee
2024 - squirrel
2025 - cat
human - 20x larger than a cat
also, algorithmic efficiency: software, the structure of the brain itself. because we can rewire the brain to get the same performance for less energy, we can use the same amount of compute more efficiently to get even better results. algorithmic efficiency has been increasing 3x per year, i.e. the same energy goes three times further.
software + hardware improvements result in 12x efficiency per year. this means we're in track for a human-sized brain by the end of 2026.


Pre-Training
During pre-training (which is really just the first part of training), we are building base-layer of intelligence: an understanding of language. This is the "predicts the next word" part people refer to, this is the method it uses to understand language. The data it uses is much of the internet, everything from silly reddit posts to medical journals. Trillions of pieces of text. To learn, it takes a sentence like "Einstein's fist name is...", covers up the answer, makes a prediction, compares the prediction to the answer, and finally adjusts its neurons in a way that's expected to increase accuracy the next time round, much like how learn by doing corrections in school;.

Post-Training
Again, a misnomer, just means the second phase of training.
Reinforcement learning: do this all the time with training a dog, teaching a baby, encouraging a child. the language changes but the method is the same: reward what behaviour we want.
People often say “ChatGPT is just predicting the next word.” But that’s never been quite true. Raw prediction of words from the internet produces outputs that are regularly crazy (as you might expect, given that it’s the internet). Think of the initial large language model (LLM) as containing a foundation of knowledge and concepts. Reinforcement learning is what enables that structure to be turned to a specific end. 
GPT only became truly useful with the addition of reinforcement learning from human feedback (RLHF):
1) The model produces outputs
2) Humans rate those outputs for helpfulness
3) The model's neurons are adjusted in a way expected to get a higher rating
A model that’s under RLHF hasn’t been trained only to predict next tokens, it’s been trained to produce whatever output is most helpful to human raters. This is where people rightly accuse LLMs of being sycophantic. AI-induced psychosis (a real thing).
This improved results a bit (list benchmarks for GPT-4 vs GPT3.5)
True paradigm shift and leap came from...

Reasoning
RL on chain of thought. Reward for good and bad reasoning reasoning. Models trained on good reasoning traces. Learn to reason, to plan, to think.
RLVR & LLM-as-a-judge.
Thinking time 

Agentic Leap
language allows agents to respond to questions like a super google search, yes, but with an understanding of language, they can go far beyond that. we think, reason, and most practically *plan* in langauge. reasoning as described above *is* planning; they can break a goal down into steps.

the next step in the agentic leap was acting, taking practical steps to achieve the user-defined goal. this is done by acting on the plan, primarily via *tool calling*. everything you do on a laptop is code: every button you press, email you send, document you save; it's all executing code. all code is a form of langauge, a "coding langauge" or "programming language". LLMs of an understanding of ALL langauges, including programming langauges, and thus can write the scripts and execute any task on a computer, provided they have access to execute these commands. for example:

Start-Process "https://www.watermangroup.com"
"Hello, Board." | Out-File -FilePath "$env:C:\Users\MRBG\Documents\demo.txt"
Start-Process "C:\Users\MRBG\Documents\demo.txt"

the current leap being taken is called *orchestration*: the agent can plan, do, and with language, they can instruct others what to do. in other words, they can be the manager of a plan and direct mini sub-agents to complete tasks in accordance with the plan to acheive the goal faster. this is called "multi-agent orchestration" or "A2A".
Second, reasoning models could make AI agents work a lot better. Agents are systems that can semi-autonomously complete projects over several days, and are now the top priority of the frontier companies.
Reasoning models make agents more capable because:
They’re better at planning towards goals.
They can check their work, improving reliability, which is a huge bottleneck.
We’re starting to see signs of how reasoning models, thinking for longer, and agents all mutually support each other.

Human brain:
1.5kg
20 watts
signals sent through dendrites at 100-200hz
signals are electro-chemical wave propagations moving at 30m/s

AI brain (data centre):
15m kg (x10m)
200Mw (x10m)
10b Hz (x10m)
300m m/s (x10m)

---

Capabilities: What Can They Actually Do?

The Olympiad Sweep

Let's start with something concrete. We all know what it means to get a gold medal in the Olympics. There are academic Olympics too: the International Mathematical Olympiad, the International Physics Olympiad, the International Olympiad in Informatics. The hardest standardised tests on Earth. The kind of thing where entire countries celebrate when their kid brings home a gold.

In July 2025, Gemini Deep Think scored 35/42 on the IMO. Gold medal. Not just any gold: it solved 5 of 6 problems perfectly, within the 4.5 hour time limit, graded by official IMO coordinators using the same criteria as human students.

In coding, OpenAI's o3 model scored gold on the 2024 International Olympiad in Informatics, ranking 6th overall against human competitors. This was a general-purpose model, not even fine-tuned for competitive programming.

In physics, an AI agent system called "Physics Supernova" scored 23.5/30 on the 2025 International Physics Olympiad, ranking 14th out of 406 contestants and beating the median human gold medallist.

These aren't cherry-picked benchmarks on a company's website. These are the hardest exams on the planet, graded by the same people who grade the kids.

---

Case Studies: The 2026 Frontier

So we've got a machine that can ace every standardised test we throw at it. So what? What does that look like in the real world?

1. Mathematics: The Erdos Conquest

Paul Erdos was one of the most prolific mathematicians in history. He left behind hundreds of unsolved problems, many with cash bounties, that have taunted the field for decades. Some have been open for 30-50 years.

In January 2026, a user named Kevin Barreto prompted GPT-5.2 Pro to tackle Erdos Problem #728. The model produced an informal proof. Then a system called Aristotle by Harmonic auto-formalised it in Lean (a proof verification language, like a spell-checker for maths). On January 8th, Terence Tao, widely regarded as the greatest living mathematician, reviewed the proof and accepted it. Erdos Problem #728 became the first Erdos problem solved largely autonomously by AI.

Within seven days, two more Erdos problems fell. Since October 2025, AI tools have helped move roughly 100 Erdos problems from "open" to "solved." Since Christmas alone, 15 problems were resolved, 11 of which specifically credited AI.

Tao is careful to note these are the "lowest-hanging fruit": problems solvable with known techniques that were simply too niche or tedious for top mathematicians to prioritise. But that's precisely what makes it remarkable. The machine didn't just solve one problem. It's systematically clearing the backlog of human mathematics. The entire pipeline from prompt to Fields Medallist verification took days, not decades.

The AI tool: GPT-5.2 Pro (OpenAI) + Aristotle (Harmonic) for Lean formalisation.
Human timeline: 30-50 years unsolved. AI timeline: days.

2. Physics: Materials Discovery at Scale

Finding new materials used to be one of science's slowest endeavours. You hypothesise a crystal structure, synthesise it in a lab, test its properties, repeat. A single new material might take 5-10 years to validate.

In November 2023, DeepMind released GNoME (Graph Networks for Materials Exploration). It predicted 2.2 million new crystal structures, of which 380,000 are stable and promising for experimental synthesis. That's equivalent to roughly 800 years of human materials discovery. Among the discoveries: 52,000 new layered compounds similar to graphene with potential for superconductors. Previously, only about 1,000 such materials had ever been identified.

This isn't theoretical. External researchers have independently created 736 of GNoME's predicted materials in the lab. An autonomous lab system at Lawrence Berkeley synthesised 41 of 58 predicted compounds in 17 days of continuous automated experiments, a 71% success rate.

The AI tool: GNoME (DeepMind), a specialised graph neural network, not a chatbot.
Human timeline: ~800 years of equivalent discovery. AI timeline: months.

3. Chemistry: Drug Discovery

Developing a new drug typically takes 10-15 years and costs an average of $2.6 billion. Most candidates fail. The process is brutal.

Insilico Medicine, a biotech company, used their AI platform Pharma.AI to identify a novel drug target for idiopathic pulmonary fibrosis (a fatal lung disease), design a molecule to hit that target, and push it through to clinical trials. Target to Phase I in 30 months, roughly a third of the traditional timeline, at a tenth of the cost. The drug, Rentosertib (ISM001-055), became the first AI-discovered drug to reach Phase II clinical trials. In June 2025, Nature Medicine published the Phase IIa results: patients on 60mg showed a mean improvement in lung function of +98.4mL, compared to a decline of -20.3mL in the placebo group.

This is real medicine, in real patients, discovered by AI, published in Nature Medicine.

The AI tool: Pharma.AI (Insilico Medicine), a purpose-built drug discovery platform combining PandaOmics (target ID) and Chemistry42 (molecule design). Not a chatbot.
Human timeline: 10-15 years, $2.6B average. AI timeline: 2.5 years to Phase I, ~$260M.

4. Biology: Designing Life From Scratch

In October 2024, David Baker won the Nobel Prize in Chemistry for computational protein design. His lab's tool, RFdiffusion, can design entirely new proteins that have never existed in nature. Not editing existing proteins. Designing them from scratch.

The latest version, RFdiffusion3, can design proteins that interact with virtually every type of molecule found in cells: DNA, other proteins, small molecules. It's open source. Baker's lab has used it to create de novo enzymes (catalysts that speed up chemical reactions) with efficiencies approaching those evolution took billions of years to produce.

Meanwhile, EvolutionaryScale's ESM-3, a protein language model trained on billions of protein sequences, can generate novel protein scaffolds from multimodal prompts (you tell it the structure, function, and sequence constraints, and it designs the protein). It's being used in a global tournament with 290+ teams from 40 countries to design better PETase enzymes, the proteins that eat plastic. Previous AI-assisted work at UT Austin (FAST-PETase, 2022) already produced an enzyme that can break down an entire plastic container in under two weeks at 50 degrees C, about 38x faster than natural variants.

Evolution took millions of years to stumble upon a bacterium that could nibble on plastic. AI is designing better versions from scratch.

The AI tool: RFdiffusion3 (David Baker lab / IPD), ESM-3 (EvolutionaryScale). Specialised protein design models, not chatbots.
Human timeline: billions of years of evolution. AI timeline: computational design cycles measured in hours.

5. Coding: The Machine That Builds Itself

This one is personal because I built this presentation with AI. But let me give you the bigger picture.

Dario Amodei, CEO of Anthropic (the company behind Claude), stated in early 2025 that 90% of code at Anthropic would soon be written by AI. By early 2026, Anthropic's Chief Product Officer confirmed it's effectively 100%. Senior engineers at both Anthropic and OpenAI have publicly stated that 100% of their code is now AI-written. They direct; the machine writes.

Claude Code, Anthropic's coding tool, hit $1 billion in annualised revenue within six months of launch. By mid-2025 it was processing 195 million lines of code weekly across 115,000 developers. Google CEO Sundar Pichai confirmed that over 30% of Google's new code is AI-generated.

On SWE-bench, a benchmark that tests AI on real GitHub issues from real open-source projects, frontier models now solve over 60% of issues autonomously. A year ago that number was in the low 20s.

The machine is building itself. Claude is writing the next version of Claude. This isn't science fiction; it's Anthropic's engineering workflow.

The AI tool: Claude Code (Anthropic), GitHub Copilot (Microsoft/OpenAI), and others. These are frontier LLMs applied to code.
Human timeline: a 5-person team, 3 months. AI timeline: hours to days for equivalent scope.

6. Engineering: This One's For Us

OK. Maths, physics, chemistry, biology, coding. Impressive. But what about engineering? What about infrastructure? What about what we actually do?

Data Centres: The First Proof

The earliest and cleanest example of AI in engineering is Google's data centre cooling system. Starting in 2016, DeepMind trained a neural network on thousands of sensor readings to optimise cooling. Result: 40% reduction in cooling energy costs. Not a projection. Measured, verified, published. They later moved to fully autonomous AI control, which delivers consistent 30% energy savings and achieved the lowest Power Usage Effectiveness (PUE) ever recorded at the facility (PUE 1.1, with 0.4% prediction error).

If you manage buildings, this is your future. AI doesn't just monitor systems; it runs them better than human operators can.

Bridge Health Monitoring: From Annual Inspections to 24/7 Prediction

The field of structural health monitoring is undergoing a transformation. Research publications in AI-driven SHM rose from 95 in 2000 to 3,432 in 2024. What used to be annual or biannual manual inspections is being replaced by continuous AI monitoring using sensors, drones, and computer vision.

Current systems use convolutional neural networks and vision transformers to detect surface damage (cracks, spalling, corrosion) from drone imagery. Machine learning models analyse high-dimensional sensor data to predict deterioration rates and forecast when specific components will need attention. AI predictive maintenance has been shown to cut infrastructure failures by up to 73%.

The UK: Our Competitors Are Already Moving

In May 2025, Arup published a global survey of 5,000 architects, engineers, and city planners. The headline: more than a third (36%) are using AI daily to design cities and infrastructure. Over 80% use it at least weekly.

Arup's own tools include Loupe 360, which combines robotics and AI to assess tunnel conditions using computer vision. They're using machine learning to analyse urban landscapes, AI-supported generative design to evaluate options across cost, carbon, and performance. Their digital twin work with the Hong Kong government won the ISOCARP Grand Award in 2025, their third.

The Department for Transport and Arup found that integrating UK transport networks using digital twins could deliver around GBP 850M in benefits over a 10-year period.

Arup. Digital twins. Autonomous inspection. Predictive maintenance. GBP 850 million. These aren't startups. This is the industry we work in, and our direct competitors are investing now.

What This Means for Waterman

The pattern across every case study is the same: specialised AI systems are compressing decades of work into days. Not replacing engineers, but changing what engineering looks like. The engineer who spends three weeks manually reviewing structural survey data will be outperformed by the engineer who spends three hours directing an AI to do it and then applies their judgement to the results.

The 12x annual efficiency improvement we discussed earlier means that the expensive, cutting-edge AI capabilities of today will be the free default tools of next year. The AI that costs hundreds of pounds per year to run right now will be on your phone, free, by 2027.

The question isn't whether AI will transform engineering consultancy. It's whether Waterman will be the consultancy that transforms, or the one that watches its competitors transform.