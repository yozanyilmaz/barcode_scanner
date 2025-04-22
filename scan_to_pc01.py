from flask import Flask, request, render_template, url_for, redirect
import pyautogui
import logging

_logger = logging.getLogger(__name__)

app = Flask(__name__)

history = list()

@app.route('/')
def home():
    return render_template("main_page.html", history=history)


@app.route('/send', methods=['POST'])
def send_text():
    text = request.form.get("text", "")
    if text:
        pyautogui.write(text)  # Simulates typing
        pyautogui.press("enter")  # Optional: Press Enter after typing
        if text not in history:
            history.insert(0, text)
        if len(history) > 15:
            history.pop()
        _logger.info(text)
        print("sent text: ", text)
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_history():
    global history
    history = list()
    return redirect('/')

if __name__ == "__main__":
    ip_addr = input('Enter the IP address:\n')
    app.run(host=ip_addr, port=14500, debug=True)

