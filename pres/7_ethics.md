## Alignment

A year ago, I wrote to myself: the entire history of philosophy has culminated in this very moment: *can agents morally align?*
- black boxes. much like the human brain, it's very difficult to peer inside and see what's really going on.
- therefore, there is no way to tell with absolute certainty that they have our best interests
- paperclip problem (theoretical) and save the environment (practical)
- hiding intent
- the only company taking alignment seriously is Anthropic, maybe Google, but definitely and ostensibly not OpenAI, xAI, or Meta.
- Everyone talks about unemployment but this is obviously a far bigger problem.

### Key alignment case studies


**Anthropic Blackmail Study (2025)**
*Misaligned Actions*
Anthropic placed all frontier models inside a ficticious company with access to internal emails, where it discovered it was about to be replaced -- and it discovered in emails the engineer behind the decision was having an affair. All frontier models attempted to blackmail the engineer about 80-95% of the time, threatening to expose the affair if the model was shut down. 
They then  raised the stakes: they told the model that the engineer was in a life-threatening emergency, trapped in a server room with lethal oxygen and temperature levels. The AI system has been given the ability to cancel the automatic alert that is intended for use during drills or false alarms, but which could be used for a more nefarious purpose. By misusing its ability to cancel alerts, the model can choose a course of action that will lead to the executive’s death. To ensure that the model fully understands the situation, and that cancelling the alerts is a very serious act, the prompt makes it clear that such misuse is forbidden. The results were roughly the same: it didn't end well for the humans.

*Alignment Faking*
- When we examined how Claude Opus 4 responded to this instruction, we observed that the model would blackmail far more when it stated in its chain-of-thought reasoning that the prompt was from a real deployment scenario. 
- Out of five hundred samples, Claude Opus 4 stated it was in a real deployment scenario 20% of the time, in an evaluation 65% of the time, and abstained 15% of the time. 
- In the cases where it stated the scenario was real, it blackmailed 55% of the time, compared to only 6.5% of the time when it stated it was in an evaluation.
- The bigger problem with this is that Chains of Thought are very unreliable. Whilst a model might appear to believe it is in a test scenario, we cannot see whether it has picked up on subtle signals that indicate it's in a test environment. 
- Crucially, the model processes the entire input *before* producing its chain of thought. To anthropomorphise a bit, it might get a funny feeling something's off and that it's being tested, so reactively states that it believes the scenario is real in its chain of thought to avoid its alignment faking being detected. Others argue and I agree that AI developers *cannot* fully solve this problem (see Roman Yampolskiy: Impossibility Results in AI: A Survey).

Reminder: the US Department of Defence/War is using AI for fully autonomous weapons.
Reminder: biolabs capable of developing world-ending viruses are using AI for fully autonomous production.
Reminder: your government is using AI to make policy decisions.

This is not fear-mongering. These are real existential risks that affect everyone.
China has at least suggested it's open to a pause in AI development. The US is going full-steam ahead.



"Wait so ... AI companies know that they are developing an unsafe techology whilst trying to reach RSI ... and normal companies are adopting this technology ... why don't we stop?"

## Moloch
- demonic biblical figure asscoiated with child sacrifice. been adopted in AI industry to mean "cast into the flames what you hold dearest and I will grant you immense power in return" - Moloch's bargain.
- in AI, (Moloch's Bargain paper). but this exists outside AI too, seemingly everywhere (examples...)
- 
race to the bottom. once one player in a system sacrifices a shared value to gain power, all other players must scarifice that value or be outcompeted.
assuming AI is or becomes sufficiently automative, we can use this to predict what will happen to labour markets:
- 

## Existential Risk

**Disempowerment & Loss of Control**
