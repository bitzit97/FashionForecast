from flask import Flask, request
from web_pages import get_main_page, get_reccs_page
from recomender import get_reccs_by_location

# Create a Flask app
app = Flask(__name__)

# Define a route and a function to handle the route
@app.route('/')
def hello_world():
  location_value = request.args.get('location')
  print(f"The value of 'location' is: [{location_value}]")  
  if location_value:
    print(f"The value of 'location' is: [{location_value}]")
    reccs = get_reccs_by_location(location_value)
    return get_reccs_page(location_value, reccs)
  else:
    return get_main_page()

# Run the app if this file is executed directly
if __name__ == '__main__':
  app.run(debug=True)
