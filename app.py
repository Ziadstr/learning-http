from flask import Flask, url_for, make_response

app = Flask(__name__)


@app.route("/one")
def endpoint_one():
    return "This is endpoint one (HTTP 200 OK)"


@app.route("/two")
def endpoint_two():
    return "This is endpoint two (HTTP 201 Created)", 201


@app.route("/three")
def endpoint_three():
    return "This is endpoint three (HTTP 204 No Content)", 204


@app.route("/four")
def endpoint_four():
    return "This is endpoint four (HTTP 400 Bad Request)", 400


@app.route("/five")
def endpoint_five():
    return "This is endpoint five (HTTP 404 Not Found)", 404


@app.route("/six")
def endpoint_six():
    return (
        "This is endpoint six (HTTP 302 Found, Redirecting)",
        302,
        {"Location": url_for("endpoint_one")},
    )


@app.route("/seven")
def endpoint_teapot():
    response = make_response("I'm a teapot (HTTP 418 I'm a teapot)")
    response.status_code = 418
    response.headers["Content-Type"] = "text/html"
    return response, 418


@app.route("/eight")
def endpoint_server_error():
    return "This is a server error (HTTP 500 Internal Server Error)", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
