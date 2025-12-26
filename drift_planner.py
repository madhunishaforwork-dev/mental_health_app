import random

def classify_context(text):
    """
    Classifies the context of the stress based on keywords.
    Returns: 'Academic', 'Career', or 'General'
    """
    text = text.lower()
    
    academic_keywords = ['exam', 'study', 'test', 'grade', 'school', 'university', 'college', 'assignment', 'homework', 'fail']
    career_keywords = ['job', 'work', 'boss', 'deadline', 'career', 'promotion', 'interview', 'salary', 'office', 'colleague']
    
    for word in academic_keywords:
        if word in text:
            return 'Academic'
            
    for word in career_keywords:
        if word in text:
            return 'Career'
            
    return 'General'

def generate_plan(emotion, risk_level, text):
    """
    Generates a structured solution journey based on emotion, risk, and context.
    """
    context = classify_context(text)
    
    plan = {
        'solution_type': '',
        'plan_title': '',
        'duration': '',
        'steps': []
    }

    # Deterministic logic for plan selection
    if risk_level == 'High' or emotion == 'Depressed':
        plan['solution_type'] = 'Trip / Reset Planner'
        plan['plan_title'] = 'Mental Reset & Recovery Protocol'
        plan['duration'] = '3 Days'
        plan['steps'] = [
            {'day': 'Day 1', 'activity': 'Complete Digital Detox. No social media. Spend 1 hour in nature.', 'focus': 'Disconnect'},
            {'day': 'Day 2', 'activity': 'Journaling session: Write down 3 stressors and burn the paper.', 'focus': 'Release'},
            {'day': 'Day 3', 'activity': 'Light social interaction with a trusted friend or family member.', 'focus': 'Reconnect'}
        ]
        
    elif context == 'Academic':
        plan['solution_type'] = 'Study Planner'
        plan['plan_title'] = 'Academic Focus & Balance Strategy'
        plan['duration'] = '1 Week'
        plan['steps'] = [
            {'day': 'Daily Routine', 'activity': 'Pomodoro Technique: 25min study, 5min break. Max 4 cycles.', 'focus': 'Focus'},
            {'day': 'Environment', 'activity': 'Clear desk of all non-essential items. Ensure good lighting.', 'focus': 'Clarity'},
            {'day': 'Resource', 'activity': 'Review summary notes before deep diving into textbooks.', 'focus': 'Efficiency'}
        ]
        
    elif context == 'Career':
        plan['solution_type'] = 'Job / Skill Planner'
        plan['plan_title'] = 'Career Growth & Stress Management'
        plan['duration'] = '2 Weeks'
        plan['steps'] = [
            {'day': 'Week 1 Goal', 'activity': 'Identify top 3 skills needed for next promotion/role.', 'focus': 'Strategy'},
            {'day': 'Daily Habit', 'activity': 'First 90 mins of work on most difficult task. No emails.', 'focus': 'Productivity'},
            {'day': 'Networking', 'activity': 'Connect with 1 peer or mentor this week for a casual chat.', 'focus': 'Growth'}
        ]
        
    else:
        # Default General Plan (Low/Medium Risk, General Context)
        plan['solution_type'] = 'Wellness Journey'
        plan['plan_title'] = 'Daily Mindfulness & Joy'
        plan['duration'] = 'Ongoing'
        plan['steps'] = [
            {'day': 'Morning', 'activity': '5 minutes of deep breathing or meditation.', 'focus': 'Calm'},
            {'day': 'Afternoon', 'activity': 'Short walk or stretching break.', 'focus': 'Energy'},
            {'day': 'Evening', 'activity': 'List 3 things you are grateful for today.', 'focus': 'Gratitude'}
        ]
        
    return plan
