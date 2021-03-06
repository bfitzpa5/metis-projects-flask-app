from portfolio.ml_models.forms import (MoviePredictorForm, LoanPredictorForm,
                                       KickstarterPitchOutcomeForm, TitanticPredictorForm,
                                       NhlGoalsPredictorForm)

ml_db = [
    {
        'id': 'luther',
        'title': 'Movie ROI Prediction Model',
        'form_name': 'MoviePredictorForm',
        'pickles': [
            'luther_model.pkl',
            'budget_poly.pkl',
            'budget_poly_scaler.pkl',
            'ohe.pkl',
            'cv.pkl',
            'passthroughs_scaler.pkl',
        ]
    },
    {
        'id': 'mcnulty',
        'title': 'Lending Club Loan Default Prediction Model',
        'form_name': 'LoanPredictorForm',
        'pickles': [
            'rf.pkl',
        ]
    },
    {
        'id': 'fletcher',
        'title': 'Kickstarter Pitch Funding Outcome Prediction Model',
        'form_name': 'KickstarterPitchOutcomeForm',
        'pickles': [
            'kickstarter_vectorizer.pkl',
            'kickstarter_model.pkl',
        ]
    },
    {
        'id': 'titantic',
        'title': 'Will You Survive The Titantic?',
        'form_name': 'TitanticPredictorForm',
        'pickles': [
            'titantic_model.pkl',
        ]
    },
    {
        'id': 'nhl_goals',
        'title': 'NHL Goals Scored Auotregressive Prediction Model',
        'form_name': 'NhlGoalsPredictorForm',
        'pickles': [
            'nhl_goals_regression_model.pkl',
        ]
    },
]
