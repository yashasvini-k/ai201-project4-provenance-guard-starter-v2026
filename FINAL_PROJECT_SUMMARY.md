# Provenance Guard — Final Project Summary

## Project Overview
Provenance Guard is a Python Flask application that evaluates submitted text using two signals: a GPT-2-based model signal and a stylometric signal. It combines the scores to classify submissions as human, unsure, or AI-generated.

The application also supports audit logging, input validation, an appeal workflow, request-duration tracking, and error handling.

## Implementation
- Built and tested Flask API endpoints for text submissions and appeals.
- Integrated model-based and stylometric scoring.
- Implemented combined scoring and three classification labels.
- Added input validation for missing, empty, whitespace-only, and oversized submissions.
- Implemented audit logging for decisions, rejections, and appeals.
- Added request-duration tracking and safe handling of unexpected application errors.
- Tested rate limiting without modifying the Unit 8 files.

## Acceptance Criteria Results

| Criterion | Result |
|---|---|
| False-positive evaluation | Passed |
| Human vs. AI score separation | Not passed |
| Three-label coverage | Passed |
| Appeal workflow | Passed |
| Input validation | Passed |

## Key Findings
The application successfully handled valid and invalid submissions, recorded audit events, and processed appeals without overwriting original decisions.

The score-separation experiment did not meet its target. The average AI score was approximately 0.5297, while the average human score was approximately 0.5966. This demonstrates that the current scoring signals do not reliably distinguish the two groups.

## Final Verification
- Python compilation completed successfully.
- Environment check: 9 passed, 0 failed.
- Git diff whitespace check passed.
- Manual tests were completed for the five acceptance criteria.

## Future Improvements
- Improve the detector's ability to distinguish human-written and AI-generated text.
- Evaluate against a larger, more diverse dataset.
- Calibrate scoring signals using representative training and validation data.
- Test performance and reliability under broader conditions.

## Conclusion
The project demonstrates a functioning text-analysis API with input validation, auditability, appeals, and error handling. Testing also identified an important limitation: the current scoring method does not reliably separate human-written and AI-generated text. This provides a clear direction for future improvement.