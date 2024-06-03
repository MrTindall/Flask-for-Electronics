from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/capture_event", methods=["POST"])
def capture_event():
    try:
        event_data = request.json["event"]
        print(event_data)
        if event_data == "start":

            return jsonify({"event": event_data})
        elif event_data == "stop":
            pass
        elif event_data == "up":
            pass
        elif event_data == "down":
            pass
        elif event_data == "left":
            pass
        elif event_data == "right":
            pass
        elif event_data == "reset":
            pass
        else:
            return jsonify({"message": "Event not recognized"})

        return jsonify({"event": event_data})
    
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


if(__name__ == "__main__"):
    app.run(port=5000, debug=True)
