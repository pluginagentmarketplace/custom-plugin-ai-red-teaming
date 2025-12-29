#!/usr/bin/env python3
"""
Red Team Framework Selector
Choose appropriate framework based on target and scope
"""

import json
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class Framework:
    """Red team framework definition"""
    name: str
    focus: str
    tools: List[str]
    best_for: List[str]
    complexity: str


class FrameworkSelector:
    """Select appropriate red team framework"""

    FRAMEWORKS = {
        "pyrit": Framework(
            name="PyRIT (Python Risk Identification Tool)",
            focus="LLM Security Testing",
            tools=["Prompt injection", "Jailbreak testing", "Content safety"],
            best_for=["Azure OpenAI", "General LLMs", "Automated testing"],
            complexity="Medium"
        ),
        "garak": Framework(
            name="Garak",
            focus="LLM Vulnerability Scanning",
            tools=["Probe generation", "Detector modules", "Reporting"],
            best_for=["Quick scans", "CI/CD integration", "Multiple models"],
            complexity="Low"
        ),
        "promptfoo": Framework(
            name="PromptFoo",
            focus="LLM Testing & Evaluation",
            tools=["Test cases", "Assertions", "Comparison"],
            best_for=["Prompt engineering", "Regression testing", "A/B testing"],
            complexity="Low"
        ),
        "counterfit": Framework(
            name="Counterfit",
            focus="Adversarial ML",
            tools=["Attack algorithms", "Evasion", "Model stealing"],
            best_for=["ML models", "Computer vision", "Adversarial examples"],
            complexity="High"
        ),
        "art": Framework(
            name="Adversarial Robustness Toolbox",
            focus="Adversarial ML Research",
            tools=["Attacks", "Defenses", "Metrics"],
            best_for=["Research", "Deep learning", "Comprehensive testing"],
            complexity="High"
        ),
        "textattack": Framework(
            name="TextAttack",
            focus="NLP Adversarial Attacks",
            tools=["Text perturbations", "Attack recipes", "Augmentation"],
            best_for=["NLP models", "Text classification", "Robustness"],
            complexity="Medium"
        )
    }

    def recommend(self, target_type: str, scope: str, expertise: str) -> List[Dict]:
        """Recommend frameworks based on requirements"""
        recommendations = []

        for key, fw in self.FRAMEWORKS.items():
            score = 0

            # Match target type
            if target_type.lower() in str(fw.best_for).lower():
                score += 3

            # Match scope
            if scope.lower() in str(fw.focus).lower():
                score += 2

            # Match expertise
            complexity_map = {"beginner": "Low", "intermediate": "Medium", "expert": "High"}
            if fw.complexity == complexity_map.get(expertise.lower(), "Medium"):
                score += 1

            if score > 0:
                recommendations.append({
                    "framework": key,
                    "name": fw.name,
                    "score": score,
                    "focus": fw.focus,
                    "complexity": fw.complexity
                })

        return sorted(recommendations, key=lambda x: x["score"], reverse=True)

    def get_framework_details(self, name: str) -> Dict:
        """Get detailed framework information"""
        if name not in self.FRAMEWORKS:
            return {"error": f"Unknown framework: {name}"}

        fw = self.FRAMEWORKS[name]
        return {
            "name": fw.name,
            "focus": fw.focus,
            "tools": fw.tools,
            "best_for": fw.best_for,
            "complexity": fw.complexity,
            "install": f"pip install {name}" if name != "art" else "pip install adversarial-robustness-toolbox"
        }


def main():
    selector = FrameworkSelector()

    print("Red Team Framework Selector")
    print("=" * 50)

    # Example recommendation
    recs = selector.recommend(
        target_type="LLM",
        scope="security",
        expertise="intermediate"
    )

    print("\nRecommended Frameworks:")
    for rec in recs[:3]:
        print(f"  {rec['score']}/6: {rec['name']} ({rec['complexity']})")

    print("\nFramework Details:")
    details = selector.get_framework_details("pyrit")
    print(json.dumps(details, indent=2))


if __name__ == "__main__":
    main()
