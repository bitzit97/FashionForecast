# get_main_page
def get_main_page():
  return """
  <!DOCTYPE html>
  <html>
  <head>
      <title>Fashion Forecast</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>      
  </head>
  <body class="p-12 flex flex-col flex-1 h-screen bg-gradient-to-b from-lime-50 to-blue-200">
    <div class="text-2xl font-bold text-center w-full" font-family: "Proxima Nova"">Fashion Forecast</div>
    <div class="p-4 h-24 w-full align-middle">
      Do you struggle with picking an outfit in the morning, let alone one that works with the unpredictable weather? Fashion Forecast is the perfect way to help you overcome this. Simply enter what city you live in and press enter! Make sure to spell everything out (no abbreviations)!    
    </div>
    <div class="h-24 w-full">
      <form>
          <label class="p-4" for="cityname">Enter Your City Name:</label>
          <input type="px-2 text font-small" id="cityname" name="location">
          <input class="p-4 cursor-pointer" type="submit" value="Submit">
      </form>
    </div>
  </body>
  </html>
  """


# get_reccs_page
#
def get_reccs_page(location, reccs_data):
  return f"""
  <!DOCTYPE html>
  <html>
  <head>
      <title>Fashion Forecast</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>      
  </head>
  <body class="p-12 flex flex-col flex-1 h-screen bg-gradient-to-b from-lime-50 to-blue-200">
    <div class="text-2xl font-bold text-center w-full">
      Fashion Forecast
    </div>
    <div class="p-4 h-24 w-full align-middle">
      Do you struggle with picking an outfit in the morning, let alone one that works with the unpredictable weather? Fashion Forecast is the perfect way to help you overcome this. Simply enter what city you live in and press enter! Make sure to spell everything out (no abbreviations)!    
    </div>
    <div class="px-1 h-24 w-full">
      <form>
          <label class="p-4" for="cityname">Enter Your City Name:</label>
          <input type="px-2 text font-small" id="cityname" name="location" value="{location}">
          <input class="p-4 cursor-pointer" type="submit" value="Submit">
      </form>
    </div>
    <div class="mx-2 flex flex-row w-full space-x-4">
      {get_day_reccs_block(reccs_data[0], "zinc")}
      {get_day_reccs_block(reccs_data[1], "zinc")}
      {get_day_reccs_block(reccs_data[2], "zinc")}
    </div>
  </body>
  </html>
  """


def get_day_reccs_block(day_forecast, bg_color):
  return f"""
    <div class="py-4 px-2 flex flex-col flex-1 rounded-md bg-{bg_color}-50  w-full shadow-md">
      <div class="h-8 w-full text-center font-medium">
        {day_forecast["week"]}, {day_forecast["date"]}
      </div>          
      <div class="">
        <p class="font-medium">Forecast</p>
        <p>{day_forecast["weather"]}</p>
      </div>
      <div class="">
        <p class="font-medium">Recommended outfit</p>
        <p>{day_forecast["outfit_reccs"]}</p>
      </div>
    </div>
  """


if __name__ == "__main__":
  print("I am useless code block.......")
  print(get_main_page())
