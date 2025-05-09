class PersonalityTest:
    def __init__(self):
        self.questions = {
            "openness": [
                {"id": "o1", "question": "I have a rich vocabulary.", "reverse": False},
                {"id": "o2", "question": "I have difficulty understanding abstract ideas.", "reverse": True},
                {"id": "o3", "question": "I have a vivid imagination.", "reverse": False},
                {"id": "o4", "question": "I am not interested in abstract ideas.", "reverse": True},
                {"id": "o5", "question": "I have excellent ideas.", "reverse": False},
                {"id": "o6", "question": "I do not have a good imagination.", "reverse": True},
                {"id": "o7", "question": "I am quick to understand things.", "reverse": False},
                {"id": "o8", "question": "I use difficult words.", "reverse": False},
                {"id": "o9", "question": "I spend time reflecting on things.", "reverse": False},
                {"id": "o10", "question": "I am full of ideas.", "reverse": False}
            ],
            "conscientiousness": [
                {"id": "c1", "question": "I am always prepared.", "reverse": False},
                {"id": "c2", "question": "I leave my belongings around.", "reverse": True},
                {"id": "c3", "question": "I pay attention to details.", "reverse": False},
                {"id": "c4", "question": "I make a mess of things.", "reverse": True},
                {"id": "c5", "question": "I get chores done right away.", "reverse": False},
                {"id": "c6", "question": "I often forget to put things back in their proper place.", "reverse": True},
                {"id": "c7", "question": "I like order.", "reverse": False},
                {"id": "c8", "question": "I shirk my duties.", "reverse": True},
                {"id": "c9", "question": "I follow a schedule.", "reverse": False},
                {"id": "c10", "question": "I am exacting in my work.", "reverse": False}
            ],
            "extraversion": [
                {"id": "e1", "question": "I am the life of the party.", "reverse": False},
                {"id": "e2", "question": "I don't talk a lot.", "reverse": True},
                {"id": "e3", "question": "I feel comfortable around people.", "reverse": False},
                {"id": "e4", "question": "I keep in the background.", "reverse": True},
                {"id": "e5", "question": "I start conversations.", "reverse": False},
                {"id": "e6", "question": "I have little to say.", "reverse": True},
                {"id": "e7", "question": "I talk to a lot of different people at parties.", "reverse": False},
                {"id": "e8", "question": "I don't like to draw attention to myself.", "reverse": True},
                {"id": "e9", "question": "I don't mind being the center of attention.", "reverse": False},
                {"id": "e10", "question": "I am quiet around strangers.", "reverse": True}
            ],
            "agreeableness": [
                {"id": "a1", "question": "I feel others' emotions.", "reverse": False},
                {"id": "a2", "question": "I am not really interested in others.", "reverse": True},
                {"id": "a3", "question": "I make people feel at ease.", "reverse": False},
                {"id": "a4", "question": "I insult people.", "reverse": True},
                {"id": "a5", "question": "I sympathize with others' feelings.", "reverse": False},
                {"id": "a6", "question": "I am not interested in other people's problems.", "reverse": True},
                {"id": "a7", "question": "I have a soft heart.", "reverse": False},
                {"id": "a8", "question": "I am not really interested in others.", "reverse": True},
                {"id": "a9", "question": "I take time out for others.", "reverse": False},
                {"id": "a10", "question": "I feel little concern for others.", "reverse": True}
            ],
            "neuroticism": [
                {"id": "n1", "question": "I get stressed out easily.", "reverse": False},
                {"id": "n2", "question": "I am relaxed most of the time.", "reverse": True},
                {"id": "n3", "question": "I worry about things.", "reverse": False},
                {"id": "n4", "question": "I seldom feel blue.", "reverse": True},
                {"id": "n5", "question": "I am easily disturbed.", "reverse": False},
                {"id": "n6", "question": "I get upset easily.", "reverse": False},
                {"id": "n7", "question": "I change my mood a lot.", "reverse": False},
                {"id": "n8", "question": "I have frequent mood swings.", "reverse": False},
                {"id": "n9", "question": "I get irritated easily.", "reverse": False},
                {"id": "n10", "question": "I often feel blue.", "reverse": False}
            ]
        }

    def get_all_questions(self):
        all_questions = []
        for trait, questions in self.questions.items():
            for q in questions:
                question_data = {
                    "id": q["id"],
                    "question": q["question"],
                    "trait": trait,
                    "reverse": q["reverse"]
                }
                all_questions.append(question_data)
        return all_questions

    def calculate_scores(self, answers):
        scores = {trait: 0 for trait in self.questions}
        counts = {trait: 0 for trait in self.questions}
        for q_id, answer in answers.items():
            for trait, questions in self.questions.items():
                for q in questions:
                    if q["id"] == q_id:
                        value = int(answer)
                        if q["reverse"]:
                            value = 6 - value
                        scores[trait] += value
                        counts[trait] += 1
                        break
        for trait in scores:
            if counts[trait] > 0:
                min_score = counts[trait]
                max_score = counts[trait] * 5
                scores[trait] = round(((scores[trait] - min_score) / (max_score - min_score)) * 100)
        return scores

    def get_personality_profile(self, scores):
        profile = {
            'openness': {
                'description': self._get_openness_description(scores['openness'])
            },
            'conscientiousness': {
                'description': self._get_conscientiousness_description(scores['conscientiousness'])
            },
            'extraversion': {
                'description': self._get_extraversion_description(scores['extraversion'])
            },
            'agreeableness': {
                'description': self._get_agreeableness_description(scores['agreeableness'])
            },
            'neuroticism': {
                'description': self._get_neuroticism_description(scores['neuroticism'])
            }
        }
        return profile

    def _get_openness_description(self, score):
        if score >= 75:
            return "You score high in openness to experience. You're curious, imaginative, and open to trying new things. You value creativity, innovation, and intellectual stimulation. You're likely to enjoy art, music, and cultural experiences."
        elif score >= 50:
            return "You have a moderate level of openness. You appreciate both new experiences and traditions. You can be creative and practical depending on the situation, making you adaptable to various environments."
        else:
            return "You score lower in openness. You're practical, conventional, and prefer familiar routines. You value tradition and consistency, and may approach problems with established solutions rather than experimental ones."

    def _get_conscientiousness_description(self, score):
        if score >= 75:
            return "You score high in conscientiousness. You're organized, responsible, and dependable. You prefer planned activities over spontaneity and excel at setting and achieving long-term goals. You're likely to be punctual and detail-oriented."
        elif score >= 50:
            return "You have a moderate level of conscientiousness. You can be organized when needed but also allow for flexibility. You balance work and leisure effectively and can adapt to both structured and unstructured environments."
        else:
            return "You score lower in conscientiousness. You're flexible, spontaneous, and prefer to keep your options open. You may find rigid schedules restrictive and prefer to approach tasks as they come rather than planning extensively."

    def _get_extraversion_description(self, score):
        if score >= 75:
            return "You score high in extraversion. You're outgoing, energetic, and draw energy from social interactions. You enjoy being around people, are comfortable in group settings, and often take the initiative in social situations."
        elif score >= 50:
            return "You have a moderate level of extraversion. You enjoy social activities but also value your alone time. You're comfortable in group settings but may also appreciate deeper one-on-one conversations and quiet reflection."
        else:
            return "You score lower in extraversion. You're more reserved and may prefer quiet, low-key environments. You value deep connections with a few close friends over large social gatherings and may need time alone to recharge after social events."

    def _get_agreeableness_description(self, score):
        if score >= 75:
            return "You score high in agreeableness. You're compassionate, cooperative, and prioritize getting along with others. You tend to trust people and value harmony in relationships. You're likely to be helpful and willing to compromise for the sake of the group."
        elif score >= 50:
            return "You have a moderate level of agreeableness. You can be cooperative but also stand up for yourself when necessary. You balance compassion with healthy boundaries and can adapt your approach based on social context."
        else:
            return "You score lower in agreeableness. You're straightforward, direct, and may prioritize honesty over tact. You're likely to be competitive and skeptical, which can be valuable for critical thinking and negotiation."

    def _get_neuroticism_description(self, score):
        if score >= 75:
            return "You score higher in emotional sensitivity. You experience emotions deeply and may be more responsive to stress. This sensitivity can make you empathetic and attuned to subtle emotional cues in yourself and others."
        elif score >= 50:
            return "You have a moderate level of emotional sensitivity. You experience a normal range of emotions but generally maintain emotional balance. You're likely to be resilient while still being aware of your feelings."
        else:
            return "You score lower in emotional sensitivity. You're calm, steady, and not easily upset by stressful situations. You bounce back quickly from setbacks and maintain emotional stability even under pressure."
