from flask import Flask, url_for, render_template
import docker_client

app = Flask(__name__)

@app.route("/")
def home():
    cntrs = docker_client.get_containers()    
    return render_template('base.html', cntrs=cntrs)

if __name__ == "__main__":    
    app.run(debug=True, host="0.0.0.0")
    