"""
Liam Michael Bailey
17/06/2023
SkillCorner Normalisations.
This file contains functions to add different normalisations for SkillCorner
Game Intelligence Data. Included are functions for per 90, per adjusted 30
min tip, per 100 actions.
"""


# Gets per 90 values for a given metric.
def get_per_90(df, metric_per_match):
    return df[metric_per_match] / (df['minutes_played_per_match'] / 90)


# Gets per 30 tip values for a given metric.
def get_per_30_tip(df, metric_per_match):
    return df[metric_per_match] / (df['adjusted_min_tip_per_match'] / 30)


# Gets per 100 values for a given metric & adjustment metric.
def get_per_100(df, metric_per_match, adjustment_metric_per_match):
    return df[metric_per_match] / (df[adjustment_metric_per_match] / 100)


# Gets p30 tip metrics for all count metrics.
def add_per_30_tip_metrics(df):
    metrics = []
    for col in df.columns:
        if 'count_' in col and 'per_match' in col:
            df[col.replace('per_match', 'per_30_tip')] = get_per_30_tip(df, col)
            metrics.append(col.replace('per_match', 'per_30_tip'))

    return df, metrics
