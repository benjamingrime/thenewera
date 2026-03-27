## Agency

### Agentic Leap
language allows agents to respond to questions like a super google search, yes, but with an understanding of language, they can go far beyond that. we think, reason, and most practically *plan* in langauge. reasoning as described above *is* planning; they can break a goal down into steps.

the next step in the agentic leap was acting, taking practical steps to achieve the user-defined goal. In other words, they are now goal-oriented machines. Human provides goal, AI acts towards achieving that goal to satisfy human's preference for that goal. this is done by acting on the plan, primarily via *tool calling*. everything you do on a laptop is code: every button you press, email you send, document you save; it's all executing code. all code is a form of langauge, a "coding langauge" or "programming language". LLMs of an understanding of ALL langauges, including programming langauges, and thus can write the scripts and execute any task on a computer, provided they have access to execute these commands. for example:

Start-Process "https://www.watermangroup.com"
"Hello world" | Out-File -FilePath "$env:C:\Users\MRBG\Documents\demo.txt"
Start-Process "C:\Users\MRBG\Documents\demo.txt"

the current leap being taken is called *orchestration*: the agent can plan, do, and with language, they can instruct others what to do. in other words, they can be the manager of a plan and direct mini sub-agents to complete tasks in accordance with the plan to acheive the goal faster. this is called "multi-agent orchestration" or "A2A". as of early 2026, frontier agents can already autonomously complete tasks that would take a human engineer over half a working day — and this capability has been doubling roughly every three to four months.
Second, reasoning models could make AI agents work a lot better. Agents are systems that can semi-autonomously complete projects over several days, and are now the top priority of the frontier companies.
Reasoning models make agents more capable because:
They’re better at planning towards goals.
They can check their work, improving reliability, which is a huge bottleneck.
We’re starting to see signs of how reasoning models, thinking for longer, and agents all mutually support each other.
"AI won't replace your job, someone using AI will" -- but AI itself can use AI, an agent can use a subagent, even dozens or hundreds. Quite soon, we will see entire organisational trees of AIs.

- next developments will be in agentic computer use and agent org: training which tools to call on and when, how to direct sub-agents. this results in...

### Recursive Self-Improvement
- AI becoming better at AI research: ultimately maths and programming, both of which it excels at due to RLVR.
- This means current models are helping AI researchers produce the next generation of models, which will help build the generation after that more, and son on
- the goal of frontier AI companies is 100% automated AI research. we are already seeing this: AI writes 100% of their code.
- AI researchers stil need to instruct the models (talk to them in language, i.e. input data) for them to act on the next thing, but much of this is interpreting new research (data), analysing results (data), giving feedback from the AI's own output (data), all of which can be input back into the model without human intervention.
- this was purely theoretical only two years ago, but we now have practical evidence this is happening.

METR, an AI safety research organisation, has been tracking what they call the "50% task horizon": the length of task that frontier AI agents can complete successfully half the time. In March 2023, GPT-4 managed tasks requiring about three and a half minutes of human effort. By December 2025, GPT-5.2 reached tasks requiring a full working day. In February 2026, Claude Opus 4.6 reached fourteen and a half hours. The original METR paper estimated this capability was doubling every seven months. A year later, they revised this to every three and a half months. Opus 4.6 sits above even that faster trend line, consistent with a doubling time of around two months. In AI research, the question on everyone's mind isn't "is AI progressing or not?"; it's "is the rate of AI progress exponential or super-exponential?" An exponential grows by a fixed factor — every seven months, say, capability doubles. But if the doubling time itself halves every year, what you have is not just exponential growth but double-exponential growth — the rate of the rate is climbing. We don't yet know if that's what's happening. It could be noise. But if the recursive self-improvement described above is genuinely compounding, it is exactly what you would expect to see in the data.

"We estimate that Claude Opus 4.6 has a 50%-time-horizon of around 14.5 hours (95% CI of 6 hrs to 98 hrs) on software tasks. While this is the highest point estimate we’ve reported, this measurement is extremely noisy because our current task suite is nearly saturated."
they have an enormous CI because it's harder to write the tests for 200 10h tasks than 200 10s tasks. also, whilst "50%" is low, remember that these tasks vary in difficulty. If the task is simple but takes three days, there's a much higher likelihood it will be able to complete it.

- this data flywheel may lead to a "fast-takeoff" or "foom" (like a car whizzing by) where AI improve so absurdly fast that we can't keep track (Singularity). hopefully, this doesn't lead to what alignment researchers call "existential risk" or "doom", but most safety experts and frontier labs agree that the probability of doom, our p(doom), is somewhere between 10 and 90 percent.

why is this?