class CareerRecommender:
    def __init__(self):
        self.career_matches = {
            "high_openness": {
                "high_conscientiousness": {
                    "high_extraversion": ["Scientist", "University Professor", "Architect", "Creative Director", "Entrepreneur"],
                    "low_extraversion": ["Research Scientist", "Writer/Author", "Software Developer", "Data Scientist", "Artist"]
                },
                "low_conscientiousness": {
                    "high_extraversion": ["Journalist", "Creative Consultant", "Marketing Specialist", "Actor", "Travel Blogger"],
                    "low_extraversion": ["Freelance Writer", "Independent Artist", "Philosopher", "Game Designer", "Musician"]
                }
            },
            "low_openness": {
                "high_conscientiousness": {
                    "high_extraversion": ["Project Manager", "Financial Advisor", "Sales Manager", "Operations Manager", "Police Officer"],
                    "low_extraversion": ["Accountant", "Logistics Coordinator", "Database Administrator", "Financial Analyst", "Quality Assurance Specialist"]
                },
                "low_conscientiousness": {
                    "high_extraversion": ["Sales Representative", "Customer Service", "Tour Guide", "Event Staff", "Retail Manager"],
                    "low_extraversion": ["Security Guard", "Machine Operator", "Driver", "Assembly Line Worker", "Data Entry Specialist"]
                }
            },
            "moderate_openness": {
                "moderate_conscientiousness": {
                    "moderate_extraversion": ["Teacher", "Nurse", "HR Manager", "Marketing Analyst", "Social Worker"]
                }
            }
        }
        self.career_modifiers = {
            "high_agreeableness": ["Counselor", "Nurse", "Social Worker", "Teacher", "Veterinarian", "HR Specialist", "Customer Support", "Nonprofit Director"],
            "low_agreeableness": ["Lawyer", "Surgeon", "Investment Banker", "Management Consultant", "Corporate Executive", "Criminal Prosecutor", "Critic"],
            "high_neuroticism": ["Artist", "Writer", "Researcher", "Editor", "Quality Control Specialist"],
            "low_neuroticism": ["Emergency Medical Technician", "Pilot", "Firefighter", "Police Officer", "Military Officer", "Surgeon", "Air Traffic Controller"]
        }

    def _get_level_category(self, score):
        if score >= 70: return "high"
        if score <= 30: return "low"
        return "moderate"

    def get_career_recommendations(self, scores):
        openness = self._get_level_category(scores["openness"])
        conscientiousness = self._get_level_category(scores["conscientiousness"])
        extraversion = self._get_level_category(scores["extraversion"])
        agreeableness = self._get_level_category(scores["agreeableness"])
        neuroticism = self._get_level_category(scores["neuroticism"])

        try:
            main = self.career_matches[f"{openness}_openness"][f"{conscientiousness}_conscientiousness"][f"{extraversion}_extraversion"]
        except KeyError:
            main = self.career_matches["moderate_openness"]["moderate_conscientiousness"]["moderate_extraversion"]

        modifiers = []
        modifiers.extend(self.career_modifiers.get(f"{agreeableness}_agreeableness", []))
        modifiers.extend(self.career_modifiers.get(f"{neuroticism}_neuroticism", []))

        best = [c for c in main if c in modifiers]
        if not best:
            best = main[:3] + modifiers[:2]
        return {"recommendations": best[:5], "explanations": []}
