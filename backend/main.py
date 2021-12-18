from website import create_app

app = create_app()

# if 'main' is imported elsewhere, equality not satisfied
if __name__ == '__main__':
    app.run(debug=True)