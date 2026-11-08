from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


@app.route("/kenttä/<icao>")
def hae_lentokentta(icao):

    yhteys = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="uskomatontabreinii"
    )

    kursori = yhteys.cursor(dictionary=True)

    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao.upper(),))

    tulos = kursori.fetchone()

    kursori.close()
    yhteys.close()

    if tulos:
        return jsonify({
            "ICAO": tulos["ident"],
            "Name": tulos["name"],
            "Municipality": tulos["municipality"]
        })

    return jsonify({"error": "Lentokenttää ei löytynyt"}), 404


if __name__ == "__main__":
    app.run(port=3000, debug=True)
