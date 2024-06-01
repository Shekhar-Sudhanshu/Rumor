import language_tool_python as checker
tool = checker.LanguageTool('en-US')

def check_grammar(text):
    matches = tool.check(text)
    for match in matches:
        return match.message
    

def correct_grammar(text):
    matches = tool.check(text)
    corrected_text = checker.utils.correct(text, matches)
    return corrected_text
