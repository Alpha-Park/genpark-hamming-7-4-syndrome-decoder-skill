import sys
import json
from client import Hamming74

def main():
    ham = Hamming74()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "encode":
            c = ham.encode(params.get("data", []))
            res = {"codeword": c}
        elif method == "decode":
            d, err = ham.decode(params.get("codeword", []))
            res = {"data": d, "error_position": err}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
