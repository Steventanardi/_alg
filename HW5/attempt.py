import ast

def analyze_program(code):
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.While) and isinstance(node.test, ast.Constant) and node.test.value is True:
                print("Warning: Detected an infinite loop.")
                return False
            if isinstance(node, ast.FunctionDef):
                print("Complex logic detected. Cannot determine halting.")
                return None
        print("No obvious infinite loops detected. The program might halt.")
        return True
    except Exception as e:
        print("Error analyzing the program:", e)
        return None


program_1 = """
while True:
    pass
"""

program_2 = """
for i in range(10):
    print(i)
"""

print("Analyzing Program 1:")
analyze_program(program_1)

print("\nAnalyzing Program 2:")
analyze_program(program_2)
