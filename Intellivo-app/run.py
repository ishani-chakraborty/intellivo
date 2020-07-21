from intellivo_package import app, socketio

# run the app 
if __name__ == '__main__':
    # init_db()
    # Change the debug to False when deploying to production
    socketio.run(app, debug=False)
    app.run(debug=False, host='0.0.0.0')
