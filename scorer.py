"""
The scorer: decides whether an answer was right.

`run_eval.py` finds this file and calls `judge()` once per run. An answer
passes when it contains the question's `expects` phrase from questions.py,
ignoring case. A refusal never passes.
"""

from gate import REFUSAL


def judge(question, expects, answer, results) -> bool:
    """Pass if the answer isn't a refusal and contains the expected phrase."""
    if not expects or not answer or answer.strip() == REFUSAL:
        return False
    return expects.lower() in answer.lower()
