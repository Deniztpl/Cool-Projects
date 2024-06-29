# Weather Notification
This project uses the OpenWeatherMap API and Twilio API to send weather notifications via SMS when rain is forecasted for a specific location in twelve hours.

## Requirements

`pip install twilio`

## Setup

**Environment Variables**:
   - Ensure you have the following environment variables set:
     - `OWM_API_KEY`: Your OpenWeatherMap API key
     - `AUTH_TOKEN`: Your Twilio account authentication token
     - `ACC_SID`: Your Twilio account SID

## Notes
Use pythonanywhere to run the script daily.
