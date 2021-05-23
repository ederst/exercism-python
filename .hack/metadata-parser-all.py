from comment_parser import comment_parser
import yaml
import inspect

file_name = r".hack/test/test.rs"

inspect.clean

#with open(file_name) as f:

doc_comment = comment_parser.extract_comments(file_name, 'text/x-c')

print(doc_comment)
