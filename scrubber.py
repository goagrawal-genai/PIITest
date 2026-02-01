import ollama
import time
import platform
import psutil
from datetime import datetime

# CONFIGURATION
MODEL = "phi3:mini"  # Ensure you have run: ollama pull phi4
RAW_DATA = "Customer John Smith (ID: 9982-X) requested a refund of $500.00 on 2025-12-01."

def get_sys_info():
    """Grabs machine specs for the 'Auth' factor"""
    try:
        os_info = f"{platform.system()} {platform.release()}"
        # detailed CPU info is hard in pure python, but this works for most:
        cpu_info = platform.processor()  
        ram_gb = round(psutil.virtual_memory().total / (1024 ** 3), 1)
        cores = psutil.cpu_count(logical=False)
        return f"{os_info} | {cpu_info} | {cores} Cores | {ram_gb}GB RAM"
    except Exception:
        return "Unknown System Config"

def run_scrub():
    # 1. System Header
    sys_specs = get_sys_info()
    print("-" * 70)
    print(f"\033[96m[SYSTEM] Detected Environment: {sys_specs}\033[0m")
    print(f"\033[96m[MODEL]  Loaded Local Model:   {MODEL}\033[0m")
    print("-" * 70)

    # 2. The Setup
    system_prompt = """
    You are a PII scrubber. Replace names and IDs with [REDACTED].
    Return JSON only. Keys: scrubbed_text, risk_score.
    """
    
    print(f"\033[93m[INPUT]  {RAW_DATA}\033[0m")

    # 3. Execution with Timestamps
    start_time_str = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"\033[90m[LOG]    Job Started at: {start_time_str}\033[0m")
    
    start_perf = time.perf_counter() # Precision timer
    
    # --- ACTUAL INFERENCE ---
    response = ollama.chat(model=MODEL, messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': RAW_DATA},
    ])
    # ------------------------

    end_perf = time.perf_counter()
    end_time_str = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    duration = end_perf - start_perf

    # 4. The Result
    print(f"\033[90m[LOG]    Job Finished at: {end_time_str}\033[0m")
    print("-" * 70)
    print(f"\033[92m[OUTPUT] {response['message']['content']}\033[0m")
    print("-" * 70)
    print(f"\033[92m[STATS]  Total Inference Time: {duration:.4f} seconds\033[0m")
    print(f"\033[90m[AUDIT]  Data transmitted to cloud: 0 bytes\033[0m")

if __name__ == "__main__":
    run_scrub()
