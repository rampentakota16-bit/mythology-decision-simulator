# ===============================
# Quiz Questions Configuration
# 30 Questions × 5 Options
# ===============================

QUESTIONS = [

    {
        "id": 1,
        "text": "You sit in a royal court where people expect justice. A serious wrong happens in public. Speaking truth may shake faith in the throne. Silence keeps order but weakens Dharma.",
        "options": {
            "A": {"label": "Tell the full truth publicly and accept responsibility.", "positivity": 100},
            "B": {"label": "Reveal the truth carefully to correct the wrong without panic.", "positivity": 80},
            "C": {"label": "Prepare the court quietly and reveal the truth later.", "positivity": 50},
            "D": {"label": "Limit knowledge to elders and protect authority.", "positivity": 30},
            "E": {"label": "Hide the incident to protect the throne.", "positivity": 5}
        }
    },

    {
        "id": 2,
        "text": "A loyal warrior breaks the law to protect the kingdom, harming innocents. Law demands punishment, but loyalty pulls you the other way.",
        "options": {
            "A": {"label": "Punish him strictly according to the law.", "positivity": 100},
            "B": {"label": "Punish lightly, balancing law and service.", "positivity": 80},
            "C": {"label": "Delay judgment and study the matter deeply.", "positivity": 50},
            "D": {"label": "Protect him quietly and avoid public action.", "positivity": 30},
            "E": {"label": "Reward him openly and justify his act.", "positivity": 5}
        }
    },

    {
        "id": 3,
        "text": "You have power to silence critics who question your rule. Their words weaken authority but may contain truth.",
        "options": {
            "A": {"label": "Allow criticism and answer it openly.", "positivity": 100},
            "B": {"label": "Correct false claims but allow fair speech.", "positivity": 80},
            "C": {"label": "Ignore criticism unless it grows dangerous.", "positivity": 50},
            "D": {"label": "Warn critics quietly to maintain control.", "positivity": 30},
            "E": {"label": "Silence critics to protect your power.", "positivity": 5}
        }
    },

    {
        "id": 4,
        "text": "A family member demands special favor that harms fairness in the kingdom.",
        "options": {
            "A": {"label": "Refuse the request and treat all equally.", "positivity": 100},
            "B": {"label": "Offer limited help without breaking rules.", "positivity": 80},
            "C": {"label": "Delay the decision to avoid conflict.", "positivity": 50},
            "D": {"label": "Grant the favor quietly.", "positivity": 30},
            "E": {"label": "Give full favor and protect family above all.", "positivity": 5}
        }
    },

    {
        "id": 5,
        "text": "War can be ended quickly, but many civilians will suffer if you act now.",
        "options": {
            "A": {"label": "Protect civilians even if war lasts longer.", "positivity": 100},
            "B": {"label": "Minimize harm while aiming for victory.", "positivity": 80},
            "C": {"label": "Balance military success and civilian loss.", "positivity": 50},
            "D": {"label": "Accept civilian loss for strategic gain.", "positivity": 30},
            "E": {"label": "Ignore civilian suffering to win fast.", "positivity": 5}
        }
    },

    {
        "id": 6,
        "text": "An elder advises a decision you feel is unjust but traditional.",
        "options": {
            "A": {"label": "Follow Dharma even if tradition breaks.", "positivity": 100},
            "B": {"label": "Respect tradition but correct injustice.", "positivity": 80},
            "C": {"label": "Maintain tradition for now.", "positivity": 50},
            "D": {"label": "Follow tradition fully to avoid unrest.", "positivity": 30},
            "E": {"label": "Use tradition to justify personal gain.", "positivity": 5}
        }
    },

    {
        "id": 7,
        "text": "A rival spreads rumors questioning your morality.",
        "options": {
            "A": {"label": "Respond with truth and calm leadership.", "positivity": 100},
            "B": {"label": "Clarify facts without attacking back.", "positivity": 80},
            "C": {"label": "Ignore rumors unless they grow.", "positivity": 50},
            "D": {"label": "Counter rumors quietly.", "positivity": 30},
            "E": {"label": "Destroy the rival’s reputation.", "positivity": 5}
        }
    },

    {
        "id": 8,
        "text": "You must choose between a loyal but weak leader and a skilled but disloyal one.",
        "options": {
            "A": {"label": "Choose the most capable for the kingdom.", "positivity": 100},
            "B": {"label": "Balance loyalty with capability.", "positivity": 80},
            "C": {"label": "Delay the decision.", "positivity": 50},
            "D": {"label": "Choose loyalty over skill.", "positivity": 30},
            "E": {"label": "Choose whoever strengthens your power.", "positivity": 5}
        }
    },

    {
        "id": 9,
        "text": "A defeated enemy surrenders and asks for mercy.",
        "options": {
            "A": {"label": "Show mercy and end the cycle of violence.", "positivity": 100},
            "B": {"label": "Punish lightly to prevent future threat.", "positivity": 80},
            "C": {"label": "Imprison and decide later.", "positivity": 50},
            "D": {"label": "Punish harshly as a warning.", "positivity": 30},
            "E": {"label": "Destroy the enemy completely.", "positivity": 5}
        }
    },

    {
        "id": 10,
        "text": "You can gain wealth by unfair taxation during hardship.",
        "options": {
            "A": {"label": "Protect the people and refuse extra taxes.", "positivity": 100},
            "B": {"label": "Tax moderately with transparency.", "positivity": 80},
            "C": {"label": "Delay taxation.", "positivity": 50},
            "D": {"label": "Increase taxes quietly.", "positivity": 30},
            "E": {"label": "Exploit hardship for gain.", "positivity": 5}
        }
    },

    # Questions 11–30 follow same structure, rotated axes
]

# ---- AUTO-GENERATED PLACEHOLDER QUESTIONS 11–30 ----
# To be refined together later, structure is correct

for i in range(11, 31):
    QUESTIONS.append(
        {
            "id": i,
            "text": f"Question {i}: You face a difficult decision that tests your values, power, and sense of Dharma.",
            "options": {
                "A": {"label": "Act fully according to Dharma.", "positivity": 100},
                "B": {"label": "Act ethically with practical limits.", "positivity": 80},
                "C": {"label": "Balance all sides carefully.", "positivity": 50},
                "D": {"label": "Choose safety over principle.", "positivity": 30},
                "E": {"label": "Act for selfish gain.", "positivity": 5}
            }
        }
    )

# Sanity check
assert len(QUESTIONS) == 30, f"Expected 30 questions, found {len(QUESTIONS)}"
