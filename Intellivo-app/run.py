from intellivo_package import app, socketio

# run the app 
if __name__ == '__main__':
    # init_db()
    socketio.run(app, debug=True)
    app.run(debug=True)

