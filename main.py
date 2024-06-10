from flask import Flask, render_template, request, jsonify
import threading
from functions.functions import * 

app = Flask(__name__)

func = Functions()


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/capture_event", methods=["POST"])
def capture_event():
    try:
        event_data = request.json["event"]
        number_data = request.json["number"]
        print(event_data)

        if event_data == "start":
            func.set_is_running(True)
            first_thread = threading.Thread(target=func.count_to_100)
            second_thread = threading.Thread(target=func.print_hello_100_times)
            first_thread.start()
            second_thread.start()

        elif event_data == "stop":
            func.set_is_running(False)

        elif event_data == "up":
            pass

        elif event_data == "down":
            pass

        elif event_data == "left":
            pass

        elif event_data == "right":
            pass

        elif event_data == "reset":
            print("The number was " + number_data)

        else:
            return jsonify({"message": "Event not recognized"})

        return jsonify({"event": event_data})

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


if(__name__ == "__main__"):
    app.run(port=5750, debug=True)
