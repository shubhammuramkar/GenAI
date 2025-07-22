import openai
import json
from typing import Dict, List

class PromptingTechniques:
    """
    Demonstrates various prompting techniques for AI models
    """
    
    def __init__(self, api_key: str = None):
        # Initialize your AI client (OpenAI example)
        # self.client = openai.OpenAI(api_key=api_key)
        pass
    
    def basic_prompt(self, query: str) -> str:
        """Basic prompting - simple question/instruction"""
        prompt = f"Answer this question: {query}"
        return prompt
    
    def role_based_prompt(self, topic: str, role: str = "expert") -> str:
        """Role-based prompting - assign a specific role"""
        prompt = f"""You are a {role} in {topic}. 
        Please explain {topic} in a way that demonstrates your expertise.
        Include practical examples and best practices."""
        return prompt
    
    def few_shot_prompt(self, examples: List[Dict], new_input: str) -> str:
        """Few-shot prompting - provide examples for pattern recognition"""
        prompt = "Here are some examples:\n\n"
        
        for i, example in enumerate(examples, 1):
            prompt += f"Example {i}:\n"
            prompt += f"Input: {example['input']}\n"
            prompt += f"Output: {example['output']}\n\n"
        
        prompt += f"Now, following the same pattern:\nInput: {new_input}\nOutput:"
        return prompt
    
    def chain_of_thought_prompt(self, problem: str) -> str:
        """Chain of thought - ask for step-by-step reasoning"""
        prompt = f"""Solve this problem step by step. Think through each step carefully:

        Problem: {problem}
        
        Please show your reasoning process:
        Step 1:
        Step 2:
        Step 3:
        ...
        
        Final Answer:"""
        return prompt
    
    def structured_output_prompt(self, topic: str, format_type: str = "json") -> str:
        """Request structured output in specific format"""
        if format_type == "json":
            prompt = f"""Analyze {topic} and provide your response in the following JSON format:
            {{
                "summary": "brief summary",
                "key_points": ["point 1", "point 2", "point 3"],
                "pros": ["advantage 1", "advantage 2"],
                "cons": ["disadvantage 1", "disadvantage 2"],
                "recommendation": "your recommendation"
            }}"""
        elif format_type == "markdown":
            prompt = f"""Write about {topic} using this markdown structure:
            # {topic}
            
            ## Overview
            [Brief overview]
            
            ## Key Features
            - Feature 1
            - Feature 2
            
            ## Conclusion
            [Your conclusion]"""
        
        return prompt
    
    def context_aware_prompt(self, context: str, question: str) -> str:
        """Context-aware prompting - provide relevant background"""
        prompt = f"""Context: {context}
        
        Based on the above context, please answer the following question:
        {question}
        
        Make sure your answer is relevant to the provided context."""
        return prompt
    
    def constraint_prompt(self, topic: str, constraints: List[str]) -> str:
        """Add specific constraints to guide the response"""
        prompt = f"Write about {topic} with these constraints:\n"
        for constraint in constraints:
            prompt += f"- {constraint}\n"
        prompt += f"\nTopic: {topic}"
        return prompt
    
    def iterative_prompt(self, initial_query: str, refinements: List[str]) -> str:
        """Build prompts iteratively with refinements"""
        prompt = f"Initial request: {initial_query}\n\n"
        prompt += "Please also consider these additional requirements:\n"
        for refinement in refinements:
            prompt += f"- {refinement}\n"
        return prompt

# Example usage and demonstrations
def demonstrate_prompting():
    """Demonstrate different prompting techniques"""
    
    pt = PromptingTechniques()
    
    # 1. Basic Prompt
    print("=== BASIC PROMPT ===")
    basic = pt.basic_prompt("What is machine learning?")
    print(basic)
    print()
    
    # 2. Role-based Prompt
    print("=== ROLE-BASED PROMPT ===")
    role_based = pt.role_based_prompt("Python programming", "senior software engineer")
    print(role_based)
    print()
    
    # 3. Few-shot Prompt
    print("=== FEW-SHOT PROMPT ===")
    examples = [
        {"input": "dog", "output": "animal"},
        {"input": "car", "output": "vehicle"},
        {"input": "apple", "output": "fruit"}
    ]
    few_shot = pt.few_shot_prompt(examples, "rose")
    print(few_shot)
    print()
    
    # 4. Chain of Thought
    print("=== CHAIN OF THOUGHT PROMPT ===")
    cot = pt.chain_of_thought_prompt("If a train travels 60 mph for 2 hours, then 80 mph for 3 hours, what's the average speed?")
    print(cot)
    print()
    
    # 5. Structured Output
    print("=== STRUCTURED OUTPUT PROMPT ===")
    structured = pt.structured_output_prompt("Python vs JavaScript", "json")
    print(structured)
    print()
    
    # 6. Context-aware
    print("=== CONTEXT-AWARE PROMPT ===")
    context = "You are helping a beginner programmer who just learned basic Python syntax"
    question = "How should I organize my first Python project?"
    context_prompt = pt.context_aware_prompt(context, question)
    print(context_prompt)
    print()
    
    # 7. Constraint-based
    print("=== CONSTRAINT-BASED PROMPT ===")
    constraints = [
        "Use simple language suitable for beginners",
        "Include practical examples",
        "Keep response under 200 words",
        "Focus on actionable advice"
    ]
    constraint_prompt = pt.constraint_prompt("learning data science", constraints)
    print(constraint_prompt)
    print()

# Advanced prompting patterns
class AdvancedPromptPatterns:
    """Advanced prompting patterns and techniques"""
    
    @staticmethod
    def temperature_control_example():
        """Example of how temperature affects responses"""
        return {
            "low_temperature": {
                "temp": 0.1,
                "prompt": "Write a technical explanation of recursion",
                "expected": "Focused, consistent, technical response"
            },
            "high_temperature": {
                "temp": 0.9,
                "prompt": "Write a creative story about recursion",
                "expected": "Creative, varied, imaginative response"
            }
        }
    
    @staticmethod
    def prompt_chaining_example():
        """Example of chaining multiple prompts"""
        chain = [
            "Step 1: Analyze the problem and identify key components",
            "Step 2: Based on step 1, propose three potential solutions",
            "Step 3: Evaluate each solution from step 2 for feasibility",
            "Step 4: Select the best solution and create an implementation plan"
        ]
        return chain
    
    @staticmethod
    def metacognitive_prompt():
        """Prompt that asks AI to think about its thinking"""
        return """Before answering, please:
        1. Identify what type of question this is
        2. Consider what information you need
        3. Think about potential pitfalls in your reasoning
        4. Then provide your answer
        
        Question: [Your question here]"""

# Best practices for prompting
PROMPTING_BEST_PRACTICES = {
    "clarity": "Be specific and clear about what you want",
    "context": "Provide relevant background information",
    "examples": "Use examples to illustrate desired output",
    "format": "Specify the desired output format",
    "constraints": "Set clear boundaries and limitations",
    "iteration": "Refine prompts based on results",
    "testing": "Test prompts with different inputs"
}

if __name__ == "__main__":
    demonstrate_prompting()
    
    # Print best practices
    print("\n=== PROMPTING BEST PRACTICES ===")
    for key, value in PROMPTING_BEST_PRACTICES.items():
        print(f"{key.title()}: {value}")