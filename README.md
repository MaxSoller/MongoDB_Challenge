## Flattening a JSON file

A tool to flatten a JSON object into flattened version of the JSON object, with keys as the path to every terminal value in the JSON structure. Output should be valid JSON.

## Usage

```bash
cat in.json | python3 flatten.py [outputfile]
```

or

```bash
python3 flatten.py [outputfile] < in.json
```
The output file will then contain the flattened JSON content.

If you do not specify the output file, it will be written to 'result.json'.

 


