from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from personality_test import PersonalityTest
from career_recommender import CareerRecommender
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

personality_test = PersonalityTest()
career_recommender = CareerRecommender()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assessment', methods=['GET'])
def assessment():
    questions = personality_test.get_all_questions()
    import random; random.shuffle(questions)
    return render_template('assessment.html', questions=questions)

@app.route('/submit_assessment', methods=['POST'])
def submit_assessment():
    answers = {key: value for key, value in request.form.items() if key.startswith(('o','c','e','a','n'))}
    scores = personality_test.calculate_scores(answers)
    
    # Get the profile from the personality test
    profile = personality_test.get_personality_profile(scores)
    
    # Safety check - ensure profile has the correct structure
    # If get_personality_profile was updated with our implementation, this won't be needed
    # But it's a good safety net
    traits = ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism']
    for trait in traits:
        if trait not in profile:
            profile[trait] = {}
        if not isinstance(profile[trait], dict):
            temp_value = profile[trait]
            profile[trait] = {'description': temp_value}
        if 'description' not in profile[trait]:
            profile[trait]['description'] = f"Description for {trait} not available"
    
    career_data = career_recommender.get_career_recommendations(scores)
    session['scores'], session['profile'], session['career_data'] = scores, profile, career_data
    return redirect(url_for('results'))

@app.route('/results')
def results():
    if 'scores' not in session:
        return redirect(url_for('assessment'))
    
    return render_template('results.html',
                          scores=session['scores'],
                          profile=session['profile'],
                          recommendations=session['career_data']['recommendations'],
                          explanations=session['career_data']['explanations'])

if __name__ == '__main__':
    app.run(debug=True)
