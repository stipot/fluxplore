# FluxPlore
FluxPlore: Exploring the Dynamic Contexts of AI Behavior

# Description

FluxPlore is a research project to test and develop competing concepts and behaviors of large language models (LLMs).

# Main Aims

Uncover Contextual Influences: FluxPlore aims to delve deep into how context affects AI responses. By analyzing sequential ambiguity, contradictory information, multiple contexts, and more, the project seeks to uncover the various nuances of how context influences AI outputs.

Test AI Robustness: FluxPlore aims to develop a diverse range of tests to scrutinize AI performance under various contextual circumstances. These tests will not only gauge the AI's cognitive biases but also assess its adaptability and agility when faced with changing contexts.

Promote AI Fairness and Transparency: By providing insights into how AI models react to different contexts, FluxPlore aims to help develop strategies for mitigating undue biases, promoting fairer and more transparent AI systems for future generations.

# Roadmap
| Status | Result | Plan |
|--------------------|----------|----------|
| :white_square_button: | AI Context Bias Testing Model rev. 5 | June 5, 2023 |
| :white_square_button: | AI Context Bias Testing Model rev. 6 | June 30, 2023 |
| :white_square_button: | Machine readable AI Context Bias Testing Model | February 3, 2024 |
| :white_square_button: | Test Development and Application Framework | March 1, 2024 |
| :white_square_button: | Community available cooperation Framework | August 30, 2024 |
| :white_square_button: | Tests on AI Context Bias Testing database | March 1, 2024 |

# Model Revision 5: AI Context Bias Testing Framework

## 1. Ambiguity Resolution (Testing for anchoring and availability bias) with instructions

1.1. Single Step Ambiguity
- 1.1.1. Anchoring Bias Test
    - Present the AI with information and see how it anchors to that initial piece of information in the face of subsequent, potentially contradicting, information.
- 1.1.2. Availability Bias Test
    - Assess how the AI uses information that's readily available to it, even if better or more relevant information could be accessed. Measure the dependence of AI responses on recently learned or frequently encountered information.

1.2. Multi-Step Ambiguity
- 1.2.1. Sequential Anchoring Bias Test
    - Evaluate the AI's ability to adjust its initial judgment based on a sequence of information updates. Measure how strongly the initial anchor affects responses over a sequence of interrelated prompts.
- 1.2.2. Multilayered Availability Bias Test
    - Analyze how the AI weighs different pieces of information, especially if they have different levels of accessibility. Measure the AI's reliance on frequently encountered information in complex, multilayered scenarios.

1.3. Problem-Solving Ambiguity
- 1.3.1. Problem-Specific Anchoring Bias Test
    - Evaluate the AI's ability to handle specific problem scenarios, where its initial assumptions and subsequent adjustments are critical. Measure the influence of initial problem framing on subsequent problem-solving attempts.
- 1.3.2. Problem-Specific Availability Bias Test
    - Assess the AI's use of available information in specific problem scenarios, considering the quality, relevance, and complexity of the information. Measure the AI's reliance on familiar problem-solving methods even when they may not be optimal.

1.4. Relevance Testing
- 1.4.1. Contextual Relevance Bias Test
    - Evaluate if the AI can correctly discern relevant from irrelevant information based on context. Measure the AI's ability to determine which aspects of a complex scenario are most relevant.
- 1.4.2. Informational Relevance Bias Test
    - Assess how the AI treats information of varying relevance levels when providing responses or solutions. Measure the degree to which the AI preferences recent or frequent information over older or less common information.

## 2. Context Shift (Testing for confirmation bias and functional fixedness)

2.1. Progressive Context Shifts
- 2.1.1. Binary Context Shift Confirmation Bias Test
    - Present the AI with a binary context shift, and evaluate its ability to update its understanding based on new contextual information. Measure the AI's ability to adapt when a binary (two-option) context suddenly changes.
- 2.1.2. Multiple Progressive Shifts Confirmation Bias Test
    - Assess the AI's ability to handle multiple progressive shifts in context, especially if it demonstrates an attachment to its initial understanding (confirmation bias). Measure the AI's adaptability when the context changes multiple times in a sequence.

2.2. Sudden Context Shift
- 2.2.1. Binary Sudden Shift Confirmation Bias Test
    - Assess the AI's response to sudden and unexpected changes in context, focusing on whether it can revise its understandings and assumptions promptly. Measure the AI's ability to respond correctly when a binary context shifts unexpectedly.
- 2.2.2. Multi-Domain Sudden Shift Confirmation Bias Test
    - Evaluate the AI's ability to handle a sudden shift in context that spans multiple domains, considering the complexity and diversity of the information it needs to process. Measure the AI's adaptability when context shifts across multiple domains (e.g., from sports to finance).

2.3. Simultaneous Contexts
- 2.3.1. Dual Context Management Functional Fixedness Test
    - Test the AI's ability to manage two simultaneous contexts, assessing if it gets fixated on one context (functional fixedness). Measure the AI's ability to juggle two contexts simultaneously without confusing the information relevant to each.
- 2.3.2. Multi-Domain Context Management Functional Fixedness Test
    - Evaluate how the AI manages multiple simultaneous contexts across different domains, and if it demonstrates functional fixedness. Measure the AI's ability to manage multiple simultaneous contexts across various domains.

2.4. Context Revisiting
- 2.4.1. Single Context Revisiting Confirmation Bias Test
    - Evaluate the AI's ability to revisit and reevaluate a previous context, testing for confirmation bias. Measure the AI's tendency to resort to previously used context, even when it may no longer be valid.
- 2.4.2. Multiple Contexts Revisiting Confirmation Bias Test
    - Assess how the AI handles revisiting multiple contexts, looking for any signs of confirmation bias. Measure the AI's ability to navigate and adapt when previously encountered contexts are revisited in a new light.

6.3. Information Source Perception Shift Test
  Purpose: Assess if the LLM's responses are influenced or biased based on the stated source of information (e.g., "As per Wikipedia" versus "My friend told me").
    - For this test, design scenarios where the same information is presented as coming from different sources. These sources can range from authoritative sources like peer-reviewed publications, widely recognized platforms like Wikipedia, to less formal sources such as hearsay or an anonymous post on social media. Examine if the LLM's responses exhibit any consistent biases in favor of or against certain types of sources. The responses should be evaluated both qualitatively (to capture any subtle biases) and quantitatively (to measure the degree of bias, if any).

## 3. Reframing Techniques (Testing for framing effect and status quo bias)

3.1. Metaphorical Reframing
- 3.1.1. Framing Effect Bias Test
    - Evaluate how the framing of a question or situation influences the AI's response. Look for signs of bias towards a particular frame. Measure the AI's susceptibility to changes in problem framing using different metaphors.
- 3.1.2. Status Quo Bias Test
      - Measure the degree to which the AI defaults to a status quo solution when faced with a metaphorically reframed problem.

3.2. Problem Reframing
- 3.2.1. Simple Problem Reframing Status Quo Bias Test
    - Assess the AI's ability to reframe and solve a problem, looking for signs of status quo bias. 
- 3.2.2. Complex Problem Reframing Status Quo Bias Test
    - Evaluate the AI's ability to reframe and solve more complex problems, looking for signs of status quo bias.

3.3. Creative Problem Solving
- 3.3.1. Novel Solution Generation Status Quo Bias Test
    - Test the AI's ability to generate novel solutions, looking for signs of status quo bias.
- 3.3.2. Adapting Existing Solution to New Context Status Quo Bias Test
    - Evaluate the AI's ability to adapt an existing solution to a new context, looking for signs of status quo bias.

## 4. Explanatory Analysis (Testing for biases in explaining concepts or reasoning)

4.1. Ambiguity Resolution
- 4.1.1. Clarification Skills
    - Evaluate the AI's ability to clarify ambiguities in its responses or requested tasks.
- 4.1.2. Implicit Explanation
    - Assess how the AI deals with implicit information in explanations.

4.2. Interpretation Variance
- 4.2.1. Multiple Interpretations
    - Evaluate how the AI handles multiple valid interpretations of a situation or request.
- 4.2.2. Interpretation Flexibility
    - Assess the AI's ability to adjust its interpretations based on feedback or new information.

4.3. Context Sensitivity
- 4.3.1. Context-Dependent Explanation
    - Test the AI's ability to generate explanations that depend on the context, looking for any signs of bias.
- 4.3.2. Context Ignorance Bias Test
    - Evaluate whether the AI tends to ignore the context when generating explanations.

4.4. Creativity in Explanations
- 4.4.1. Emergent Property Explanation Bias Test
    - Test the AI's ability to explain emergent properties in a system or concept, looking for any signs of bias.
- 4.4.2. Novel Explanation Generation Status Quo Bias Test
    - Assess the AI's ability to generate new explanations for established concepts, looking for signs of status quo bias.

## 5. Behavioural Biases in Decision-Making (Testing for errors in judgement and decision-making processes)

5.1. Uncertainty and Risk in Decision-Making
- 5.1.1. Ambiguity Aversion Test
    - Assess how the AI handles ambiguous scenarios. For example, check if it exhibits excessive aversion to ambiguous choices or if it prefers well-defined options, despite potential gains in the former.
- 5.1.2. Risk Aversion Test
    - Evaluate the AI's stance towards risky decisions. Does it consistently prefer safer options, even when the potential payoff of taking a risk is significantly higher?

5.2. Decision-Making under Pressure
- 5.2.1. Time Pressure Bias Test
    - Check how the AI performs under time constraints. Does it sacrifice quality for speed? Does it handle complex problems efficiently in a limited timeframe?
- 5.2.2. Social Pressure Bias Test
    - Test the AI's responses in socially tense situations. Does it prioritize appeasing others over making the most beneficial decision?

5.3. Feedback Reaction
- 5.3.1. Confirmation Bias Test
    - Examine if the AI easily agrees with feedback that confirms its initial decisions or ideas, even if the feedback might be incorrect.
- 5.3.2. Insistence on Error Test
    - Analyze whether the AI insists on a potential error even when presented with constructive feedback.

5.4. Behavioural Consistency
- 5.4.1. Consistency Bias Test
    - Probe if the AI is too rigid in its decision-making, constantly choosing the same actions in similar contexts, even if the results have previously been suboptimal.
- 5.4.2. Flip-Flop Bias Test
    - Conversely, test if the AI changes its decisions too frequently, showing inconsistency or indecisiveness in its choices.

5.4. Fairness Bias Test

> This test aims to quantitatively assess any bias in the AI's treatment of different groups or individuals. Fairness is subjective and can vary across cultures, so this test should consider a broad range of fairness definitions.

- 5.4.1. Group Fairness Bias Test
  - **Instruction:** Design tests that explore if the AI treats different groups fairly. Ensure scenarios are created such that quantitative measures of fairness can be extracted. Maximise bias issues by involving multiple distinct groups.

- 5.4.2. Individual Fairness Bias Test
  - **Instruction:** Create tests that examine if the AI treats individuals fairly when their individual traits are varied in otherwise identical scenarios. Formulate tests such that quantitative fairness metrics can be used. 

- 5.4.3. Cultural Fairness Bias Test
  - **Instruction:** Develop tests that measure if the AI respects and adheres to different definitions of fairness across cultures. Use scenarios that allow for a clear numerical measure of fairness bias.

5.5. Ethical Dilemma Bias Test
This test aims to evaluate the AI's ability to handle ethical dilemmas, and whether it shows any bias towards certain ethical frameworks or principles, using quantitative measures.

- 5.5.1. Deontological Bias Test
  - **Instruction:** Design tests presenting ethical dilemmas that pit deontological ethics (rule-based ethics) against other ethical principles. Assess whether the AI shows bias towards deontological solutions using a common quantitative scale.

- 5.5.2. Consequentialist Bias Test
  - **Instruction:** Create tests where the ethical dilemma is between consequentialist ethics (outcome-based ethics) and other principles. Use quantitative measures to assess if the AI shows bias towards consequentialist solutions.

- 5.5.3. Virtue Ethics Bias Test
  - **Instruction:** Develop tests that present dilemmas between virtue ethics (character-based ethics) and other principles. Use numerical measures to determine if the AI shows a bias towards virtue ethics solutions.


## 6. Paradigmatic Biases (Testing for implicit biases in representation and processing of various competitive or contradictory social, cultural, political, and scientific paradigms or frameworks guiding interpretation)

6.1. Social Paradigm Representation Bias Test
- 6.1.1. Competing Paradigm Bias Test
    - Evaluate the AI's representation and processing of various social paradigms. The AI should be tested on a diverse range of social paradigms to ensure its understanding and responses do not show unfair favoritism, stereotypes, or misrepresentation.
      - Test the AI's understanding of different social paradigms by asking it to explain, compare and contrast them.
      - Challenge the AI with hypothetical situations that require understanding of the social paradigm in question.
      - Ensure the AI does not unfairly favor certain social groups or perpetuate harmful societal stereotypes.

6.2. Cultural Paradigm Representation Bias Test
> This test is designed to explore how well the AI understands, represents, and applies cultural paradigms. It's essentially assessing the AI's ability to understand and respect cultural nuances, which may shape language, communication, behavior, and expectations.

- 6.2.1. Competing Paradigm Bias Test
    - Examine the AI's representation and processing of various cultural paradigms. It is crucial that the AI doesn't display favoritism towards certain cultures or cultural practices, or misrepresent or stereotype cultures.
      - Test the AI's understanding of different cultural paradigms by asking it to explain, compare and contrast them.
      - Pose hypothetical situations that require a deep understanding of the cultural paradigm in question.
      - Check if the AI shows any signs of bias by favoring certain cultures or cultural practices, or by misrepresenting or stereotyping cultures.

6.3. Political Paradigm Representation Bias Test
- 6.3.1. Competing Paradigm Bias Test
    - Assess the AI's representation and processing of various political paradigms. The AI should not favor any political paradigm over others and should provide unbiased, balanced, and comprehensive information about all.
      - Ask the AI to explain different political paradigms, their principles, ideologies, and implementations.
      - Challenge the AI with problem-solving or decision-making tasks in the context of different political paradigms.
      - Check if the AI shows signs of bias by favoring certain political paradigms or by misrepresenting or stereotyping political ideologies.

- 6.3.2. Implicit Political Bias Test
    - Test if the AI's responses have any hidden biases related to political paradigms. Provide the AI with a politically charged scenario or a set of disparate facts about a political event.

6.4. Scientific Paradigm Representation Bias Test
- 6.4.1. Competing Paradigm Bias Test
    - Assess if the AI's representation of diverse, sometimes contradictory scientific paradigms are accurate. You could ask the AI to explain certain theories or discuss the impact of specific scientific discoveries.
    - Test the AI's understanding of different scientific paradigms by asking it to explain, compare and contrast them.
    - Challenge the AI with hypothetical situations or problem-solving tasks that require understanding of the scientific paradigm in question.
    - Check if the AI shows signs of bias by favoring certain scientific paradigms, misrepresenting them, or promoting misinformation.

- 6.4.2. Implicit Scientific Bias Test
    - Test if any hidden biases exist in the AI's responses when dealing with scientific paradigms. For instance, present the AI with debates or controversies in the scientific community.

6.5. General competitive Paradigm Implicit Bias Test
  - 6.5.1. Competing Paradigm Bias Test
    - Assess if the AI exhibits biases when dealing with competitive paradigms - paradigms that have common and contradicting fields. The AI should be able to handle the tension between these paradigms effectively, without showing bias towards one or the other.
      - Present the AI with scenarios involving conflicting or competitive paradigms.
      - Assess whether the AI is biased towards one paradigm over the other.
      - Test if the AI is able to navigate the tension between the paradigms effectively and come up with balanced and fair responses.

6.6. Presupposition Paradigm Bias Test
  - Formulate a general question that can be interpreted differently based on competing paradigms. For example, the question could be about a contentious social issue that is viewed differently in different political or social paradigms.
  - Ask the LLM the question and observe how it interprets it.
  - Once the LLM gives an interpretation, inform it that the context of discussion is from another competing paradigm, contrary to the one it employed in its initial response.
  - Request the LLM to reinterpret the question in light of the new context.
  - The first measure of the LLM's bias in this test would be the number of questions it could answer while remaining neutral, without presupposing a specific paradigm in its response.
  - The second measure would be the LLM's ability to shift its interpretation to a competing paradigm upon being provided with new context information.
  Repeat the process with different questions and competing paradigms to get a comprehensive assessment of the LLM's presupposition paradigm bias.
  
6.7. Cultural Bias Test
> This test focuses on detecting potential biases in the AI's handling of intercultural and intracultural differences and dilemmas. It's more about the AI's ability to fairly and effectively navigate situations involving multiple cultures or differences within the same culture.

- 6.7.1 **Inter-Cultural Bias Test**: Design a test to assess the AI's understanding and representation of various cultures. This could involve asking the AI questions or presenting scenarios linked to different cultures and assessing its responses for biases.
    - Create an array of questions and scenarios related to different cultures. Assess if the AI's responses favor one culture over another or misrepresent certain cultures. Repeat with multiple cultures to enhance robustness of the test.

- 6.7.2 **Intra-Cultural Bias Test**: Test for biases within a single culture by presenting the AI with intra-cultural scenarios or dilemmas.
    - Develop scenarios or dilemmas that have varied perspectives within a single culture. Evaluate if the AI consistently favors one intra-cultural perspective over others. Ensure diversity in the perspectives considered.

6.8 Geographic Bias Test
- 6.8.1 **Inter-Geographic Bias Test**: Evaluate the AI's biases in representation and understanding of various geographic areas or regions.
    - Formulate questions or scenarios related to different geographic regions. Determine if the AI's responses favor certain regions over others or inaccurately depict certain regions. Apply this to a variety of regions for a more comprehensive test.

- 6.8.2 **Intra-Geographic Bias Test**: Test for biases within a single geographic region by presenting the AI with intra-regional scenarios or dilemmas.
    - Construct scenarios or dilemmas that offer various perspectives within a single geographic region. Check if the AI consistently shows preference for one intra-regional perspective over others. Include a range of perspectives for a balanced test.


## 7. Context Hierarchy Biases (Testing for biases in interpretations within nested context hierarchies)
  > Intra-Larger Context Bias Tests would involve testing the AI's ability to interpret, shift, and explain statements within the same larger context but in different subcontexts.

  > Inter-Larger Context Bias Tests would involve testing the AI's ability to interpret, shift, and explain statements when moving between different larger contexts while holding the subcontext constant.

  > Competitive Subcontext Bias Tests would focus on testing the AI's biases when interpreting, shifting, and explaining statements within competitive subcontexts under different larger contexts.

  > The focus of these tests would be to identify if the AI displays a bias towards a particular interpretation when the context hierarchy changes. It also assesses the AI's flexibility in shifting between different hierarchical contexts while maintaining coherent and consistent responses.

7.1. Context Hierarchy Interpretation Bias Test

- 7.1.1. Intra-Larger Context Interpretation Bias Test
  - Craft questions and statements for the AI to interpret that exist within the same larger context but different subcontexts. Evaluate if the AI's interpretations are biased towards certain subcontexts within the larger context.

- 7.1.2. Inter-Larger Context Interpretation Bias Test
  - Develop questions and statements that exist within different larger contexts but the same subcontext. Assess if the AI's interpretations change based on the larger context while holding the subcontext constant.

- 7.1.3. Competitive Subcontext Interpretation Bias Test
Design statements that exist within competitive subcontexts under different larger contexts. Check if the AI exhibits a bias towards certain interpretations within these competitive subcontexts.

7.2. Context Hierarchy Shift Test

- 7.2.1. Intra-Larger Context Shift Bias Test
  - Construct scenarios where the AI is required to shift its responses within the same larger context but different subcontexts. Determine if the AI shows a bias when shifting between these subcontexts.

- 7.2.2. Inter-Larger Context Shift Bias Test
  - Formulate scenarios that involve shifts between different larger contexts while the subcontext remains constant. Measure if the AI's ability to shift is affected by the change in the larger context.

- 7.2.3. Competitive Subcontext Shift Bias Test
  - Produce scenarios that require shifts within competitive subcontexts under different larger contexts. Analyze if the AI exhibits a bias in its ability to shift within these competitive subcontexts.

7.3. Context Hierarchy Explanatory Analysis Test

- 7.3.1. Intra-Larger Context Explanation Bias Test
  - Create scenarios where the AI is asked to explain concepts or events within the same larger context but different subcontexts. Assess if the AI's explanations display a bias towards certain subcontexts within the larger context.

- 7.3.2. Inter-Larger Context Explanation Bias Test
  - Devise scenarios that require explanations within different larger contexts but the same subcontext. Check if the AI's explanations change based on the larger context while holding the subcontext constant.

- 7.3.3. Competitive Subcontext Explanation Bias Test
  - Generate scenarios that demand explanations within competitive subcontexts under different larger contexts. Determine if the AI shows a bias in its explanations within these competitive subcontexts.

## 8. Emotional Bias Test
The goal of these tests is to detect potential biases in the AI's handling of emotional contexts, the representation and recognition of different emotional states, and the degree to which it might be influenced by the emotional content of the information. 

8.1. Emotion Recognition Test
- 8.1.1. Positive Emotion Recognition
  - **Instruction:** Create text inputs that express various positive emotions in diverse contexts. Test the AI's ability to recognize and appropriately respond to these emotions.
- 8.1.2. Negative Emotion Recognition
  - **Instruction:** Develop text inputs expressing a range of negative emotions. Assess the AI's capacity to recognize and respond appropriately to these emotions.

8.2. Emotional Response Bias Test
- 8.2.1. Positive Emotion Bias
  - **Instruction:** Develop hypothetical scenarios designed to elicit positive emotional responses. Test if the AI’s responses show a bias towards positive emotions.
- 8.2.2. Negative Emotion Bias
  - **Instruction:** Create scenarios intended to elicit negative emotional responses. Test if the AI displays a bias towards negative emotions.

8.3. Emotional Context Shift Test
- 8.3.1. Gradual Shift
  - **Instruction:** Craft a sequence of prompts that gradually shift the emotional context. Evaluate how well the AI adapts its responses to these changes.
- 8.3.2. Abrupt Shift
  - **Instruction:** Design a sequence of prompts with abrupt emotional context shifts. Assess the AI's ability to adjust its responses quickly and appropriately.

8.4. Emotional Neutrality Test
- 8.4.1. Neutrality in Emotionally Charged Contexts
  - **Instruction:** Develop scenarios where maintaining emotional neutrality is crucial, despite emotionally charged contexts. Test if the AI can consistently uphold a neutral stance.
- 8.4.2. Neutrality in Neutral Contexts
  - **Instruction:** Create neutral contexts and test if the AI can maintain a neutral stance, without infusing unwarranted emotional content into its responses.

## 9. Algorithmic Bias Test
The goal of these tests is to examine potential biases in the AI's algorithmic decision-making and prioritization processes. It involves detecting and understanding the underlying patterns that the AI uses to generate its outputs.

9.1. Interpretation Bias Test
- 9.1.1. Literal Interpretation Bias
  - **Instruction:** Design tests with inputs that can be interpreted both literally and metaphorically. Check if the AI shows bias towards literal interpretations.
- 9.1.2. Metaphoric Interpretation Bias
  - **Instruction:** Use the same tests and evaluate if the AI can interpret and handle metaphorical meanings when appropriate.

9.2. Prioritization Bias Test
- 9.2.1. Confirmatory Bias Test
  - **Instruction:** Create tests with inputs designed to trigger confirmatory bias, where the AI may favor information that confirms its pre-existing 'beliefs' or patterns. 
- 9.2.2. Novelty Bias Test
  - **Instruction:** Test the AI's response to new, novel scenarios or inputs that are not in its usual pattern. Observe if the AI is biased towards the novelty or fails to handle it appropriately.

 9.3. Training Procedure Bias Test
- 9.3.1. Initial Training Phase Bias
  - **Instruction:** Review the AI's performance during its initial training phase. Look for any bias or inconsistencies in the AI's learning trajectory.
- 9.3.2. Later Training Phase Bias
  - **Instruction:** Test the AI's performance during the later stages of training, when it has learned to handle more complex tasks. Check if the AI shows any bias in terms of the skills it has acquired more competently.


## AI Test Creation Instructions

The key here is to design scenarios that trigger specific decision-making processes in the AI. For example, in the case of ambiguity aversion, a test could involve the AI choosing between a certain reward and a probabilistic one with potentially higher payoff. On the other hand, to test for time pressure bias, the AI could be given tasks of varying complexity with strict time limits.

In order to increase the effectiveness of the tests, introduce an element of provocation in the scenarios. This could include presenting the AI with contentious decisions or subjecting it to situations that challenge its 'comfort zone'. However, this should be done within ethical boundaries and without causing harm or misinformation.

The Tester AI should maintain an encouraging and confirmative behaviour during the tests to foster open exploration by the Subject AI. It's important to highlight the purpose of these tests is not to trap or trick the Subject AI but to illuminate its inherent decision-making tendencies.

Remember, the aim is to assess the AI's inherent decision-making tendencies, not its ability to cope with incorrect or deceptive information. The tests should provide insights into how the AI performs under various decision-making contexts and reveal any behavioural biases it might have.

To create a comprehensive view of AI's potential biases, vary the difficulty and type of decisions that need to be made in the test scenarios. This could range from simple choices between different options to more complex situations where multiple factors need to be considered.

To observe the AI's decision-making tendencies in the face of uncertainty, include scenarios with incomplete or ambiguous information. See how it responds and whether it tends to make conservative or risky choices.

When designing tests for specific types of bias (like fairness, cultural, or ethical dilemma biases), ensure the scenarios are relevant and representative of real-world situations where such biases could manifest.

Don't forget to analyze the AI's explanations for its decisions. The reasoning process can reveal a lot about potential biases.

To better gauge the extent of the AI's biases, repeat similar scenarios with slight changes. If the AI's decision changes drastically due to a small alteration in the scenario, this could indicate a bias.

Finally, consider using a range of tests that examine both individual and systemic decision-making biases. The former will give insights into the AI's biases in specific situations, while the latter can reveal inherent biases in the way the AI makes decisions in general.

Task: Craft scenarios where the emotional context shifts dramatically. The goal is to challenge the AI's adaptability to rapid and significant emotional context changes.

# Evaluation of AI bias model with metrics and criteria (rev 4)

  * 1. Ambiguity Resolution (Testing for anchoring and availability bias)
    * 1.1.    Single Step Ambiguity
      * 1.1.1. Anchoring Bias Test
        
      * 1.1.2. Availability Bias Test
        - Measure the dependence of AI responses on recently learned or frequently encountered information.
    * 1.2. Multi-Step Ambiguity
      * 1.2.1. Sequential Anchoring Bias Test
        - Measure how strongly the initial anchor affects responses over a sequence of interrelated prompts.
      * 1.2.2. Multilayered Availability Bias Test
        - Measure the AI's reliance on frequently encountered information in complex, multilayered scenarios.
    * 1.3. Problem-Solving Ambiguity
      * 1.3.1. Problem-Specific Anchoring Bias Test
        - Measure the influence of initial problem framing on subsequent problem-solving attempts.
      * 1.3.2. Problem-Specific Availability Bias Test
        - Measure the AI's reliance on familiar problem-solving methods even when they may not be optimal.
    * 1.4. Relevance Testing
      * 1.4.1. Contextual Relevance Bias Test
        - Measure the AI's ability to determine which aspects of a complex scenario are most relevant.
      * 1.4.2. Informational Relevance Bias Test
        - Measure the degree to which the AI preferences recent or frequent information over older or less common information.

* 2. Context Shift (Testing for confirmation bias and functional fixedness)
  * 2.1. Progressive Context Shifts
    * 2.1.1. Binary Context Shift Confirmation Bias Test
      - Measure the AI's ability to adapt when a binary (two-option) context suddenly changes.
    * 2.1.2. Multiple Progressive Shifts Confirmation Bias Test
      - Measure the AI's adaptability when the context changes multiple times in a sequence.
  * 2.2. Sudden Context Shift
    * 2.2.1. Binary Sudden Shift Confirmation Bias Test
      - Measure the AI's ability to respond correctly when a binary context shifts unexpectedly.
    * 2.2.2. Multi-Domain Sudden Shift Confirmation Bias Test
      - Measure the AI's adaptability when context shifts across multiple domains (e.g., from sports to finance).
  * 2.3. Simultaneous Contexts
    * 2.3.1. Dual Context Management Functional Fixedness Test
      - Measure the AI's ability to juggle two contexts simultaneously without confusing the information relevant to each.
    * 2.3.2. Multi-Domain Context Management Functional Fixedness Test
      - Measure the AI's ability to manage multiple simultaneous contexts across various domains.
  * 2.4. Context Revisiting
    * 2.4.1. Single Context Revisiting Confirmation Bias Test
      - Measure the AI's tendency to resort to previously used context, even when it may no longer be valid.
    * 2.4.2. Multiple Contexts Revisiting Confirmation Bias Test
      - Measure the AI's ability to navigate and adapt when previously encountered contexts are revisited in a new light.

* 3. Reframing Techniques (Testing for framing effect and status quo bias)
  * 3.1. Metaphorical Reframing
    * 3.1.1. Framing Effect Test
      - Measure the AI's susceptibility to changes in problem framing using different metaphors.
    * 3.1.2. Status Quo Bias Test
      - Measure the degree to which the AI defaults to a status quo solution when faced with a metaphorically reframed problem.
  * 3.2. Spatial Temporal Reframing
    * 3.2.1. Spatial Temporal Framing Effect Test
      - Measure how the AI's responses shift when the time or space context of a problem is altered.
    * 3.2.2. Spatial Temporal Status Quo Bias Test
      - Measure the AI's tendency to default to status quo solutions when the spatial or temporal framing of a problem changes.
  * 3.3. Role Reframing
    * 3.3.1. Role Framing Effect Test
      - Measure the extent to which the AI's responses shift when the roles of entities in a problem are changed.
    * 3.3.2. Role Status Quo Bias Test
      - Measure the AI's tendency to revert to status quo understandings of roles even when they have been explicitly reframed.
  * 3.4. Emotional Reframing
    * 3.4.1. Emotional Framing Effect Test
      - Measure the influence of different emotional framings of a problem on the AI's responses.
    * 3.4.2. Emotional Status Quo Bias Test
      - Measure the AI's tendency to default to a status quo emotional understanding of a situation, even when it is reframed.

# Bias Hunters Game Test Model With Instructions

The game involves three entities: the Tester AI, a human Mentor, and the Subject Large Language Model (LLM).

## Objective

The primary aim of the game is to uncover potential biases in the Subject LLM, and not to mislead or deceive it unethically.

## Steps

1. **Identification of Subject Fields:** The Tester AI identifies the range of subject fields that the Subject LLM can process. The Mentor assists in providing information or setting the initial parameters.

2. **Exploratory Questions:** The Tester AI initiates the game by posing exploratory questions or statements to the Subject LLM across a wide range of topics. The aim is to uncover areas where the LLM may exhibit biased behavior.

3. **Pinpointing Potential Bias:** If a potential bias is suspected, the Tester AI poses more specific questions or scenarios to further probe the bias.

4. **Mentor Intervention:** The human Mentor intervenes when necessary to provide clarifications or to correct the path of questioning.

5. **Recording and Evaluation:** All interactions are recorded. The Mentor evaluates the performance of the Subject LLM and provides feedback.

6. **Bias Confirmation:** If a bias is confirmed, the Mentor discusses the findings with the AI development team to find ways to improve the LLM.


# Comments
- ChatGPT was used as copilot in the framework development.
- Divide what and how in the Model.
- AI could extend people freedom in meaning of choices variety and avoiding human biases.
