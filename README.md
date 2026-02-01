# Local PII Scrubber (PoC)

A "Low Tech" Proof-of-Concept for running enterprise-grade PII (Personally Identifiable Information) scrubbing entirely on local hardware using Small Language Models (SLMs).

**As seen in my [LinkedIn Article](https://www.linkedin.com/pulse/8gb-barrier-why-enterprise-ai-needs-go-diet-gopal-agrawal-vgv9c).**

## The "Why"
Enterprise AI often defaults to massive cloud models (GPT-4, Claude) for simple tasks. This project demonstrates that **Microsoft Phi-3 Mini** (3.8B parameters) can effectively identify and redact sensitive data on a standard 8GB laptop with:
* **Zero Cloud Cost**
* **100% Data Privacy (Offline)**
* **<1.6GB RAM Footprint**

## Prerequisites
1.  **Ollama**: [Download here](https://ollama.com)
2.  **Python 3.8+**
3.  **Hardware**: Tested on MacBook Air M1/M2/M3 (8GB RAM).

## Installation

```bash
# 1. Clone the repo
git clone [https://github.com/goagrawal-genai/PIITest.git](https://github.com/goagrawal-genai/PIITest.git)
cd PIITest

# 2. Install dependencies
pip install -r requirements.txt

# 3. Pull the "Edge-Safe" Model
ollama pull phi3:mini
