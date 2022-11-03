SUBMIT = "assessment.doConfirmSubmit(submitAssessment);"

def value_set (value, id):
    if value is None:
        return None
    return (f"document.getElementById('{id}').value = '{value}'")

def write_js (lines):
    index = 0
    with open("output.js","w") as output:
        for line in lines:
            if line is None:
                continue
            output.write(line + ";")
            index += 1
        output.write(SUBMIT)
    return index

