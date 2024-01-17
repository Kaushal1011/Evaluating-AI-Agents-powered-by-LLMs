# LLMAO: Evaluating AI Agents powered by LLMs

## Overview
This project explores the integration of Large Language Models (LLMs) in decision-making within various game environments. We investigate how models like GPT-4, GPT-3.5, LLama, Mistral, and Vicuna perform in complex scenarios compared to traditional AI agents. Our focus is on environments such as Blackjack, Grid Navigation, Accessory Environment, and Traffic Signal Evaluation, examining the efficacy of LLMs in these diverse settings.

## More Information

- [**Presentation**](https://github.com/Kaushal1011/Evaluating-AI-Agents-powered-by-LLMs/blob/main/CS483%20LLMAO%20Project%20Presentation.pdf)
- [**Report**](https://github.com/Kaushal1011/Evaluating-AI-Agents-powered-by-LLMs/blob/main/Evaluating_AI_Agents_powered_by_LLMs_Report.pdf)

## Repository Structure
- **`.ipynb_checkpoints`**: Jupyter Notebook checkpoints.
- **`Conversations`**: Logs of LLM conversations.
    - `AccessoryEnvironment` & `TrafficEnvironment`: History of conversations made during human evaluation of LLM Agents for these environments.
- **`Data`**: Dataset produced while doing this project including A* Algorithm-generated data for navigation tasks.
- **`Environments`**: Python scripts for various environments simulated in the project.
- **`Generated`**: Media generated during simulations, including gifs and images.
- **`Notebooks`**: Jupyter Notebooks detailing experiments and simulations.
    - Subfolders for specific environments and experimental setups.
    - Some notebooks are duplicated because they contain results on different LLMs and were duplicated for easier comparison.
- **`Prompts`**: Markdown files with LLM prompts for different scenarios.
- **`Scripts`**: Utility scripts for prompt generation and test case creation.
- **`Evals`**: Human evaluation results' excel sheet for LLMs in Weather/Accessory and Traffic environments.

## Project Components
### Environments
1. **Blackjack**: Evaluating LLM decision-making against an AI agent using a traditional Blackjack setup.
2. **Grid Navigation**: A matrix-based navigation task, where LLMs guide an agent to a target location.
3. **Accessory Environment**: Decision-making based on weather data, where LLMs choose appropriate accessories and clothing.
4. **Traffic Signal Evaluation**: Optimizing traffic flow at intersections, where LLMs make real-time signal control decisions.

### LLMs Used
- GPT-4, GPT-3.5, LLama 2, Mistral Instruct, Vicuna, and OpenChat 3.5.

### Methodology
- Integration of LLMs as the 'brain' of agents in simulated environments.
- Use of various techniques like baseline prompting, chain of thought, and few-shot learning to enhance LLM performance.

## Setup and Installation
1. **Clone the Repository**: `git clone 'this-repo-url'`

## Running the Experiments

The project requires LM studio to be installed. The following steps are required to run the experiments:
- Install LM studio
- Start LM studio
- Download the Large Language Models (LLMs) from the LM studio
- Load the LLMs in the LM studio
- Start the API server
- Install requirements for the notebooks (gymansium, etc.)
- Run the notebooks

### To generate prompt data / test cases for human evaluted environments
- Run the scripts in the Scripts folder
- Run the environment scripts in the Environments folder

## Analysis and Results
The following are the key components of the analysis and results and can be found in our project report:
- Summary of findings from each environment.
- Comparative analysis of LLMs' performance against AI agents.
- Human evaluation of LLMs' decision-making.
- Discussion of the limitations of LLMs in decision-making.
- Future work and potential improvements.

