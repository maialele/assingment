from flask import Flask, render_template
import docker

cli = docker.DockerClient()
containers = cli.containers.list()


app = Flask(__name__)

@app.route("/")
def display_containers():
    return render_template ("index.html", stringContainers=containers)
if __name__ == '__main__':
	app.run(debug=True)
