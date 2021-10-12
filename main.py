from website import create_app

app =create_app()
if __name__ == '__main__':  #Only if this file is ran (not imported)
    app.run(debug = True)   #This line will be executed and the flask server will be created, along side activating live changes on the page
                            # a.k.a. refreshing the page every time a change in source code is made

