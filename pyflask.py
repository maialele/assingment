from flask import Flask, render_template
import docker

cli = docker.DockerClient()
containers = cli.containers.list()
print(containers)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template ("index.html", stringContainers=''.join(str(x) for x in containers))
if __name__ == '__main__':
	app.run(debug=True)
