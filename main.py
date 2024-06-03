from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/capture_event", methods=["POST"])
def capture_event():
    try:
        event_data = request.json["event"]

        if event_data == "start":
            print("Start")
            return jsonify({"event": event_data})
        elif event_data == "stop":
            print("Stop")
            return jsonify({"event": event_data})
        elif event_data == "up":
            print("Up")
            return jsonify({"event": event_data})
        elif event_data == "down":
            print("Down")
            return jsonify({"event": event_data})
        elif event_data == "left":
            print("Left")
            return jsonify({"event": event_data})
        elif event_data == "right":
            print("Right")
            return jsonify({"event": event_data})
        elif event_data == "reset":
            print("Reset")
            return jsonify({"event": event_data})
        else:
            return jsonify({"message": "Event not recognized"})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


if(__name__ == "__main__"):
    app.run(port=5000, debug=True)
