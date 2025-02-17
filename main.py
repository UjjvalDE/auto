import os
import random
import requests
import subprocess
import github3
from urllib.parse import urljoin
from pathlib import Path

# --- CONFIGURATION ---
GITHUB_REPO = "UjjvalDE/hackerearth"        # Format: "username/repo"
GITHUB_TOKEN = "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"   # Store token in environment variables
OLLAMA_MODEL = "llama3:latest"
SOLUTIONS_DIR = Path("./solutions")

# --- PROBLEM FETCHING ---
def get_random_leetcode_problem():
    try:
        response = requests.get("https://leetcode.com/api/problems/all/", timeout=10)
        response.raise_for_status()
        problems = [p for p in response.json()["stat_status_pairs"] if not p["paid_only"]]
        problem = random.choice(problems)
        return (
            problem["stat"]["question__title"],
            f"https://leetcode.com/problems/{problem['stat']['question__title_slug']}/"
        )
    except Exception as e:
        print(f"Error fetching problem: {e}")
        raise

# --- AI SOLUTION GENERATION ---
def solve_with_ollama(problem_title, problem_url):
    prompt = (
        f"Provide only the Python solution code for this LeetCode problem.\n"
        f"Problem: {problem_title}\n"
        f"URL: {problem_url}\n"
        "Return only the Python code without any explanations or markdown formatting."
    )
    
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
            timeout=300
        )
        # Clean the output to extract pure Python code
        code = result.stdout.strip()
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0]
        elif "```" in code:
            code = code.split("```")[1].split("```")[0]
        return code.strip()
    except Exception as e:
        print(f"Error generating solution: {e}")
        return None

# --- SOLUTION MANAGEMENT ---
def save_solution(title, content):
    SOLUTIONS_DIR.mkdir(exist_ok=True)
    safe_title = "".join(c if c.isalnum() else "_" for c in title)
    filepath = SOLUTIONS_DIR / f"{safe_title}.py"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content if content else "# Solution generation failed")
    return filepath

# --- GITHUB INTEGRATION ---
def push_to_github(filepath):
    try:
        gh = github3.login(token=GITHUB_TOKEN)
        repo = gh.repository(*GITHUB_REPO.split("/"))
        
        with open(filepath, "rb") as f:  # Read as bytes
            content = f.read()
            
        repo.create_file(
            path=str(filepath.relative_to(SOLUTIONS_DIR)),
            message=f"Add solution for {filepath.stem}",
            content=content,
            branch="main"
        )
        return True
    except Exception as e:
        print(f"GitHub error: {e}")
        return False

# --- MAIN WORKFLOW ---
def main():
    try:
        title, url = get_random_leetcode_problem()
        print(f"Working on: {title}\n{url}")
        
        solution = solve_with_ollama(title, url)
        if not solution:
            print("Failed to generate solution")
            return
            
        solution_file = save_solution(title, solution)
        
        if push_to_github(solution_file):
            print(f"✅ Successfully pushed {solution_file.name} to GitHub!")
        else:
            print("❌ Failed to push to GitHub")
            
    except Exception as e:
        print(f"Critical error: {e}")

if __name__ == "__main__":
    main()