import docstring_parser
import ast
import yaml

file_name = r"high-scores/high_scores.py"


def parse_docstring_from_file(f):
    return ast.get_docstring(ast.parse(''.join(f)))


with open(file_name) as f:
    doc_string = docstring_parser.parse(parse_docstring_from_file(f))

print("The doc string:")
print("Short description", doc_string.short_description)
print("Long description", doc_string.long_description)

# Note: possible do it via params
print("Params:")
for param in doc_string.params:
    print(f"- {param.arg_name}: {param.description}")

# Note:
#   or do it via long description + yaml/json whatever
#   ^ probably the better solution for it being a more general approach for other languages as well:
#     rust/c/c++/whatever:
#       /*
#        *  Short description
#        *
#        *  <Yaml as long description meta whatever>
#        */
exercism_metadata = yaml.safe_load(doc_string.long_description)

print(exercism_metadata)



