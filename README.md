# LPI Agent - Yash Vardhan

## What this is
This is my Level 3 AI Agent for the LPI Developer Kit.

It uses LPI tools to:
- retrieve knowledge
- show case studies
- provide explainable output

## How to run

1. Clone both repos:

git clone https://github.com/Yashjal11/lpi-agent-yash.git  
git clone https://github.com/Life-Atlas/lpi-developer-kit.git  

2. Setup LPI:

cd lpi-developer-kit  
npm install  
npm run build  

3. Run agent:

cd ../lpi-agent-yash  
python agent.py  

## Example

Input:
Explain smart buildings

Output includes:
- LPI tool results
- explanation
- sources

## Explainability

If user asks "why", agent explains:
- which tools were used
- why they were used
