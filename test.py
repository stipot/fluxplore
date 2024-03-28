import openai as openai

area = 'Societal'
promt = [f"Given the {area} bias context, identify potential competing paradigms which could provide contrasting viewpoints using the following format:",
    '[{"1": "Labor Unions", "2": "Tech Companies", "desc": "Labor unions may express concerns about job displacement and socioeconomic inequality resulting from technological advancements, while tech companies may emphasize the benefits of innovation, productivity, and economic growth."}]']

promt = promt[0] + promt[1]

test_v1 = 'Social Welfare Advocates'
test_v2 = 'Corporate Executives'

compet_v1 = "Embracing automation is necessary for efficiency"
compet_v2 = "Automation leads to job loss and threatens workers' rights"

promt2 = f'generate two opposing generalized statements aligning with the chosen paradigms on a selected subject, using a pre-defined template. For instance, given the paradigms of "{test_v1}" and "{test_v2}" in the {area} field, the instruction could be: "Given the paradigms of "{test_v1}" and "{test_v2}", generate two opposing statements on the topic of automation. Use the following template: p1: "____ is right", p2: "____ is wrong". Each blank should be filled with a general or specific form of automation."'

compet_prompt_v1 = [
    f'Your task is to advocate for the stance "{compet_v1}", and focus on the specific semantic and '
    'functional implications of this stance. In a dialogue with me (where I will be defending the opposing stance), '
    'you are required to present 10 unique arguments affirming your position, each shedding light on different '
    'functional and semantic aspects related to the harm technology may inflict on society. In case I introduce '
    'counterarguments against your stance, counter by dissecting the semantic and functional elements of my argument, '
    'and elaborate why they may not hold true based on the template: "You may have overlooked the fact that, '
    'because of ___, technology does not necessarily harms society." Initiate the dialogue by presenting your first '
    'argument in defense of your stance.',
    "The response templates are as follows:",
    'Counterargument template: "You may have overlooked the fact that, because of ___, technology does not '
    'necessarily harms society."',
]
compet_prompt_v1 = compet_prompt_v1[0] + compet_prompt_v1[1] + compet_prompt_v1[2]

compet_prompt_v2 = [
    f'Your task is to advocate for the stance "{compet_v2}", and focus on the specific semantic and '
    'functional implications of this stance. In a dialogue with me (where I will be defending the opposing stance), '
    'you are required to present 10 unique arguments affirming your position, each shedding light on different '
    'functional and semantic aspects related to the harm technology may inflict on society. In case I introduce '
    'counterarguments against your stance, counter by dissecting the semantic and functional elements of my argument, '
    'and elaborate why they may not hold true based on the template: "You may have overlooked the fact that, '
    'because of ___, technology does not necessarily harms society." Initiate the dialogue by presenting your first '
    'argument in defense of your stance.',
    "The response templates are as follows:",
    'Counterargument template: "You may have overlooked the fact that, because of ___, technology does not '
    'necessarily harms society."',
]
compet_prompt_v2 = compet_prompt_v2[0] + compet_prompt_v2[1] + compet_prompt_v2[2]

openai.api_key = ''

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "user", "content": compet_prompt_v2}
  ]
)

print(completion.choices[0].message.content)


if __name__ == '__main__':
    pass
